import logging

# Basic config with handlers (writes to file + can stream)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

# Create logger for this module
logger = logging.getLogger("arithmetic_app")

def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error occurred", exc_info=True)
        return None

add(10, 15)
subtract(15, 10)
multiply(10, 20)
divide(20, 10)
divide(20, 0)   # triggers the error log