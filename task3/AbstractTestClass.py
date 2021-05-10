import abc
import logging
import sys


def get_logger():
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s] %(filename)s:%(lineno)d %(levelname)-8s %(message)s')
    fileHandler = logging.FileHandler("log.txt", encoding="utf-8")
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger

logger = get_logger()

class AbstractTestClass(abc.ABC):



    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name

    @abc.abstractmethod
    def prep(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def clean_up(self):
        pass

    def execute(self):
        logger.info("Started test-case : id " + str(self.tc_id) + " name: " + self.name)
        try:
            self.prep()
        except Exception as e:
            logger.error("Error on preparation stage")
            logger.error(e)
            sys.exit()
        try:
            self.run()
        except Exception as e:
            logger.error("Error on run stage")
            logger.error(e)
            sys.exit()
        try:
            self.clean_up()
        except Exception as e:
            logger.error("Error on clean up stage")
            logger.error(e)
            sys.exit()
        logger.info("Finished test-case: id " + str(self.tc_id) + " name: " + self.name)