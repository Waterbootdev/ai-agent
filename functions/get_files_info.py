from pathlib import Path
from functions.function_helpers import get_path
from functions.function_helpers import outside_working_directory_error
import os

def get_file_info(path: Path, name: str) -> str:
    return f'- {name}: file_size={path.stat().st_size} bytes, is_dir={path.is_dir()}'

def get_files_info(working_directory:str, directory: str|None=None) -> str:

    if directory is None:
        return f'Error: "{directory}" is not a directory'
    
    path, inside_working_directory = get_path(working_directory, directory)

    if (not inside_working_directory or not path.exists())   :
        return outside_working_directory_error(directory, 'list')
    
    if not path.is_dir():
        return f'Error: "{directory}" is not a directory'
        
    return '\n'.join(get_file_info(path.joinpath(name), name) for name in os.listdir(path.absolute())) 


    
    
    