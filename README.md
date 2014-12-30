vagrant fabric
====
vagrantをfabricでセットアップしてみる

## Description

| インストール | version |
|:-----------|:------------|
| php        |        This |
| apache     |      column |
| mysql      |        will |
| redis      |          be |
| python     |       right |

- その他
  - git
  - zsh
  - curl
  - など

## Requirement

以下をインストール(macのみでしか検証してません！！)
- virualbox
  - [Downloads – Oracle VM VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- vagrant
  - [Download Vagrant - Vagrant](https://www.vagrantup.com/downloads.html)
- fabric
```
$ easy_install pip
$ pip install fabric
$ pip install paramiko==1.10  # paramikoがいるってエラーでたのでinstall
```

## Install

```
$ vagrant up
$ fab -H vagrant@192.168.56.101 update_packages
$ vagrant ssh
```

## developer memo
- fabtool?
  - [Welcome to fabtools’s documentation! — fabtools 0.17.0 documentation](http://fabtools.readthedocs.org/en/0.17.0/)

- vagrant確認中はsandboxを有効にする

```
$ vagrant plugin install sahara

$ vagrant sandbox on
$ vagrant sandbox rollback
$ vagrant sandbox commit
$ vagrant sandbox off
$ vagrant sandbox status
```

- saharaのインストールが失敗する
  - [jedi4ever/sahara](https://github.com/jedi4ever/sahara)

## other
- [複数プロジェクトを抱えるチームでのデプロイ自動化 | SOTA](http://deeeet.com/writing/2014/10/30/fabric/)
