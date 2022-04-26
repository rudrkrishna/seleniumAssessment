import inspect
import logging



class customLogger():

    def customLogger(loglevel=logging.DEBUG):

        # 1.) This is used to get the  class / method name from where this customLogger method is called
        logName = inspect.stack()[1][3]
        logger = logging.getLogger(logName)

        # 3.) Set the Log level
        logger.setLevel(logging.DEBUG)

        # 4.) Create the fileHandler to save the logs in the file
        fileHandler = logging.FileHandler("run.html", mode='a')

        # 5.) Set the logLevel for fileHandler
        fileHandler.setLevel(logging.DEBUG)

        # 6.) Create the formatter in which format do you like to save the logs
        formatter = logging.Formatter('%(name)s: %(asctime)s : %(levelname)s : %(message)s',
                                      datefmt='%d/%m/%y %I:%M:%S %p ')

        # 7.) Set the formatter to fileHandler
        fileHandler.setFormatter(formatter)

        # 8.) Add file handler to logging
        logger.addHandler(fileHandler)
        #  9.) Finally return the logging object
        return logger


