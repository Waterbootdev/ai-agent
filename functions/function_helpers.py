
from pathlib import Path
from typing import Tuple

def get_path(working_directory : str, other : str) -> Tuple[Path, bool]:
    working_directory_path : Path = Path(working_directory).absolute()

    path : Path = working_directory_path.joinpath(other).resolve()

    inside_working_directory = str(path).startswith(str(working_directory_path))
    
    return path,inside_working_directory
    

def outside_working_directory_error(path: str, action: str) -> str:
    return f'Error: Cannot {action} "{path}" as it is outside the permitted working directory'
