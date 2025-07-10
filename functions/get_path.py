
from pathlib import Path

def get_path(working_directory : str, other : str):
    working_directory_path : Path = Path(working_directory).absolute()

    path : Path = working_directory_path.joinpath(other).resolve()

    inside_working_directory = str(path).startswith(str(working_directory_path))
    
    return path,inside_working_directory
    

