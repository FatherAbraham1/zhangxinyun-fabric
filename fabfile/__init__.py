from fabric.api import *

import prepare_env
import fab_flask

env.hosts = ['192.168.1.104']
env.user = 'anthony'
env.password = '1'

def init():
    prepare_env.install_pip()
    prepare_env.install_virtualenv()
    prepare_env.install_git()

def install():
    fab_flask.git_clone()
    fab_flask.create_virtualenv()
    fab_flask.pip_install()

def clean():
    fab_flask.clean()

def run():
    fab_flask.runserver()
        