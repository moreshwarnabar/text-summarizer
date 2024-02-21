import os
import yaml

from text_summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return a ConfigBox object.

    Parameters
    ----------
    path_to_yaml : Path
        Path to the YAML file.

    Returns
    -------
    ConfigBox
        A ConfigBox object.

    Raises
    ------
    BoxValueError
        If the YAML file cannot be read.
    """
    with open(path_to_yaml) as f:
        try:
            content = yaml.safe_load(f)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        except yaml.YAMLError as e:
            raise BoxValueError(e) from e
        

@ensure_annotations
def create_directories(path_to_dir: list, verbose=True):
    """
    Create a list of directories.

    Parameters
    ----------
    path_to_dir : list
        List of directories to be created.
    verbose : bool, optional
        Whether to print a message. The default is True.

    Returns
    -------
    None.

    Raises
    ------
    FileExistsError
        If a directory already exists.
    """
    for path in path_to_dir:
        if os.path.exists(path):
            if verbose:
                logger.info(f'Directory already exists: {path}')
        else:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f'Creating directory: {path}')


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file.

    Parameters
    ----------
    path : Path
        Path to the file.

    Returns
    -------
    str
        The size of the file.
    """
    size = round(os.path.getsize(path) / 1024)
    return f'~{size} KB'