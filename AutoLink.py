# -*- coding: utf-8 -*-
from flask import g

from utils.tools import Tools

__author__ = "苦叶子"

"""

公众号: 开源优测

Email: lymking@foxmail.com

"""
import os
import sys

from flask_script import Manager

from auto.www.app import create_app, load_all_task
from auto.settings import HEADER
from utils.help import check_version
from staticVar import staticVar


if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
    os.environ["PATH"] = os.environ["PATH"] + ":" + os.getcwd() + "/driver"
else:
    os.environ["PATH"] = os.environ["PATH"] + ";" + os.getcwd() + "/driver"

print(HEADER)

app = create_app('default')
manager = Manager(app)
staticVar.initapp = app



if __name__ == '__main__':
    Tools.runLogHander.debug(__file__)
    Tools.runLogHander.debug(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    check_version()
    load_all_task(app)
    manager.run()


