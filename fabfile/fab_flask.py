from fabric.api import *
from contextlib import contextmanager

def git_clone():
    with cd('~'):
        run('git clone https://github.com/zhangxinyun/zhangxinyun-flask.git')

def create_virtualenv():
    with cd('~/zhangxinyun-flask'):
        run('virtualenv env')

@contextmanager
def virtualenv():
    with cd('~/zhangxinyun-flask'):
        with prefix('source env/bin/activate'):
            yield

def pip_install():
    with virtualenv():
        run('pip install -r requirements.txt')

def runserver():
    with virtualenv():
        run('python manage.py runserver')

def clean():
    with cd('~'):
        run('rm -rf zhangxinyun-flask')