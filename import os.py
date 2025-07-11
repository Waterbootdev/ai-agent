import os
import sys
from dotenv import load_dotenv
from google import genai 
from google.genai.types import GenerateContentResponse, Content, Part, GenerateContentConfig
from system_prompt import SYSTEM_PROMPT_FUNCTION_CALL_PLAN_WITHOUT_WORKING_DIRECTORY as SYSTEM_PROMPT
from functions.function_declarations import available_schema_functions
from typing import List 
from functions.call_function import call_function

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
    
    config: GenerateContentConfig = GenerateContentConfig(tools=[available_schema_functions], system_instruction=SYSTEM_PROMPT)

    response : GenerateContentResponse = client.models.generate_content(model=model, contents=contens, config=config) # type: ignore

    if verbose:
        print(f'User prompt: {user_prompt}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}') # type: ignore
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}') # type: ignore


    if response.candidates is not  None:
         for candidate in response.candidates:

            if candidate.content is not None:
                contens.append(candidate.content)
    

    if response.function_calls is not None:
        for function_call_part in response.function_calls:
            content = call_function(function_call_part, verbose)

            assert content is not None
            assert content.parts is not None

            if content.parts[0].function_response is None:
                raise Exception()
            
            if verbose:
                print(f"-> {content.parts[0].function_response.response}")
            
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")

    print(response.text)

    
if __name__ == "__main__":
    main()
