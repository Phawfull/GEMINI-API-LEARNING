import google.generativeai as genai

import os

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

generation_config = genai.GenerationConfig(
    temperature=0.2,
    max_output_tokens=100,
    top_p=0.95,
    top_k=40
)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a helpful assistant. Be concise.",
    generation_config=generation_config
)

response = model.generate_content(
    "Explain what a token is in LLMs."
)

print(response.text)

print(f"\nInput Tokens  : {response.usage_metadata.prompt_token_count}")
print(f"Output Tokens : {response.usage_metadata.candidates_token_count}")
print(f"Total Tokens  : {response.usage_metadata.total_token_count}")