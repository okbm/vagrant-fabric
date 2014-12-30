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
$ vagrant ssh
```
