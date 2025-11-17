import logging
import os
from typing import List, Dict, Tuple

logger = logging.getLogger(__name__)

def get_config() -> Dict[str, str]:
    try:
        config_path = os.environ.get('CONFIG_PATH', 'config.json')
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        logger.error(f"Config file '{config_path}' not found.")
        return {}
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing config file: {e}")
        return {}

def load_env() -> Dict[str, str]:
    env_vars = {}
    for key, value in os.environ.items():
        env_vars[key] = value
    return env_vars

def get_absolute_path(path: str) -> str:
    return os.path.abspath(os.path.expanduser(path))

def get_env_or_config(key: str, default: str = '') -> str:
    env_value = os.environ.get(key, default)
    if env_value:
        return env_value
    config_value = get_config().get(key, default)
    if config_value:
        return config_value
    return default

def get_list_from_env_or_config(key: str, default: List[str] = []) -> List[str]:
    env_value = os.environ.get(key)
    if env_value:
        return env_value.split(',')
    config_value = get_config().get(key, default)
    if config_value:
        return config_value.split(',')
    return default

def get_dict_from_env_or_config(key: str, default: Dict[str, str] = {}) -> Dict[str, str]:
    env_value = os.environ.get(key)
    if env_value:
        return dict(pair.split('=') for pair in env_value.split(','))
    config_value = get_config().get(key, default)
    if config_value:
        return config_value
    return default

def get_int_from_env_or_config(key: str, default: int = 0) -> int:
    env_value = os.environ.get(key)
    if env_value:
        return int(env_value)
    config_value = get_config().get(key, default)
    if config_value:
        return int(config_value)
    return default

def get_bool_from_env_or_config(key: str, default: bool = False) -> bool:
    env_value = os.environ.get(key)
    if env_value:
        return env_value.lower() == 'true'
    config_value = get_config().get(key, default)
    if config_value:
        return config_value.lower() == 'true'
    return default

def get_float_from_env_or_config(key: str, default: float = 0.0) -> float:
    env_value = os.environ.get(key)
    if env_value:
        return float(env_value)
    config_value = get_config().get(key, default)
    if config_value:
        return float(config_value)
    return default