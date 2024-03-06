#!/usr/bin/python3
"""fab script that generates a .tgz archive from the contents of the web_static"""

from datetime import datetime
import os
import fabric


def do_pack():
    """to make archive"""
    d = datetime.now()
    local("sudo mkdir -p versions")
    archive = "versions/web_static_{}{}{}{}{}{}.tgz"
                .format(d.year, d.month, d.day, d.hour, d.minute, d.second)
    res = local("sudo tar -cvzf {} web_static".format(archive))
    if res.failed:
        return None
    else:
        return archive
