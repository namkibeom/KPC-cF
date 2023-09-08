# Korean-ABSA
Korean Aspect-Based Sentiment Analysis via NLI model-Based Pseudo-Label using Translated Dataset

홍익대학교 산업공학과 졸업 프로젝트입니다.

<img src="image/abstract.png" width="400" height="600">


## Evaluation (Categorical Prompt)
| Model(Kor-SemEval) | Precision |  Recall | F1 score | 4-way acc | 3-way acc | Binary |
|:------------------:|:---------:|:-------:|:--------:|:---------:|:---------:|:------:|
| M-BERT-single      |   92.16   |  77.95  |   84.46  |   68.20   |   71.84   |  77.95 |
| XLM-R-single       |   91.01   |  49.37  |   64.01  |   62.93   |   66.29   |  75.20 | 
| M-BERT-NLI         |   91.10   |  79.90  |   85.14  |   73.95   |   77.90   |  84.87 | 
| XLM-R-NLI          |   91.37   |  83.71  |   87.37  |   79.41   |   83.66   |  89.98 |
| NLI-ensemble       |   93.70   |  81.27  |   87.04  |   78.24   |   82.43   |  89.65 |
