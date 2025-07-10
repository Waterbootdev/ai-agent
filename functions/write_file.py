
from functions.get_path import get_path

def write_file(working_directory : str, file_path : str, content : str):

        path, inside_working_directory = get_path(working_directory, file_path)

        if not inside_working_directory:
            return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
        
        try:
            with path.open("w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f'Error: {e}'

