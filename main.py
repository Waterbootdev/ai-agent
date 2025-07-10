import os
import sys
from dotenv import load_dotenv
from google import genai 
from google.genai.types import GenerateContentResponse, Content, Part
from typing import List 

model : str = 'gemini-2.0-flash-001'

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
   
    if len(args) == 0:
        print("please provide a prompt")
        sys.exit(1)

    user_prompt : str = " ".join(args)
        
    contens : List[Content] = [Content(role="user", parts=[Part(text=user_prompt)])]
    
    response : GenerateContentResponse = client.models.generate_content(model=model, contents=contens) # type: ignore

    if verbose:
        print(f'User prompt: {user_prompt}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}') # type: ignore
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}') # type: ignore

    print(response.text)

    
if __name__ == "__main__":
    main()
