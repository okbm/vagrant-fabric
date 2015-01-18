# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.decorators import task
from fabric.contrib import files
from fabric.colors import red, green
from cuisine import run
import cuisine

env.hosts = ['vagrant@192.168.56.101']
#env.port = 2222
env.user = 'vagrant'
env.password = 'vagrant'
env.forward_agent = True

@task
def update_packages():
    puts(green('update packages'))
    sudo("apt-get update")

# 使いそうなツール
@task
def setup_devtools():
    puts(green('Installing Devtools'))
    packages = '''
        vim curl wget build-essential tmux screen zsh make sqlite3 tig tree locate git-core python-software-properties
        '''.split()

    for pkg in packages:
        cuisine.package_ensure(pkg)

# アプリケーション
@task
def setup_packages():
    puts(green('Installing Packages'))

    # apache2
    cuisine.package_ensure('apache2')

    sudo ("rm -rf /var/www")
    sudo ("ln -fs /home/vagrant /var/www")

    # php
    sudo("add-apt-repository -y ppa:ondrej/php5-5.6")
    sudo("apt-get update")

    packages = '''
        php5 libapache2-mod-php5 php5-mysql php5-curl php5-gd php5-mcrypt php5-xdebug php5-cli
        '''.split()

    for pkg in packages:
        cuisine.package_ensure(pkg)

    # other
    cuisine.package_ensure('mysql-server-5.5')
    cuisine.package_ensure('redis-server')

    # composer
    run("curl -sS https://getcomposer.org/installer | php")
    sudo("mv composer.phar /usr/local/bin/composer")
    run('composer global require "phpunit/phpunit=4.3.*"')
    run('echo PATH="$PATH":~/.composer/vendor/bin/ >> ~/.bashrc')

@task
def restart_application():
    puts(green('Restarting application'))
    cuisine.upstart_ensure('apache2')

@task
def setup_original():
    puts(green('setup original'))

    # ssh
    run('echo "Host github.com" > $HOME/.ssh/config');
    run('echo "     HostName github.com" >> $HOME/.ssh/config');
    run('echo "     User git" >> $HOME/.ssh/config');
    run('echo "     StrictHostKeyChecking no" >> $HOME/.ssh/config');
    run('chmod 600 $HOME/.ssh/config');

    # git
    run('git clone git@github.com:okbm/dotfiles.git');
    run('WORK=$HOME/');

    # mysql
    # mysql -uroot -proot < $WORK/misc/local-create.sql

@task
def setup_tmp():
    puts(green('tmp done'))
#   確認用のコマンドをここで動かしてOKなら別のところに移動させる
    # mysql
    # mysql -uroot -proot < $WORK/misc/local-create.sql


@task
def main():
    update_packages()
    setup_devtools()
    setup_packages()
    restart_application()

    setup_original()
    setup_tmp()

    puts(green('finish script'))

