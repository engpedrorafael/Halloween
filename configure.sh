#!/bin/bash

if [[ $# -eq 1 ]];then
    IP=$1
else
    IP=$(hostname -I | cut -d ' ' -f 1 | tr -d ' ')
fi

echo "Using IP: ${IP}"

echo "Installing dependencies..."
sudo apt-get update
sudo apt-get install -y vim vlc apache2 python-serial openssh-server
sudo usermod -aG dialout www-data
sudo usermod -aG sudo www-data
sudo usermod -aG pulse-access www-data
sudo usermod -aG pulse www-data
sudo usermod -aG audio www-data
sudo chown -R www-data.www-data  /var/www/

./update.sh

echo "Please restart the PC and access the page:  http://${IP}"
