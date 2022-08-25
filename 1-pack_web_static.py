#!/usr/bin/python3
from datetime import datetime
from fabric.api import local


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
