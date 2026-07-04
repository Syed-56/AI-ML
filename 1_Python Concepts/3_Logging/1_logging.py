import logging

#Log Levels
logging.debug("Detailed diagnostic info")      # 10 - dev-time only
logging.info("Confirmation things are working")   # 20 - normal operation
logging.warning("Something unexpected, not fatal")  # 30 - default level if unconfigured
logging.error("A function failed to execute")        # 40 - real problem
logging.critical("Program may not be able to continue")  # 50 - severe

#Basic Config
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='app.log',
    filemode='w'   # 'w' overwrites each run, 'a' (default) appends
)

#Exception and Rotation
try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Division failed")   # logs the message + full traceback automatically
    
from logging.handlers import RotatingFileHandler
handler = RotatingFileHandler('app.log', maxBytes=5*1024*1024, backupCount=3)
# rotates to app.log.1, app.log.2... once app.log hits 5MB, keeps 3 backups