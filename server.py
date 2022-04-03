#!/usr/bin/python3
import socket
import time
import json
import database
#import mysql.connector

# cette fonction  permet au serveur de recupérer les informations d'inscription d'un client
def Inscription(client:socket, buffer:int):
    liste = list()
    req = "ENTREZ VOTRE NOM  SVP : " 
    client.send(req.encode("utf-8")) #1
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    req = "ENTREZ VOTRE PRENOM SVP :"
    client.send(req.encode("utf-8")) #2
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    req = "ENTREZ VOTRE MAIL SVP :"
    client.send(req.encode("utf-8")) #3
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    requete1 = "mdp1"
    requete2 = "mdp2"

    while requete1 != requete2:
        req = "ENTREZ VOTRE PASSWORD SVP :"
        client.send(req.encode("utf-8")) #4
        requete1 = client.recv(buffer)

        req = "ENTREZ DE NOUVEAU VOTRE PASSWORD :"
        client.send(req.encode("utf-8")) #5
        requete2 = client.recv(buffer)

        if requete1 != requete2:
            req = "LES PASSWORD SONT DIFEERENTS !!"
            client.send(req.encode("utf-8")) #3
        else:
            req = "LES PASSWORD SONT LES MEMES !!"
            client.send(req.encode("utf-8")) #3

    liste.append(requete1.decode("utf-8"))
    if database.Inscription(liste) == True:
        req = "INSCRIPTION REUSSIE !!!"
        client.send(req.encode("utf-8")) #6
    else:
        req = "ECHEC DE L'INSCRIPTION !!!"
        client.send(req.encode("utf-8")) #6

#Cette fonction permet au serveur de recupérer les informations de connexion du client
def Connexion(client:socket,buffer:int):
    liste = list()
    req = "Veuillez entrer votre adresse mail svp :"
    client.send(req.encode("utf-8")) #1
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    req = "Veuillez entrer votre mot de passe svp :"
    client.send(req.encode("utf-8")) #2
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    if database.Connexion(liste) == True:
        req = "CONNEXION REUSSIE !!!"
        client.send(req.encode("utf-8")) #3
    else:
        req = "Echec de lors de la connexion !!!"
        client.send(req.encode("utf-8")) #3

#Cette fonction permet au serveur d'initialiser une connexion avec le client
def openServer(host,
               port,
               buffer=1024):
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind((host,port))
    serveur.listen(5)

    client, infosClient = serveur.accept()
    print("Client connecté avec l'Adresse " + infosClient[0])  

    while True:    
        
        reponse = "VEUILLEZ CHOISIR 1 POUR VOUS INSCRIRE ,2 POUR VOUS CONNECTER, 3 POUR FERMER :"
        client.send(reponse.encode("utf-8"))
        time.sleep(2)

        requete = client.recv(buffer)
        requete_decode = requete.decode("utf-8")

        if requete_decode == "1":
            Inscription(client,buffer)

        elif requete_decode == "2":
            Connexion(client,buffer)

        elif requete_decode == "3":         
            req = "BYE !!!"
            client.send(req.encode("utf-8")) 
            client.close()
            break

    serveur.close()
           
    


if __name__ == "__main__":
    
    openServer('192.168.10.1', 50000)
