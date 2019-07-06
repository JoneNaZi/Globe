from common.common_fun import Common
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time
class LoginView(Common):
    # 密码登录界面元素
    et_phone = (By.ID, 'com.gogocinema.android:id/et_phone')
    et_password = (By.ID, 'com.gogocinema.android:id/et_password')
    btn_login = (By.ID, 'com.gogocinema.android:id/btn_login')
    username_view = (By.ID, 'com.gogocinema.android:id/tv_user_name')

    # 退出登录元素
    tv_setting = (By.ID, 'com.gogocinema.android:id/tv_setting')
    btn_login_out = (By.ID, 'com.gogocinema.android:id/btn_login_out')

    # 短信验证码登录界面元素
    cb_chage_login = (By.ID, 'com.gogocinema.android:id/cb_chage_login')
    et_sms_phone = (By.ID, 'com.gogocinema.android:id/et_phone')
    et_sms_password = (By.ID, 'com.gogocinema.android:id/et_password')
    btn_sms_login = (By.ID, 'com.gogocinema.android:id/btn_login')

    # toast提示
    error_message = "用户不存在"
    message = '//*[@text=\'{}\']'.format(error_message)
    toast = (By.XPATH, message)

    # 图标id
    image = (By.ID, 'com.gogocinema.android:id/imageView3')

    # 密码登录
    def login_password_action(self, phoneNum, password):
        self.skip_guide_page()
        self.go_login_view()
        logging.info('======login_password_action======')
        logging.info('phoneNum is %s' % phoneNum)
        self.driver.find_element(*self.et_phone).send_keys(phoneNum)
        time.sleep(1)
        logging.info('password is %s' % password)
        self.driver.find_element(*self.et_password).send_keys(password)

        self.driver.find_element(*self.image).click()
        self.driver.find_element(*self.btn_login).click()

    # 验证码登录
    def login_sms_action(self, phoneNum, verificationCode):
        self.skip_guide_page()
        self.go_login_view()
        self.driver.find_element(*self.cb_chage_login).click()
        logging.info('======login_sms_action======')
        logging.info('phoneNum is %s' % phoneNum)
        self.driver.find_element(*self.et_sms_phone).send_keys(phoneNum)
        logging.info('verificationCode is %s' % verificationCode)
        self.driver.find_element(*self.et_sms_password).send_keys(verificationCode)

        self.driver.find_element(*self.image).click()
        self.driver.find_element(*self.btn_sms_login).click()

    # 检测登录状态
    def check_login_status(self):
        logging.info('======check_login_status======')
        try:
            WebDriverWait(self.driver, 15, 0.5).until(lambda x: x.find_element(*self.username_view))
            self.driver.find_element(*self.username_view)
        except NoSuchElementException:
            logging.info('login fail!')
            self.get_screen_shot('login fail')
            return False
        else:
            logging.info('login success!')
            return True

    # 登录失败
    def check_login_fail_status(self):
        logging.info('======check_login_fail_status======')
        try:
            WebDriverWait(self.driver, 15, 0.5).until(lambda x: x.find_element(*self.toast))
        except NoSuchElementException:
            logging.info('没找到提示信息')
            return False
        else:
            logging.info('账号或密码错误')
            return True
