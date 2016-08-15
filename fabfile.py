from fabric.api import *
env.use_ssh_config = True
env.hosts = ['ubuntu']

def ship():
    with lcd('/Users/stevengarcia/Desktop/airbnb_clone'):
        local('git add . && git commit -a --allow-empty-message -m " " ')
        local('git push')
def deploy():
    with cd('/home/admin/airbnb_clone'):
        run('sudo git pull')
