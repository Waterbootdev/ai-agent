import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai.types import (
    GenerateContentResponse,
    Content,
    Part,
    GenerateContentConfig,
)
from system_prompt import (
    SYSTEM_PROMPT_FUNCTION_CALL_PLAN_WITHOUT_WORKING_DIRECTORY as SYSTEM_PROMPT,
)
from functions.function_declarations import available_schema_functions
from typing import List
from functions.call_function import call_function
from functions.config import MAX_NUMBER_ITERATIONS

model: str = "gemini-2.0-flash-001"

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if len(args) == 0:
        print("please provide a prompt")
        sys.exit(1)

    user_prompt: str = " ".join(args)

    contens: List[Content] = [Content(role="user", parts=[Part(text=user_prompt)])]

    config: GenerateContentConfig = GenerateContentConfig(
        tools=[available_schema_functions], system_instruction=SYSTEM_PROMPT
    )

    for i in range(MAX_NUMBER_ITERATIONS):
        response: GenerateContentResponse = client.models.generate_content(
            model=model, contents=contens, config=config
        )  # type: ignore

        if verbose:
            print(f"User prompt(iteration {i}): {user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")  # type: ignore
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")  # type: ignore

        if response.text is not None:
            print(response.text)
            break

        if response.candidates is not None:
            for candidate in response.candidates:
                if candidate.content is not None:
                    contens.append(candidate.content)
        try:
            if response.function_calls is None or len(response.function_calls) == 0:
                raise Exception()
            else:
                function_responses: List[Part] = []

                for function_call_part in response.function_calls:
                    content = call_function(function_call_part, verbose)

                    assert content is not None
                    assert content.parts is not None

                    part = content.parts[0]

                    if (
                        part.function_response is None
                        or part.function_response.response is None
                    ):
                        raise Exception()

                    if verbose:
                        for key, value in part.function_response.response.items():
                            print(f"-> {key} : {value}")

                    function_responses.append(part)

                contens.append(Content(role="tool", parts=function_responses))

        except Exception as e:
            print(f"Error in generate_content: {e}")


if __name__ == "__main__":
    main()
