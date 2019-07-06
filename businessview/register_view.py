from common.common_fun import Common
import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class RegisterView(Common):
    # 注册界面入口按钮元素
    btn_login = (By.ID, 'com.gogocinema.android:id/btn_login')
    # tv_repassword = (By.ID, 'com.gogocinema.android:id/tv_repassword')
    btn_register_login = (By.ID, 'com.gogocinema.android:id/btn_register')

    # 注册界面元素
    et_phone = (By.ID, 'com.gogocinema.android:id/et_phone')
    et_code = (By.ID, 'com.gogocinema.android:id/et_code')
    et_password = (By.ID, 'com.gogocinema.android:id/et_password')
    btn_register = (By.ID, 'com.gogocinema.android:id/btn_register')

    # 图标id
    image = (By.ID, 'com.gogocinema.android:id/imageView3')

    def register_action(self, phoneNum, verificationCode, password):
        self.skip_guide_page()
        self.go_login_view()
        logging.info('======register_action======')
        self.driver.find_element(*self.btn_register_login).click()
        logging.info('phoneNum is %s' % phoneNum)
        self.driver.find_element(*self.et_phone).send_keys(phoneNum)
        logging.info('verificationCode is %s' % verificationCode)
        self.driver.find_element(*self.et_code).send_keys(verificationCode)
        logging.info('password is %s' % password)
        self.driver.find_element(*self.et_password).send_keys(password)

        self.driver.find_element(*self.image).click()
        self.driver.find_element(*self.btn_register).click()
