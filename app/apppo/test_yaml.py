"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/7 5:09 下午'
"""
# python 自带的日志收集模块
import logging

import yaml

logging.basicConfig(level=logging.INFO)


def test_yaml():
    logging.info("test_yaml")

    pythonobj = {
        'desirecaps': {'platformName': 'android', 'deviceName': 'emulator-5554', 'appPackage': 'com.tencent.wework',
                       'appActivity': '.launch.LaunchSplashActivity', 'noReset': 'true',
                       'skipServerInstallation': 'true',
                       'skipDeviceInitialization': 'true'}, 'server': {'ip': '127.0.0.1', 'port': 4723}}
    print(yaml.safe_dump(pythonobj))
    logging.info(yaml.safe_dump(pythonobj))
