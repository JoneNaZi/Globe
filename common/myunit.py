import unittest
from common.appium_desired import appium_desired
import logging
import time

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('======setUp======')
        self.driver = appium_desired()

    def tearDown(self):
        logging.info('======tearDown======')
        time.sleep(5)
        self.driver.close_app()