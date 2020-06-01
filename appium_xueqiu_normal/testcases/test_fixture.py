# abby
import os
import shlex
import signal
import subprocess

import pytest
import yaml

from appium_xueqiu_normal.common.dir_config import data_dir, video_dir


def handle_back(func):
    def wrapper(*args, **kwargs):
        print('异常处理开启了')
        res = func(*args, **kwargs)
        print(func.__name__)

        print('异常处理停止了')

    return wrapper


@handle_back
def do_cacke(size, weidao, caomei):
    return ('尺寸大小{0},口味{1},{2}'.format(size, weidao, caomei))


# handle_back(do_cacke)(1.6,'偏甜',caomei=10)
# res = do_cacke(1.6, '偏甜', caomei=10)
filename=os.path.join(data_dir, 'test_search.yaml')
# print(yaml.safe_load(open(filename,encoding='utf-8')))


@pytest.mark.parametrize('searchkey,search_result',
                         yaml.safe_load(open(os.path.join(data_dir, 'test_search.yaml'), encoding='utf-8')))
def test_p(searchkey, search_result):
    print(searchkey)
    print(search_result)


def test_vi():
    # 切割成一个数组(默认空格切割)，3个命令--》<class 'list'>: ['scrcpy', '--record', 'tmp.mp4']
    import time

    now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    str = "scrcpy --record " +now_time+ '.mp4'
    cmd = shlex.split(str)
    # shell =false ,不使用shell 这种方式，shell 所有的命令在一行，由于系统不同，不同系统使用的命令不一样，wind-cmd ,linux -bash
    # stderr错误
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    import time
    time.sleep(10)
    os.kill(p.pid, signal.CTRL_C_EVENT)

test_vi()