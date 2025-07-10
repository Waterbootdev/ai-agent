from pathlib import Path
from functions.config import MAX_NUMBER_CHARS

    

def get_file_content(working_directory : str, file_path : str):
        
    working_directory_path : Path = Path(working_directory).absolute()

    path : Path = working_directory_path.joinpath(file_path).resolve()

    inside_working_directory = str(path).startswith(str(working_directory_path))

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
    

