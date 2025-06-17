# DAugSindhi: A Data Augmentation Approach for Enhancing Sindhi Language Text Classifcation



## Project Overview

**Sindhi**, a low-resource language spoken by millions, faces significant challenges in Natural Language Processing (NLP) due to the scarcity of annotated datasets. This project, titled **DAugSindhi**, addresses these challenges by enhancing Sindhi text classification through various **data augmentation techniques** aimed at artificially expanding the dataset and improving model performance.

The study explores multiple augmentation strategies:
- **Easy Data Augmentation (EDA)** methods such as synonym replacement, random insertion, random deletion, and random swapping to introduce semantic and syntactic diversity.
- **Back Translation** using machine translation to generate contextual variations.
- **Paraphrasing and Text Generation** using Large Language Models (LLMs) like GPT-3.5 to create enriched and diverse sentence structures.

Experiments were conducted on a Sindhi dataset containing **3364 news articles** across three categories: **sports, entertainment, and technology**. A multilingual BERT model (`bert-base-multilingual-cased`) was fine-tuned for both **binary** and **multi-class classification** tasks. Among all the methods, **Random Deletion (EDA)** achieved the highest performance, reaching a **99% F1 score** in binary classification. Back Translation and Paraphrasing also showed strong performance improvements, underlining the value of augmentation in low-resource settings.

This project sets a strong baseline for Sindhi NLP and demonstrates how even simple augmentation techniques can meaningfully enhance performance for underrepresented languages. It also opens doors for future research involving hybrid methods and larger datasets to further evolve Sindhi language technologies.

