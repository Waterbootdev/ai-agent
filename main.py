from initialize import initialze
from response_loop import response_function_calls_loop


def main():
    verbose, user_prompt, contens, model, client, config = initialze()

    print(f"User prompt: {user_prompt}")

    response_function_calls_loop(verbose, contens, model, client, config)


if __name__ == "__main__":
    main()
