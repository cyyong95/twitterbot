import constants
import json


def read_config() -> dict:
    with open(constants.config_path) as f:
        config = json.load(f)

    return config
