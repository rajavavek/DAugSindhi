
import openai
import os
import json

# Ensure your OpenAI API key is set in the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

def paraphrase_sentence(sentence, n_variants=3):
    prompt = f"Rephrase the following Sindhi sentence while maintaining its original meaning:

"{sentence}""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            n=n_variants
        )
        variants = [choice['message']['content'].strip() for choice in response.choices]
        return variants
    except Exception as e:
        return [f"Error: {str(e)}"]

# Example usage
if __name__ == "__main__":
    sentence = "تون سڀاڻي اسڪول ويندو؟"  # Example Sindhi sentence
    paraphrased = paraphrase_sentence(sentence)
    result = {
        "original": sentence,
        "paraphrased": paraphrased
    }

    # Save result
    output_path = "paraphrasing/result.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Original:", sentence)
    print("Paraphrased Variants:", paraphrased)
