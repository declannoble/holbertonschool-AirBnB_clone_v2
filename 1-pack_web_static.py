#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
from the contents of the web_static folder
sing the function do_pack. """

from fabric.api import local
import datetime


def do_pack():
    """
        Generates a .tgz archine from contents of web_static
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"version/web_static_{date}.tgz"
    local("mkdir -p versions")
    archive_file = local("tar -czvf {}.tar.gz web_static".format{filename})
    if archive_file:
        return filename
    else:
        return None
