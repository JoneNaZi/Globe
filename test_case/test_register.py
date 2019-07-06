from businessview.register_view import RegisterView
from businessview.login_view import LoginView
from common.myunit import StartEnd
import logging
import unittest
import random

class RegisterTest(StartEnd):
    phone_number = '1' + str(random.randint(1000000000, 9999999999))
    verificationCode = str(random.randint(1000, 9999))
    password = 'a' + str(random.randint(1000000, 9999999))

    def test_register(self):
        logging.info('======test_register======')
        r = RegisterView(self.driver)
        l = LoginView(self.driver)

        r.register_action(self.phone_number, self.verificationCode, self.password)
        self.assertTrue(l.check_login_status())
