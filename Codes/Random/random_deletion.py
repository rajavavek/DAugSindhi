
import random
import json
import os

def random_deletion(sentence, deletion_prob=0.2):
    words = sentence.split()
    if len(words) == 1:
        return sentence
    new_words = [word for word in words if random.random() > deletion_prob]
    if len(new_words) == 0:
        return random.choice(words)
    return " ".join(new_words)

# Example usage
if __name__ == "__main__":
    sentence = "This is a simple example to test random deletion"
    augmented = random_deletion(sentence)
    result = {
        "original": sentence,
        "augmented": augmented
    }

    # Save result
    output_path = "eda_random_deletion/result.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Original:", sentence)
    print("Augmented:", augmented)
