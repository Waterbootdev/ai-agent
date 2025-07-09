import os
from dotenv import load_dotenv
from google import genai 
from google.genai.types import GenerateContentResponse
  

model : str = 'gemini-2.0-flash-001'

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    contens : str ='''Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'''
    response : GenerateContentResponse = client.models.generate_content(model=model, contents=contens) # type: ignore
    print(response.text)

    print(f'Promt tokens: {response.usage_metadata.prompt_token_count}') # type: ignore
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}') # type: ignore

    
if __name__ == "__main__":
    main()
