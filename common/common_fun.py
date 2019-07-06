from base.baseView import BaseView
import logging
import time
import os
import csv
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

class Common(BaseView):
    # tv_go_to = (By.ID, 'com.gogocinema.android:id/tv_go_to')
    tv_go_to = (By.XPATH, '//android.widget.TextView')

    rb_four = (By.ID, 'com.gogocinema.android:id/rb_four')
    tv_user_name = (By.ID, 'com.gogocinema.android:id/tv_user_name')

    # 跳过引导页
    def skip_guide_page(self):
        logging.info('======skip_guide_page======')
        try:
            skip_Btn = WebDriverWait(self.driver, 15).until(lambda x: x.find_element(*self.tv_go_to))
        except NoSuchElementException:
            logging.info('no skip_Btn')
        else:
            skip_Btn.click()

    # 跳转到我的模块
    def go_login_view(self):
        logging.info("======go_login_view======")
        try:
            WebDriverWait(self.driver, 15, 0.5).until(lambda x: x.find_element(*self.rb_four))
            myself_Btn = self.driver.find_element(*self.rb_four)
        except NoSuchElementException:
            logging.info('no myself_Btn')
        else:
            myself_Btn.click()

        self.driver.find_element(*self.tv_user_name).click()

    # 获取当前时间
    def get_Time(self):
        now = time.strftime('%Y-%m-%d %H_%M_%S')
        return now

    # 获取截图
    def get_screen_shot(self, module):
        time = self.get_Time()
        file_image = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)
        logging.info('get %s shot' % module)
        self.driver.get_screenshot_as_file(file_image)

    # 拿取csv文件里的内容
    def get_csv_data(self, csv_file, line):
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row
