#!/bin/bash

python dual_filtering.py --target_data <path_to_target_data> \
                          --model_labse 'sentence-transformers/LaBSE' \
                          --model_pre 'KorABSA/XLM-NLI-M-KorSemEval' \
                          --batch_size 16 \
                          --threshold_msp 0.5 \
                          --pbar True


python training.py --filtered_data_path final_batch.pkl \
                    --model_pre 'KorABSA/XLM-NLI-M-KorSemEval' \
                    --epochs 4 \
                    --batch_size 16 \
                    --learning_rate 2e-5
