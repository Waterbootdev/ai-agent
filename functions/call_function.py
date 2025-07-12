from google.genai.types import FunctionCall, Content, Part
from functions.config import WORKING_DIRECTORY
from functions.function_calls import available_functions


def call_function(function_call_part: FunctionCall, verbose: bool = False) -> Content:
    print_calling_function(function_call_part, verbose)
    return get_response_for_function_call(function_call_part)


def get_response_for_function_call(function_call_part: FunctionCall):
    function_name = function_call_part.name
    function_args = function_call_part.args

    assert function_name is not None

    if function_name not in available_functions:
        return Content(
            role="tool",
            parts=[
                Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    assert function_args is not None

    function_args["working_directory"] = WORKING_DIRECTORY

    function_result: str = available_functions[function_name](**function_args)

    return Content(
        role="tool",
        parts=[
            Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )


def print_calling_function(function_call_part: FunctionCall, verbose: bool):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
