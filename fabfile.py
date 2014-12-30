# -*- coding: utf-8 -*-
from fabric.api import run

def hello():
    run("uname -n")
    run("pwd")
