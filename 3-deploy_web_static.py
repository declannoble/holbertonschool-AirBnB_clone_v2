#!/usr/bin/python3
from datetime import datetime
from fabric.api import *

env.hosts = ['3.94.193.192', '50.19.39.94']


def do_pack():
    """generates a tgz archive from the web_static directory"""
    currentTime = datetime.now()
    timeString = currentTime.strftime("web_static_%Y%m%d%H%m%S")
    fileName = "versions/{}.tgz".format(timeString)
    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(fileName))
    if result:
        return fileName
    else:
        return None


def do_deploy(archive_path):
    """
    pushes, and decompresses archive file to webserver
    """
    archive_list = archive_path.split("/")
    archiveFile = archive_list[-1]
    fileName = archiveFile.split('.')[0]
    directory = "/data/web_static/releases" + fileName + '/'

    try:
        put(archive_path, "/tmp/")
        run('mkdir -p {}'.format(directory))
        run('tar -xzf /tmp/{} -C {}'.format(archiveFile, directory))
        run('rm /tmp/{}'.format(archiveFile))
        run('mv {}/web_static/* {}'.format(directory, directory))
        run('ln -sfn {} /data/web_static/current'.format(directory))
        return True
    except Exception:
        return False


def deploy():
    """
    takes in do_deploy and do_pack to distribute archive to web servers
    """
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
    return None
