#!/bin/bash

if [[ $# -eq 1 ]];then
    IP=$1
else
    IP=$(hostname -I | cut -d ' ' -f 1 | tr -d ' ')
fi

echo "Using IP: ${IP}"

sudo chown -R www-data.www-data  /var/www/
sudo rm -rf /var/www/html/*

echo "Installing Web Page..."
sudo cp webPage/000-default.conf /etc/apache2/sites-available/
sudo ls -s /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-enabled/000-default.conf

cat webPage/page.cgi | sed "s#%PATH%#$(pwd)#g" > webPage/page.cgi_installed
sudo cp webPage/page.cgi_installed /usr/lib/cgi-bin/page.cgi
sudo chmod 755 /usr/lib/cgi-bin
sudo chown root.root /usr/lib/cgi-bin
sudo chmod 775 /usr/lib/cgi-bin/page.cgi

cat webPage/index.html | sed "s#%IP%#${IP}#g" > webPage/index.html_installed
sudo cp webPage/index.html_installed /var/www/html/index.html
sudo chown www-data.www-data /var/www/html/index.html
sudo ln -s $(pwd)/images /var/www/html/images
sudo chmod -R 777 /var/www/html/images

echo "Restarting apache..."
sudo a2enmod cgi
sudo service apache2 restart

echo "Access the page:  http://${IP}"
