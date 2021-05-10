from AbstractTestClass import *

import time
import os
import os.path

class TestCase1(AbstractTestClass):

    def prep(self):
        logger.debug("Preparation stage")
        if round(time.time()) % 2 != 0:
            logger.warning("System time is not even. Test case aborted.")
            sys.exit(0)
        logger.debug("Preparation stage finished successfully")

    def run(self):
        logger.debug("Run stage")
        homeDir = os.path.expanduser("~")
        print(os.listdir(path=homeDir))
        logger.debug("Run stage finished successfully")

    def clean_up(self):
        logger.debug("Clean up stage")
        logger.debug("Nothing to do")
        logger.debug("Clean up stage finished successfully")