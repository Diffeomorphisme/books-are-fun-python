import logging
from pathlib import Path

def get_logger():
    logger = logging.getLogger("SBT-chatbot-logger")
    logger.setLevel(logging.INFO)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s: %(message)s", datefmt="%b-%d %H:%M:%S"
    )
    console.setFormatter(formatter)
    logger.addHandler(console)
    return logger


logger = get_logger()
BASE_DIR: Path = Path(__file__).parents[1]
