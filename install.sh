#!/bin/bash
apt-get install apache2
a2enmod cgid
cd /etc/apache2/mods-enabled
ln -s /etc/apache2/mods-available/cgi.load
sudo vi /etc/apache2/conf-enabled/serve-cgi-bin.conf


