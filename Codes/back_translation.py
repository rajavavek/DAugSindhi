
import json
import os
from googletrans import Translator

def back_translate(text, src='sd', intermediate='en'):
    translator = Translator()
    try:
        translated = translator.translate(text, src=src, dest=intermediate).text
        back_translated = translator.translate(translated, src=intermediate, dest=src).text
        return back_translated
    except Exception as e:
        return f"Translation failed: {e}"

# Example usage
if __name__ == "__main__":
    sentence = "تون سڀاڻي اسڪول ويندو؟"  # Example Sindhi sentence
    augmented = back_translate(sentence)
    result = {
        "original": sentence,
        "back_translated": augmented
    }

    # Save result
    output_path = "back_translation/result.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Original:", sentence)
    print("Back Translated:", augmented)
