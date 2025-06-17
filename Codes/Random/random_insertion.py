
import random
import json
from nltk.corpus import wordnet
import nltk
import os

nltk.download('wordnet')
nltk.download('omw-1.4')

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.name() != word:
                synonyms.add(lemma.name().replace("_", " "))
    return list(synonyms)

def random_insertion(sentence, insertion_prob=0.2):
    words = sentence.split()
    n = max(1, int(len(words) * insertion_prob))
    for _ in range(n):
        add_word(words)
    return " ".join(words)

def add_word(words):
    synonyms = []
    counter = 0
    while len(synonyms) < 1 and counter < 10:
        random_word = random.choice(words)
        synonyms = get_synonyms(random_word)
        counter += 1
    if synonyms:
        synonym = random.choice(synonyms)
        insert_pos = random.randint(0, len(words))
        words.insert(insert_pos, synonym)

# Example usage
if __name__ == "__main__":
    sentence = "This is a simple example to test random insertion"
    augmented = random_insertion(sentence)
    result = {
        "original": sentence,
        "augmented": augmented
    }

    # Save result
    output_path = "eda_random_insertion/result.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Original:", sentence)
    print("Augmented:", augmented)
