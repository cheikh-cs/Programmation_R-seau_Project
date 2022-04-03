# Programmation_R-seau_Project

Ici nous avons mis en place des scripts permettant d'etablir des connexion entre un client et un serveur de base de donnees et un script analyseur de paquets 

**A - Script database.py : module qui permet d'interagir avec la base de données.**

ce script permet d'etablir une communication entre le serveur et la base de données pour l'enregistrement, la sauvegarde des informations des clients.
-nous avons donc importer mysql.connector qui est un module qui permet d'interagir avec la base de données.
Ce script sera exécuté dans la machine serveur.



**B - Script server.py : module qui permet de fournir des services a un client.**

Ce script permet d'etablir une communication avec le client et récupère les informations entrées par le client afin de les enregistrer dans la base de données. 
de ce fait nous avons importé la base de données pour que les informations inserées soient sauvegardées dans la base de données.

Pour lancer le script côté server on lance lance la commande: **python3 server.py.**
Ce script sera exécuté dans la machine serveur.



**C - Script client.py : module qui permet d'interagir avec un serveur en ecoute.**
Le script client.py va permettre au client d'etablir une connexion avec son serveur et d'interagir avec celui ci; de ce fait nous avons mis en place :
-une fonction Inscription qui interagit avec le serveur pour inscrire les identifiants d'un client dans la base de donnée.
-une fonction Connexion qui interagit avec le serveur pour se connecter.

Pour lancer le script on execute la commande : **python3 client.py.**
 Mais pour ce faire il faut d'abord lancer le serveur d'abord comme expliquer dans la partie B.
 Ce script sera exécuté dans la machine cliente.



**D- Analyseur_Packet : module qui permet de capturer des packets UDP/TCP.**
Ce script fonctionne en analysant les paquets et récupère ensuite tous les packets TCP/UDP en plus des entête les types de protocoles utilisés les adresses IP  puis les ports utilisés dans la communication. 

On lance le script dans une machine Kali linux qui fait office de Man in the Middle en executant la commande : **python3 Analyseur_Packet.py 60** (60 est le durée d'analyse des packest en s)


