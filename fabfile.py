# -*- coding: utf-8 -*-
from fabric.api import sudo
from fabric.api import env
from fabric.decorators import task
from cuisine import run

env.hosts = ['vagrant@192.168.56.101']

@task
def hello():
    run("uname -n")
    run("pwd")

@task
def update_packages():
    sudo("apt-get update")

@task
def main():
    hello()
    #update_packages()
