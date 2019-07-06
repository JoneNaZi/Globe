import re, subprocess, os
import logging
class ApkInfo():
    def __init__(self, apkPath):
        self.apkPath = apkPath

    # 获取apk的包名以及基本信息
    def getApkBaseInfo(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdin=subprocess.PIPE
                             , stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        # print(p.communicate())
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
        # print(match)
        print(output.decode())
        if not match:
            raise Exception("can't get packageinfo")
        packagename = match.group(1)
        appkey = match.group(2)
        appVersion = match.group(3)
        logging.info('======getApkInfo======')
        logging.info('packageName:', packagename)
        logging.info('appkey:', appkey)
        logging.info('appVersion:', appVersion)
        # print(packagename, appkey, appVersion)

    # 获取启动类
    def getApkActivity(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdin=subprocess.PIPE
                             , stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("launchable-activity: name='(\S+)'").search(output.decode())
        # print(output.decode())
        # if match is not None:
        #     print(match.group(1))

if __name__ == '__main__':
    info = ApkInfo(r'D:\Downloads\app-debug.apk')
    info.getApkBaseInfo()
    info.getApkActivity()