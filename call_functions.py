from functions.call_function import call_function, FunctionCall, Part
from typing import List

def call_functions(verbose: bool, function_calls: List[FunctionCall]) -> List[Part] :
    
    function_responses : List[Part] = []

    for function_call_part in function_calls:
        content = call_function(function_call_part, verbose)

        assert content is not None
        assert content.parts is not None

        part = content.parts[0]

        if part.function_response is None or part.function_response.response is None:
            raise Exception()

        if verbose:
            for key, value in part.function_response.response.items(): 
                print(f"-> {key} : {value}")
                            
        function_responses.append(part)
    
    return function_responses