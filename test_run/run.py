import HTMLTestRunner
import logging
import unittest
import time

test_dir = '../test_case'
report_dir = '../reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')

report_name = report_dir + '/' + now + 'test_report.html'

with open(report_name, 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='HuanQiu Test Report', description=u'HuanQiu Android App Test Report')
    logging.info('start run test case...')
    runner.run(discover)