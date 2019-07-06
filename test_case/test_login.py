from businessview.login_view import LoginView
from common.myunit import StartEnd
import logging
import unittest


class LoginTest(StartEnd):
    csv_file = '../data/account.csv'

    # def test_01(self):
    #     logging.info('======test_01======')
    #     l = LoginView(self.driver)
    #     data = l.get_csv_data(self.csv_file, 1)
    #
    #     l.login_password_action(data[0], data[1])
    #     self.assertTrue(l.check_login_status())
    #
    # def test_02(self):
    #     logging.info('======test_02======')
    #     l = LoginView(self.driver)
    #     data = l.get_csv_data(self.csv_file, 2)
    #
    #     l.login_sms_action(data[0], data[1])
    #     self.assertTrue(l.check_login_status())
    def test_01(self):
        logging.info('======test_01======')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 3)
        l.login_password_action(data[0], data[1])
        self.assertTrue(l.check_login_fail_status())


if __name__ == '__main__':
    unittest.main()