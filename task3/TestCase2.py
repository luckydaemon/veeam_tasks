from AbstractTestClass import *

import psutil
import os
import os.path

class TestCase2(AbstractTestClass):

    def prep(self):
        logger.debug("Preparation stage")
        if psutil.virtual_memory().total < 1073741824:
            logger.warning("Not enough memory. Test case aborted.")
            sys.exit(0)
        logger.debug("Preparation stage finished successfully")

    def run(self):
        logger.debug("Run stage")
        with open("test.txt", 'wb') as fout:
            fout.write(os.urandom(1024))
        logger.debug("Run stage finished successfully")

    def clean_up(self):
        logger.debug("Clean up stage")
        os.remove("test.txt")
        logger.debug("Clean up stage finished successfully")