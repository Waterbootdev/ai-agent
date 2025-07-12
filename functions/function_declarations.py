from google.genai.types import FunctionDeclaration, Schema, Type, Tool
from functions.config import MAX_NUMBER_CHARS

schema_get_files_info: FunctionDeclaration = FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "directory": Schema(
                type=Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_NUMBER_CHARS} characters of the content from a specified file within the working directory.",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "file_path": Schema(
                type=Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)

schema_run_python_file = FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "file_path": Schema(
                type=Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": Schema(
                type=Type.ARRAY,
                items=Schema(
                    type=Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)

schema_write_file = FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "file_path": Schema(
                type=Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": Schema(
                type=Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)

available_schema_functions: Tool = Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)
