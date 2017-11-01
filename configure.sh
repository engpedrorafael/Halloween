#!/bin/bash

echo "Installing dependencies..."
sudo apt-get update
sudo apt-get install vim vlc apache2
sudo usermod -aG dialout www-data
sudo usermod -aG sudo www-data
sudo usermod -aG pulse-access www-data
sudo usermod -aG pulse www-data
sudo usermod -aG audio www-data
sudo chown -R www-data.www-data  /var/www/

echo "Installing Web Page..."
sudo cp webPage/000-default.conf /etc/apache2/sites-available/
sudo ls -s /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-enabled/000-default.conf

cat webPage/page.cgi | sed "s#%PATH%#$(pwd)#g" > webPage/page.cgi_installed
sudo cp webPage/page.cgi_installed /usr/lib/cgi-bin/page.cgi
sudo chmod 755 /usr/lib/cgi-bin
sudo chown root.root /usr/lib/cgi-bin
sudo chmod 775 /usr/lib/cgi-bin/page.cgi

cat webPage/index.html | sed "s#%IP%#$(hostname -I)#g" > webPage/index.html_installed
sudo cp webPage/index.html_installed /var/www/html/indes.html
sudo chown www-data.www-data /var/www/html/index.html

echo "Restarting apache..."
sudo a2enmod cgi
sudo service apache2 restart


