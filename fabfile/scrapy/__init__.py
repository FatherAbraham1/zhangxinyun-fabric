#encoding:utf-8
from fabric.api import *

from .. import prepare

@task
def deploy():
    prepare();
    start();


def prepare():
    prepare_dependencies()
    prepare_scrapyd()
    prepare_scrapy_project()

def prepare_dependencies():
    sudo('apt-get update')
    sudo('apt-get install build-essential python-dev')
    sudo('apt-get install libxml2-dev libxslt-dev')
    sudo('apt-get install libssl-dev libffi-dev')

    sudo('apt-get install dtach')

def prepare_scrapyd():
    with cd('~'):
        run('rm -rf scrapyd')
        run('mkdir scrapyd')
        with cd('scrapyd'):
            run('virtualenv env')
            with prefix('source env/bin/activate'):
                run('pip install lxml')
                run('pip install pyopenssl')
                run('pip install scrapy')
                run('pip install scrapyd')

def prepare_scrapy_project():
    with cd('~'):
        run('rm -rf zhangxinyun-scrapy')
        run('git clone https://github.com/zhangxinyun/zhangxinyun-scrapy.git')
        with cd('zhangxinyun-scrapy'):
            run('virtualenv env')
            with prefix('source env/bin/activate'):
                run('pip install lxml')
                run('pip install pyopenssl')
                run('pip install scrapy')
                run('pip install scrapyd-client')

def start():
    with cd('~/scrapyd'):
        with prefix('source env/bin/activate'):
            run('dtach -n `mktemp -u /tmp/scrapy.XXXX` scrapyd')

    with cd('~/zhangxinyun-scrapy'):
        with prefix('source env/bin/activate'):
            run('scrapyd-deploy')
