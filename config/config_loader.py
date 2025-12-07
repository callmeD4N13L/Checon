import json
from core.logger import exception_log as log
def config_process(JSONFILE):
    try:
        with open(JSONFILE, "r", encoding="utf-8") as f:
            config = json.load(f)
            return config
    except FileNotFoundError as e:
        log(e)