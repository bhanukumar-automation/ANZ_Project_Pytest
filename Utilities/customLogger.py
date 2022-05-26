import logging


class LogGenerator:

    @staticmethod
    def log_gen():
        log_filename = "..\\Logs\\automation.log"
        logging.basicConfig(filename= log_filename,
                            filemode='w',
                            format= '%(asctime)s::%(levelname)s::%(message)s',
                            datefmt='%d-%m-%y %H:%M:%S',
                            level= logging.INFO,
                            force= True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

