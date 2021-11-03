import inspect
import logging
import os
from datetime import datetime



def customlogger(loglevel=logging.DEBUG):
    # This method is for logging message in test steps
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.DEBUG)


    log_file = datetime.now().strftime('_%Y_%m_%d-%H_%M.txt')
    fileHandler = logging.FileHandler(log_file, mode='a')
    fileHandler.setLevel(loglevel)
    formatter = logging.Formatter('%(asctime)s -%(name)s -%(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
