#abby
import os
import shlex
import signal
import subprocess
import time

import pytest


@pytest.fixture(scope='class')
def record():
    # 切割成一个数组，3个命令
    now_time=time.strftime("%Y%m%d%H%M%S", time.localtime())
    str="scrcpy --record "+now_time+'.mp4'
    cmd = shlex.split(str)
    # shell =false ,不使用shell 这种方式，shell 所有的命令在一行，由于系统不同，不同系统使用的命令不一样，wind-cmd ,linux -bash
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)
