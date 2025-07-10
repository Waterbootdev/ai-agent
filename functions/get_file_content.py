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
            content = f.read(MAX_NUMBER_CHARS)
        if path.stat().st_size > MAX_NUMBER_CHARS:
            content += f'[...File "{file_path}" truncated at {MAX_NUMBER_CHARS} characters]'
        return content
    
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'

