
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

def synonym_replacement(sentence, replacement_prob=0.3):
    words = sentence.split()
    new_words = words.copy()
    n = max(1, int(len(words) * replacement_prob))
    random_word_list = list(set([word for word in words if get_synonyms(word)]))
    random.shuffle(random_word_list)
    num_replaced = 0
    for word in random_word_list:
        synonyms = get_synonyms(word)
        if synonyms:
            synonym = random.choice(synonyms)
            new_words = [synonym if w == word else w for w in new_words]
            num_replaced += 1
        if num_replaced >= n:
            break
    return " ".join(new_words)

# Example usage
if __name__ == "__main__":
    # Example sentence (replace with Sindhi sentence if working with a proper Sindhi WordNet)
    sentence = "This is a simple example to test synonym replacement"
    augmented = synonym_replacement(sentence)
    result = {
        "original": sentence,
        "augmented": augmented
    }

    # Save result
    output_path = "eda_synonym_replacement/result.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Original:", sentence)
    print("Augmented:", augmented)
