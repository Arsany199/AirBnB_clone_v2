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
    """deploy archive to the server"""
    if not os.path.exists(archive):
        return False
    f_name = archive.split('/')[1]
    f_path = "/data/web_static/releases/"
    rel_path = f_path + f_name[:-4]
    try:
        put(archive, '/tmp/')
        run('mkdir -p {}'.format(rel_path))
        run('tar -xzf /tmp/{} -C {}'.format(f_name, rel_path))
        run('rm /tmp/{}'.format(f_name))
        run('mv {}/web_static/* {}/'.format(rel_path, rel_path))
        run('rm -rf {}/web_static'.format(rel_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(rel_path))
        print('New version deployed!')
        return True
    except Exception as e:
        print(f"Exception occurred: {e}")
        return False
