#!/usr/bin/python3
"""fab script that generates a .tgz archive
from the contents of the web_static"""

from datetime import datetime
import os
from fabric.api import *


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
