
import random
import json
import os

def random_swap(sentence, swap_prob=0.2):
    words = sentence.split()
    n = max(1, int(len(words) * swap_prob))
    for _ in range(n):
        words = swap_word(words)
    return " ".join(words)

def swap_word(words):
    idx1 = random.randint(0, len(words)-1)
    idx2 = idx1
    while idx2 == idx1:
        idx2 = random.randint(0, len(words)-1)
    words[idx1], words[idx2] = words[idx2], words[idx1]
    return words

# Example usage
if __name__ == "__main__":
    sentence = "This is a simple example to test random swap"
    augmented = random_swap(sentence)
    result = {
        "original": sentence,
        "augmented": augmented
    }

    # Save result
    output_path = "eda_random_swap/result.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Original:", sentence)
    print("Augmented:", augmented)
