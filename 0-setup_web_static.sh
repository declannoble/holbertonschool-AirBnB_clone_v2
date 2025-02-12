#!/usr/bin/env bash                                                                                                                                                       
# script to setup web servers to deploy static website                                                                                                                    
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "                                                                                                                                                               
    <html>                                                                                                                                                                
        <head>                                                                                                                                                            
        </head>                                                                                                                                                           
        <body>                                                                                                                                                            
            Holberton School                                                                                                                                              
        </body>                                                                                                                                                           
    </html>                                                                                                                                                               
" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/a location /hbnb_static { \n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
