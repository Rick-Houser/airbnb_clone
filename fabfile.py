from fabric.api import *
# fab deploy_to_web1 deployWeb1 to deploy


def deploy_to_web1():
        # Specifying wich host I want to use
        env.use_ssh_config = True
        env.hosts = ['admin']


def deploy_to_web2():
    # Specifying wich host I want to use
    env.use_ssh_config = True
    env.hosts = ['ubuntu']


def ship():
    # pushing to github
    with lcd('/Users/stevengarcia/Desktop/airbnb_clone'):
        local('git add . && git commit -a --allow-empty-message -m " " ')
        local('git push')


def deployWeb1():
    # Pulling from a github repository
    with cd('/home/admin/airbnb_clone'):
        run('sudo git pull')


def deployWeb2():
    # trying to Pull from a github repository if fails it clones repository
    try:
        with cd('/home/ubuntu/airbnb_clone'):
            run('sudo git pull')
    except:
        with cd('/home/ubuntu/'):
            run('git clone https://github.com/stvngrcia/airbnb_clone.git')
