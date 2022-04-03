#!/bin/bash
hostnamectl set-hostname server.projet.local
wget https://github.com/iredmail/iRedMail/archive/1.5.2.tar.gz
tar -xf 1.5.2.tar.gz
cd iRedMail-1.5.2/
chmod +x iRedMail.sh
./iRedMail.sh
