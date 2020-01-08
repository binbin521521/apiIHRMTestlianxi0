"""
编写初始化日志的函数
"""
import logging
from logging import handlers
import os

"""全局变量的封装"""
# 绝对路径的封装
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# url的封装
HOST = "http://182.92.81.159"
# headers的封装
HEADERS = {"Content-Type": "application/json"}
# 登陆后ID的封装
EMP_ID = ""

"""日志器函数封装"""


def init_logging():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 设置处理器
    # 设置控制台处理器
    sh = logging.StreamHandler()
    # 设置文件处理器
    # TimedRotatingFileHandler 可以用来帮助我们切分日志：
    # 按时间来设置日志
    filename = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename,when='m', interval=1, backupCount=7)
    # 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 将格式化器添加到处理器中
    # 添加到控制台
    sh.setFormatter(formatter)
    # 添加到文件处理器
    fh.setFormatter(formatter)
    # 将处理器添加到日志器
    logger.addHandler(fh)
    logger.addHandler(sh)
