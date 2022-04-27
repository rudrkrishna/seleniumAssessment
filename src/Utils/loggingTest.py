import inspect
import logging
import os


class customlogs:

    def customLogger(loglevel=logging.DEBUG):

        logName = inspect.stack()[1][3]
        logger = logging.getLogger(logName)

        # 3.) Set the Log level
        logger.setLevel(logging.DEBUG)

        # 4.) fileHandler to save the logs in the file
        fileHandler = logging.FileHandler("run.log", mode='a')

        # 5.) Setting the logLevel for fileHandler
        fileHandler.setLevel(logging.DEBUG)

        # 6.) formatter format to save the logs
        formatter = logging.Formatter('%(name)s: %(asctime)s : %(levelname)s : %(message)s',
                                      datefmt='%d/%m/%y %I:%M:%S %p ')

        # 7.) Set the formatter to fileHandler
        fileHandler.setFormatter(formatter)

        # 8.) Adding file handler to logging
        logger.addHandler(fileHandler)
        #  9.) return the logging object
        return logger
