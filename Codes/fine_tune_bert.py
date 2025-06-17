
import os
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from datasets import Dataset
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from transformers import DataCollatorWithPadding
import torch

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def preprocess(df, tokenizer, label_column):
    dataset = Dataset.from_pandas(df)
    dataset = dataset.map(lambda e: tokenizer(e['text'], truncation=True, padding='max_length', max_length=128), batched=True)
    dataset = dataset.rename_column(label_column, "labels")
    dataset.set_format(type='torch', columns=['input_ids', 'attention_mask', 'labels'])
    return dataset

def fine_tune_bert(train_df, val_df, num_labels, output_dir, label_column='label'):
    tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
    train_dataset = preprocess(train_df, tokenizer, label_column)
    val_dataset = preprocess(val_df, tokenizer, label_column)

    model = BertForSequenceClassification.from_pretrained('bert-base-multilingual-cased', num_labels=num_labels)

    training_args = TrainingArguments(
        output_dir=output_dir,
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=10,
        weight_decay=0.01,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        logging_dir=f"{output_dir}/logs",
        load_best_model_at_end=True,
        metric_for_best_model="f1",
        save_total_limit=2
    )

    def compute_metrics(eval_pred):
        from sklearn.metrics import accuracy_score, precision_recall_fscore_support
        logits, labels = eval_pred
        predictions = torch.argmax(torch.tensor(logits), dim=-1)
        precision, recall, f1, _ = precision_recall_fscore_support(labels, predictions, average='weighted')
        acc = accuracy_score(labels, predictions)
        return {"accuracy": acc, "f1": f1, "precision": precision, "recall": recall}

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        tokenizer=tokenizer,
        data_collator=DataCollatorWithPadding(tokenizer),
        compute_metrics=compute_metrics
    )

    trainer.train()
    trainer.save_model(output_dir)

# Example usage
if __name__ == "__main__":
    # Example assumes you have a CSV file with 'text' and 'label' columns
    df = pd.DataFrame({
        "text": [
            "ڪرڪيٽ جو مقابلو دلچسپ هو", 
            "نئون ٽيڪنالاجي آرٽيڪل شايع ٿيو", 
            "فلم جو جائزو سٺو هو"
        ],
        "label": [0, 1, 2]  # 0 = Sports, 1 = Technology, 2 = Entertainment
    })

    train_df, val_df = train_test_split(df, test_size=0.2, stratify=df['label'])
    fine_tune_bert(train_df, val_df, num_labels=3, output_dir="fine_tuning/bert_multiclass")
