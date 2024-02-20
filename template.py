import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'text-summarizer'

list_of_files = [
    '.github/workflows/.gitkeep',  # CI/CD
    f'src/{project_name}/__init__.py',  # required for local installation
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging//__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',  # model related parameters
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',  # experimentation in notebooks
]

for file_path in list_of_files:
    # convert file path to the local system structure
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f'Creating directory: {file_dir} for file: {file_name}')

    # file does not exist or is empty
    if (not os.path.exists(file_path)) or os.path.getsize(file_path) == 0:
        with open(file_path, 'w') as f:
            # pass as only want to create the file
            pass
            logging.info(f'Creating an empty file: {file_name}')
    else:
        logging.info(f'{file_name} already exists')