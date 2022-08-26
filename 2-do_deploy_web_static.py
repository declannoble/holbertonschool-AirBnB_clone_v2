#!/usr/bin/python3
"""script to upload archive to web server"""
from fabric.api import *

env.hosts = ['3.94.193.192', '50.19.39.94']


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
