#!/usr/bin/env bash
# prepare the web server for deployment
apt-get -y update
apt-get install -y nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -hR ubuntu:ubuntu /data/
serve="\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t}"
sed -i "s/^\tserver_name .*;$/&\n$serve/" /etc/nginx/sites-available/default
service nginx restart
