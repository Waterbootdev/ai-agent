from pathlib import Path
import os

def get_file_info(path: Path, name: str) -> str:
    return f'- {name}: file_size={path.stat().st_size} bytes, is_dir={path.is_dir()}'

def get_files_info(working_directory:str, directory: str|None=None) -> str:

    if directory is None:
        return f'Error: "{directory}" is not a directory'
    
    working_directory_path : Path = Path(working_directory).absolute()

    path : Path = working_directory_path.joinpath(directory).resolve()

    inside_working_directory = str(path).startswith(str(working_directory_path))

    if (not inside_working_directory or not path.exists())   :
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not path.is_dir():
        return f'Error: "{directory}" is not a directory'
        
    return '\n'.join(get_file_info(path.joinpath(name), name) for name in os.listdir(path.absolute())) 


    
    
    