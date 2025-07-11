from functions.write_file import write_file
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from typing import Dict, Any

available_functions :  Dict[str, Any] = {"write_file": write_file, "get_files_info": get_files_info, "get_file_content": get_file_content, "run_python_file": run_python_file}
