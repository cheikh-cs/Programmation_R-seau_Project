#!/bin/bash

sudo apt-get update
sudo apt-get install -y wget
wget https://dev.mysql.conn/get/mysql-apt-config_0.8.22-1_all.deb
sudo apt-get install ./mysql-apt-config_0.8.22-1_all.deb
sudo apt-get installmysql-community-server
sudo systemctl enable --now mysql
