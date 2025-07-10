from functions.get_path import get_path
from functions.config import MAX_NUMBER_CHARS

    

def get_file_content(working_directory : str, file_path : str):
        
    path, inside_working_directory = get_path(working_directory, file_path)

    if not inside_working_directory:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not path.exists():
        return f'Error: Cannot read "{file_path}" as it does not exist'

    if not path.is_file():
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with path.open("r") as f:
            return f.read(MAX_NUMBER_CHARS)
    except UnicodeDecodeError:
        return f'Error: Cannot read "{file_path}" as it is not a text file'

