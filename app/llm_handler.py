from transformers import pipeline

# Increased max_new_tokens to allow for more comprehensive resume generation
generator = pipeline("text-generation", model="tiiuae/falcon-rw-1b", max_new_tokens=1000) # Increased from 300

def query_llm(prompt: str) -> str:
    # The pipeline returns a list of dictionaries, we want the 'generated_text' from the first element.
    # We also slice the result to remove the prompt itself from the generated text,
    # as the model might repeat it.
    result = generator(prompt)[0]["generated_text"]
    # Find the start of the expected output (e.g., "1. Name + Contact Info")
    # This helps to remove any conversational preamble the LLM might add.
    start_index = result.find("1. Name + Contact Info")
    if start_index != -1:
        return result[start_index:].strip()
    return result.strip()