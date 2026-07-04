import logging

# Basic config — sets format/date for ALL loggers using default settings
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S"
)

# Logger for module 1
logger1 = logging.getLogger("module1")
logger1.setLevel(logging.DEBUG)     # must be capital DEBUG, not lowercase "debug"

# Logger for module 2
logger2 = logging.getLogger("module2")
logger2.setLevel(logging.WARNING)   # capital WARNING, not "warnings"

# Usage
logger1.debug("This is a debug message for module 1")
logger2.warning("This is a warning message for module 2")
logger2.error("This is an error message for module 2")