# logger.py
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log'
)

logger = logging.getLogger(__name__)

# test.py
from logger import logger

def add(a, b):
    logger.debug(f"Adding {a} and {b}")
    return a + b

logger.debug("Addition function called")
result = add(10, 15)