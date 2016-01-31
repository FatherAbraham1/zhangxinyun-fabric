from fabric.api import *

def install_pip():
    get_pip_url = "https://bootstrap.pypa.io/get-pip.py";
    with cd('~'):
        run('wget ' + get_pip_url)
        sudo('python get-pip.py')
        run('rm -f get-pip.py')

def install_virtualenv():
    sudo('pip install virtualenv')

def install_git():
    sudo('apt-get update')
    sudo('apt-get install git')