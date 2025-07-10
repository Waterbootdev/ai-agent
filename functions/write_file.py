
from functions.function_helpers import get_path
from functions.function_helpers import outside_working_directory_error

def write_file(working_directory : str, file_path : str, content : str):

        path, inside_working_directory = get_path(working_directory, file_path)

        if not inside_working_directory:
            return outside_working_directory_error(file_path, 'write')
        
        try:
            with path.open("w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f'Error: {e}'

