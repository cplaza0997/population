"""
This module is intended to manage all interactions with any kind of files.
"""

import yaml


def read_yml(path):
    """
    Reads an YAML file and returns a dict object.

    Args:
        path (str): Path of the file

    Returns:
        dict: Content of the YAML file.
    """
    
    try:
        with open(path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except:
        return {}


