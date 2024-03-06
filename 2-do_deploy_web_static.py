#!/usr/bin/python3
"""Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers"""

from datetime import datetime
import os
from fabric.api import *

env.host = ['52.201.211.116', '54.210.96.228']
env.user = "ubuntu"


def do_pack():
    """to make archive"""

    local("sudo mkdir -p versions")
    d = datetime.now()
    archive = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            d.year, d.month, d.day, d.hour, d.minute, d.second)
    res = local("sudo tar -cvzf {} web_static".format(archive))
    if res.failed:
        return None
    else:
        return archive


def do_deploy(archive_path):
    '''
    Deploy archive to web server
    '''
    if not os.path.exists(archive):
        return False
    file_name = archive.split('/')[1]
    file_path = '/data/web_static/releases/'
    releases_path = file_path + file_name[:-4]
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(releases_path))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, releases_path))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}/web_static/* {}/'.format(releases_path, releases_path))
        run('rm -rf {}/web_static'.format(releases_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases_path))
        print('New version deployed!')
        return True
    except:
        return False
