import logging.config
from appium import webdriver
import yaml

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging.getLogger()

def appium_desired():
    with open('../config/desired_caps', 'r', encoding='utf-8') as file:
        # data = yaml.load(file)
        data = yaml.safe_load(file)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['automationName'] = data['automationName']

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver