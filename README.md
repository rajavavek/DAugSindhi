# DAugSindhi: A Data Augmentation Approach for Enhancing Sindhi Language Text Classifcation

[![GitHub](https://img.shields.io/badge/GitHub-Code-blue?logo=github)](https://github.com/rajavavek/DAugSindhi) [![Paper](https://img.shields.io/badge/Paper-DOI:10.1007/s44248--025--00040--8-red?logo=read-the-docs)](https://doi.org/10.1007/s44248-025-00040-8) [![Web](https://img.shields.io/badge/Web-DAugSindhi-grey)](https://rajavavek.github.io/DAugSindhi/) 

[![Authors](https://img.shields.io/badge/Authors-Raja_Vavekanand,_Bhagwan_Das,_Teerath_Kumar-pink?logo=academia)](#)

## Abstract
This paper presents DAugSindhi, a data augmentation approach for improving Sindhi text classification, addressing the scarcity of annotated datasets. The study evaluates techniques like Easy Data Augmentation (EDA), Back Translation, Paraphrasing, and Text Generation using Large Language Models (LLMs). Experiments on a Sindhi dataset of 3364 news articles showed that EDA, especially Random Deletion, achieved the highest performance with a 99% F1 score in binary classification. Back Translation and Paraphrasing also provided notable improvements. This work sets a strong baseline for Sindhi text classification and highlights the potential of simple augmentation methods for enhancing NLP in low-resource languages. 


## Overview

**Sindhi**, a low-resource language spoken by millions, faces significant challenges in Natural Language Processing (NLP) due to the scarcity of annotated datasets. This project, titled **DAugSindhi**, addresses these challenges by enhancing Sindhi text classification through various **data augmentation techniques** aimed at artificially expanding the dataset and improving model performance.

The study explores multiple augmentation strategies:
- **Easy Data Augmentation (EDA)** methods such as synonym replacement, random insertion, random deletion, and random swapping to introduce semantic and syntactic diversity.
- **Back Translation** using machine translation to generate contextual variations.
- **Paraphrasing and Text Generation** using Large Language Models (LLMs) like GPT-3.5 to create enriched and diverse sentence structures.

![Raw Sindhi Text_page-0001](https://github.com/user-attachments/assets/1f68f9a0-c894-41d5-a236-dd54295ae746)

Experiments were conducted on a Sindhi dataset containing **3364 news articles** across three categories: **sports, entertainment, and technology**. A multilingual BERT model (`bert-base-multilingual-cased`) was fine-tuned for both **binary** and **multi-class classification** tasks. Among all the methods, **Random Deletion (EDA)** achieved the highest performance, reaching a **99% F1 score** in binary classification. Back Translation and Paraphrasing also showed strong performance improvements, underlining the value of augmentation in low-resource settings.

![results ](https://github.com/user-attachments/assets/b0e2d35f-e08c-4430-ab08-ae9c32208869)

The mixing ratio α signifcantly impacts classifcation accuracy. Optimal performance occurs when α=0.5, balancing original and augmented data

![image](https://github.com/user-attachments/assets/176980b8-1135-45b7-92e2-5fe3899efb47)

The performance comparison between the baseline model and augmented models shows significant improvements. The baseline achieved 93% accuracy, while augmented methods like Random Deletion, Back Translation, and Paraphrasing reached 99%, 96%, and 94% accuracy, respectively, demonstrating their effectiveness in enhancing model performance.

| Model                         | Accuracy (%) | Precision (%) | Recall (%) | F1 Score (%) |
|-------------------------------|--------------|---------------|------------|--------------|
| Baseline (No Augmentation)     | 93           | 93.1          | 93         | 92.9         |
| Random Deletion                | 99           | 99            | 99         | 98.9         |
| Back Translation               | 96           | 96            | 96         | 96           |
| Paraphrasing                   | 94           | 94            | 94         | 94           |

This project sets a strong baseline for Sindhi NLP and demonstrates how even simple augmentation techniques can meaningfully enhance performance for underrepresented languages. It also opens doors for future research involving hybrid methods and larger datasets to further evolve Sindhi language technologies.

