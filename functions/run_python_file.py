from functions.function_helpers import get_path
from functions.function_helpers import outside_working_directory_error
from typing import List
from functions.config import TIMEOUT
import subprocess


def run_python_file(working_directory: str, file_path: str) -> str:

    path, inside_working_directory = get_path(working_directory, file_path)

    if not inside_working_directory:
        return outside_working_directory_error(file_path, 'execute')
    
    if not path.exists():
        return f'Error: File "{file_path}" not found.'
    
    if not path.suffix == '.py':
        return f'Error: "{file_path}" is not a Python file.'

    try:    
    
        completed  = subprocess.run(args=['uv', 'run', file_path], timeout=TIMEOUT, capture_output=True, text=True, cwd=working_directory)
    
    except Exception as e:

        return f"Error: executing Python file: {e}"

    if len(completed.stdout) == 0 and len(completed.stderr) == 0:
        return'No output produced.'
    
    stdrun: List[str] = []

    stdrun.append(f'STDOUT: {completed.stdout}')
    
    stdrun.append(f'STDERR: {completed.stderr}')

    if completed.returncode > 0:
       
      stdrun.append(f'Process exited with code {completed.returncode}')

    return '\n'.join(stdrun)    
