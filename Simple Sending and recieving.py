import google.generativeai as genai   #OLD importing
import os

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="You are a helpful assistant."
)

print("Example 1: Simple Send and receive.")

response = model.generate_content("What is machine learning in once sentence")
print(response.text)
print(f"  Input tokens:  {response.usage_metadata.prompt_token_count}")
print(f"  Output tokens: {response.usage_metadata.candidates_token_count}")
print(f"  Total tokens:  {response.usage_metadata.total_token_count}")