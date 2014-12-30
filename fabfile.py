# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.decorators import task
from fabric.contrib import files
from fabric.colors import red, green
from cuisine import run

import cuisine
# cuisine.select_package("apt")

env.hosts = ['vagrant@192.168.56.101']

@task
def update_packages():
    puts(green('update packages'))
    #sudo("apt-get update")

@task
def setup_devtools():
    puts(green('Installing Devtools'))
    packages = '''
        vim curl wget build-essential tmux screen zsh make sqlite3 tig tree locate git-core
        '''.split()

    for pkg in packages:
        cuisine.package_ensure(pkg)

@task
def main():
    update_packages()
    setup_devtools()

    puts(green('finish script'))
