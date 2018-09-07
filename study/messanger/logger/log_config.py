import logging
import time
import re
import sys

logging.basicConfig(
    filename = "messenger_{}.log".format(time.strftime('%d_%m_%y', time.localtime())),
    format = "%(asctime)s %(levelname)s %(name)s.%(funcName)s %(message)s",
    level = logging.DEBUG
)


def logger():
    filename = re.findall(r"[a-zA-Z0-9._]+$", sys.argv[0])
    log = logging.getLogger(filename[0])
    return log


def log(func):
    def wrapper(*args, **kwargs):
        func_str = func.__name__
        filename = re.findall(r"[a-zA-Z0-9._]+$", sys.argv[0])
        with open('{}_{}.log'.format(filename[0], time.strftime('%d_%m_%y', time.localtime())), 'a') as file:
            file.write('{} function {} start '.format(time.ctime(), func_str))
            file.write(' with args {} '.format(str(args)))
            file.write(' with kwargs {}\n'.format(kwargs))
        return func(*args, **kwargs)
    return wrapper

