# <span style="font-variant:small-caps;">KPC-cF</span> 

> **<span style="font-variant:small-caps;">KPC-cF: Aspect-Based Sentiment Analysis via Implicit-Feature Alignment with Corpus Filtering**<br>
> [Kibeom Nam](https://www.linkedin.com/in/Kibeom-nam/)<sup>1,2</sup>   
> <sup>1</sup>Hongik university <sup>2</sup>MODULABS



<a href="https://drive.google.com/file/d/1ZVGuA9SUBJ4EkunWIX8scXaYDDCENrfd/view"><img src="https://img.shields.io/static/v1?label=Paper&message=Arxiv:KPC-cF&color=red&logo=arxiv"></a> &ensp;
<a href="https://huggingface.co/KorABSA/KPC-cF"><img src="https://img.shields.io/badge/Model-Checkpoints-blue"></a> &ensp;


## Abstract
### Keywords
> ABSA in Low-resource language / Dual filtering
### TL;DR
>  We addressed the language gap issue in ABSA by building a pseudo-classifier. This involved fine-tuning an NLI model with translated data, performing LaBSE scoring on Korean NLI pairs, and further fine-tuning with optimal pseudo-labels.

<details><summary>FULL abstract</summary>
> Investigations into Aspect-Based Sentiment Analysis (ABSA) for Korean industrial reviews are notably lacking in the existing literature. Our research proposes an intuitive and effective framework for ABSA in low-resource languages such as Korean. It optimizes prediction labels by integrating translated benchmark and unlabeled Korean data. Using a model fine-tuned on translated data, we pseudo-labeled the actual Korean NLI set. Subsequently, we applied LaBSE and MSP-based filtering to this pseudo-NLI set as implicit feature, enhancing Aspect Category Detection and Polarity determination through additional training. Incorporating dual filtering, this model bridged dataset gaps, achieving positive results in Korean ABSA with minimal resources. Through additional data injection pipelines, our approach aims to utilize high-resource data and construct effective models within communities, whether corporate or individual, in low-resource language countries. Compared to English ABSA, our framework showed an approximately 3% difference in F1 scores and accuracy. We release the dataset and our code for Korean ABSA, at this link: https://github.com/namkibeom/KPC-cF.
</details>

## Flowchart
<p align="center">
  <img align="middle" width="850" src="image/paper_figure(3).png">
</p>

## Dataset
**Kor-SemEval**
> Train set : Machine translated [SemEval14 dataset](https://github.com/HSLCY/ABSA-BERT-pair)   
> Test set : Machine translated + Human 
correction SemEval14

**[KR3](https://github.com/yejoon-lee/kr3) subset**
> Train set : Pseudo labeled by fine-tuning(Kor-SemEval) model   
> Test set : Gold Label

## Evaluation 

**Aspect Category Detection (ACD)**
> Precision, Recall, F1 score

**Aspect Category Polarity (ACP)**
> 4-way, 3-way, Binary Acc

<!--
**KR3 test**
<p align="center">
  <img src="image/paper_figure(4).png" width="500" height="150">
</p>

## Embedding Visualization

<p align="center">
  <img src="image/Figure_tSNE.png" style="max-width: 350px; height: auto;" alt="">
</p>
-->
<!--
## Performance of ACD and ACP during fine-tuning 

<p align="center">
 <img src="image/paper_plot.png" width="600" height="600">
</p>
-->

## Probability Distribution

<p align="center">
  <img align="middle" width=“750" src="image/Figure_ProbDist.png">
</p>

## To-Do List

- [ ]  Inference code [(HuggingFace)](https://huggingface.co/KorABSA)
- [ ]  Filtering & Training code
  


## Acknowledgement
> This research was supported by Brian Impact, a non-profit organization dedicated to the advancement of science and technology.
