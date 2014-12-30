# -*- coding: utf-8 -*-
from fabric.api import run
from fabric.api import sudo

def hello():
    run("uname -n")
    run("pwd")

def update_packages():
    sudo("apt-get update")
