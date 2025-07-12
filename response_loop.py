from google import genai 
from google.genai.types import GenerateContentResponse, Content, GenerateContentConfig, FunctionCall
from typing import List 
from functions.call_function import call_functions
from functions.config import MAX_NUMBER_ITERATIONS


def response_function_calls_loop(verbose: bool, contens: List[Content], model: str, client: genai.Client, config: GenerateContentConfig):
    for i in range(MAX_NUMBER_ITERATIONS):
        response : GenerateContentResponse = client.models.generate_content(model=model, contents=contens, config=config) # type: ignore

        print_response_stats(verbose, i, response)

        if response.text is not None:
            print(response.text)
            break
    
        function_calls = get_function_calls_or_raise_exception(response)

        append_candidates(contens, response)

        append_function_calls(verbose, contens, function_calls)


def get_function_calls_or_raise_exception(response: GenerateContentResponse) -> List[FunctionCall]:
    if response.function_calls is None or len(response.function_calls) == 0:
        raise Exception("Error: no text and no function calls found")

    return response.function_calls
        
def append_function_calls(verbose: bool , contens: List[Content], function_calls: List[FunctionCall]):
    try:
        contens.append(Content(role="tool", parts=call_functions(verbose, function_calls)))
    except Exception as e:
        print(f"Error in generate_content: {e}")

def append_candidates(contens: List[Content], response: GenerateContentResponse):
    if response.candidates is not  None:
         for candidate in response.candidates:
            if candidate.content is not None:
                contens.append(candidate.content)

def print_response_stats(verbose: bool, index: int, response: GenerateContentResponse):
        if verbose:
            print(f'Iteration: {index + 1}')
            print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}') # type: ignore
            print(f'Response tokens: {response.usage_metadata.candidates_token_count}') # type: ignore
    
