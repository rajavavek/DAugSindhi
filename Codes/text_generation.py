
import openai
import os
import json

# Ensure your OpenAI API key is set in the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_sentences(base_sentence, n_variants=3):
    prompt = f"Generate {n_variants} Sindhi sentences similar in meaning to the following:

"{base_sentence}""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            n=1
        )
        return response['choices'][0]['message']['content'].strip().split('\n')
    except Exception as e:
        return [f"Error: {str(e)}"]

# Example usage
if __name__ == "__main__":
    sentence = "تون سڀاڻي اسڪول ويندو؟"  # Example Sindhi sentence
    generated = generate_sentences(sentence)
    result = {
        "original": sentence,
        "generated": generated
    }

    # Save result
    output_path = "text_generation/result.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Original:", sentence)
    print("Generated Sentences:", generated)
