import google.generativeai as genai

API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=API_KEY)

generation_config = genai.GenerationConfig(
    temperature=0.2,
    max_output_tokens=150
)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a helpful assistant. Keep answers short.",
    generation_config=generation_config
)

try:
    prompt = input("Enter your prompt: ")

    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    if len(prompt) > 500:
        raise ValueError("Prompt is too long.")

    response = model.generate_content(prompt)

    print("\nResponse:\n")
    print(response.text)

    usage = response.usage_metadata

    print("\nToken Usage")
    print("Prompt Tokens :", usage.prompt_token_count)
    print("Output Tokens :", usage.candidates_token_count)
    print("Total Tokens  :", usage.total_token_count)

except ValueError as e:
    print("Input Error:", e)

except Exception as e:
    print("API Error:", e)