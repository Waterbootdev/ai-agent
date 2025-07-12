import os
import sys
from google import genai 
from google.genai.types import Content, Part, GenerateContentConfig
from system_prompt import SYSTEM_PROMPT_FUNCTION_CALL_PLAN_WITHOUT_WORKING_DIRECTORY as SYSTEM_PROMPT
from functions.function_declarations import available_schema_functions
from typing import List 

def initialze():

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
   
    if len(args) == 0:
        print("please provide a prompt")
        sys.exit(1)

    user_prompt : str = " ".join(args)
    contens : List[Content] = [Content(role="user", parts=[Part(text=user_prompt)])]
    model : str = 'gemini-2.0-flash-001'   
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    config: GenerateContentConfig = GenerateContentConfig(tools=[available_schema_functions], system_instruction=SYSTEM_PROMPT)
    
    return verbose, user_prompt, contens, model, client, config
