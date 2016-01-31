from fabric.api import *

import prepare
import scrapy
import flask

env.hosts = ['192.168.1.103']
env.user = 'anthony'
env.password = '1'


@task
def init():
    install_git()
    install_pip()
    install_virtualenv()
