import yaml
from ..exceptions import PlaybookEngineException

def load_yaml(file_path):
    """
    Load a YAML file and return its contents as a Python object.

    Args:
    file_path (str): Path to the YAML file.

    Returns:
    dict: The contents of the YAML file as a Python dictionary.

    Raises:
    PlaybookEngineException: If there's an error reading or parsing the YAML file.
    """
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as e:
        raise PlaybookEngineException(f"Error parsing YAML file: {e}")
    except IOError as e:
        raise PlaybookEngineException(f"Error reading YAML file: {e}")

def dump_yaml(data, file_path):
    """
    Dump a Python object to a YAML file.

    Args:
    data (dict): The Python object to be dumped to YAML.
    file_path (str): Path where the YAML file should be written.

    Raises:
    PlaybookEngineException: If there's an error writing the YAML file.
    """
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
    except yaml.YAMLError as e:
        raise PlaybookEngineException(f"Error dumping to YAML: {e}")
    except IOError as e:
        raise PlaybookEngineException(f"Error writing YAML file: {e}")
