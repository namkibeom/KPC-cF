import numpy as np
import torch
import math
import pickle
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sentence_transformers import SentenceTransformer

def normalization(embeds):
    norms = torch.linalg.norm(embeds, 2, 1, keepdims=True)
    return embeds / norms

def calculate_labse_score(x_s, x_a, model_labse):
    embeddings_s = model_labse.encode(x_s, convert_to_tensor=True)
    embeddings_a = model_labse.encode(x_a, convert_to_tensor=True)

    embeddings_s = normalization(embeddings_s)
    embeddings_a = normalization(embeddings_a)

    labse_score = torch.matmul(embeddings_s, embeddings_a.T)
    return labse_score

def get_msp_and_prediction(model_pre, tokenizer_pre, x_s, x_a):
    inputs = tokenizer_pre(x_s, x_a, return_tensors='pt', truncation=True, padding=True)
    outputs = model_pre(**inputs)
    logits = outputs.logits
    probs = torch.softmax(logits, dim=-1)

    pred_label = torch.argmax(logits, dim=-1).item()
    score_msp = torch.max(probs).item()

    return pred_label, score_msp

def SAMPLING(Target_data, model_labse, model_pre, tokenizer_pre, batch_size, threshold_MSP=0.5, pbar=True):
    clean_data = []
    
    for sample in Target_data:
        x_s, x_a = sample
        if len(x_s.strip()) > 0 and len(x_a.strip()) > 0:
            clean_data.append(sample)
    
    num_batches = math.ceil(len(clean_data) / batch_size)
    selected_batch = []
    temp_scores_L = []

    if pbar:
        for i in tqdm(range(num_batches)):
            batch = clean_data[i * batch_size : i * batch_size + batch_size]

            for x_s, x_a in batch:
                score_L = calculate_labse_score([x_s], [x_a], model_labse)
                temp_scores_L.append(score_L.item())

                y, score_MSP = get_msp_and_prediction(model_pre, tokenizer_pre, x_s, x_a)

                if score_MSP > threshold_MSP:
                    selected_batch.append((x_s, x_a, y, score_L))

    else:
        for i in range(num_batches):
            batch = clean_data[i * batch_size : i * batch_size + batch_size]

            for x_s, x_a in batch:
                score_L = calculate_labse_score([x_s], [x_a], model_labse)
                temp_scores_L.append(score_L.item())

                y, score_MSP = get_msp_and_prediction(model_pre, tokenizer_pre, x_s, x_a)

                if score_MSP > threshold_MSP:
                    selected_batch.append((x_s, x_a, y, score_L))

    avg_L = np.mean(temp_scores_L)
    final_batch = [sample for sample in selected_batch if sample[3].item() > avg_L]

    return final_batch

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Sampling with LaBSE and a classification model.")
    parser.add_argument('--target_data', type=str, required=True, help="Path to the target data file.")
    parser.add_argument('--model_labse', type=str, required=True, help="Pretrained LaBSE model identifier.")
    parser.add_argument('--model_pre', type=str, required=True, help="Pretrained model identifier for Ψpre.")
    parser.add_argument('--batch_size', type=int, default=32, help="Batch size for processing.")
    parser.add_argument('--threshold_msp', type=float, default=0.5, help="Threshold for MSP score.")
    parser.add_argument('--pbar', type=bool, default=True, help="Show progress bar (True/False).")

    args = parser.parse_args()

    model_labse = SentenceTransformer('sentence-transformers/LaBSE')  # Using sentence-transformers for LaBSE

    model_pre = AutoModelForSequenceClassification.from_pretrained('KorABSA/XLM-NLI-M-KorSemEval')
    tokenizer_pre = AutoTokenizer.from_pretrained(args.model_pre)

    # Load target data
    # Here we assume target data is a list of tuples (x_s, x_a)
    Target_data = [("review sentence", "aspect")]

    final_batch = SAMPLING(Target_data, model_labse, model_pre, tokenizer_pre, args.batch_size, args.threshold_msp, args.pbar)

    #print(f"Final Batch Size: {len(final_batch)}")
    #print(final_batch)
    
    with open("final_batch.pkl", "wb") as f:
        pickle.dump([(x_s, x_a, y) for (x_s, x_a, y, _) in final_batch], f)