# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.decorators import task
from fabric.contrib import files
from fabric.colors import red, green
from cuisine import run
import cuisine

env.hosts = ['vagrant@192.168.56.101']

@task
def update_packages():
    puts(green('update packages'))
    #sudo("apt-get update")

# 使いそうなツール
@task
def setup_devtools():
    puts(green('Installing Devtools'))
    packages = '''
        vim curl wget build-essential tmux screen zsh make sqlite3 tig tree locate git-core
        '''.split()

    for pkg in packages:
        cuisine.package_ensure(pkg)

# アプリケーション
@task
def setup_packages():
    puts(green('Installing Packages'))
    cuisine.package_ensure('apache2')

@task
def restart_application():
    puts(green('Restarting application'))
    cuisine.upstart_ensure('apache2')

@task
def main():
    update_packages()
    setup_devtools()
    setup_packages()
    restart_application()

    puts(green('finish script'))
