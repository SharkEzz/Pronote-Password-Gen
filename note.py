#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python :2.7

#Présentation
try:
 print("#Chance d'avoir le bon mot de passe : 100 %")
 print("#CTRL+C pour fermer le programme.")
except KeyboardInterrupt  :
 print("\n[*] Sortie du programme ..\n")
 os.system("pause")
 sys.exit(1)

#Importation
try:
 import os,sys,time
except ImportError:
 print("\n[*] Impossible d'importer une librairie ")
 print("\n[*] Sortie du programme ...\n")
 os.system("pause")
 sys.exit(1)


#creation fichier log
def log():
 global pseudo
 user = os.path.expanduser("~")
 user = user + "/Brutenote"
 date = time.strftime("%D %H:%M:%S")
 logs = open(user + "/logs.txt","a")
 logs.write(str(date)+" : "+ str(pseudo)+"\n")
 logs.close

#creation dossier principal
def dossier():
 user = os.path.expanduser("~")
 user = user + "/Brutenote"
 if not os.path.isdir(user) :
  os.mkdir(user)
 



#Demande des informations obligatoire et traitement des informations
try:
 prenom=raw_input("Prenom du compte :")
 nom=raw_input("nom du compte :")
 prenom=prenom.lower()
 nom=nom.lower()
 prenom=prenom.strip()
 nom=nom.strip()
 premier=prenom[0:2]
 second=nom[0:2]
 pseudo=(prenom)+(".")+(nom)
except KeyboardInterrupt  :
 print("\n[*] Sortie du programme ..\n")
 os.system("pause")
 sys.exit(1)

# creation du dictionnaire de mot de passe et du dossier
try:
 dossier()
 user = os.path.expanduser("~")
 user = user + "/Brutenote"
 fichier=open(user + "/dico.txt", "w")
except KeyboardInterrupt  :
 print("\n[*] Sortie du programme ...\n")
 os.system("pause")
 sys.exit(1)

# generation des mots de passe
try:
 a=10
 c=10
 e=10
 g=0
 while a!=100:
  for i in range(10,100):
   fichier.write(str(premier)+str(a)+str(second)+str(i)+"&*"+"\n")
   if i==99:
    a+=1
    i==0
 while c!=100:
  for d in range(0,10):
    fichier.write(str(premier)+str(c)+str(second)+"0"+str(d)+"&*"+"\n")
    if d==9:
     d==0
     c+=1
 while e!=100:
   for f in range(0,10):
    fichier.write(str(premier)+"0"+str(f)+str(second)+str(e)+"&*"+"\n")
    if f==9:
     f==0
     e+=1
 while g!=10:
  for h in range(0,10):
   fichier.write(str(premier)+"0"+str(g)+str(second)+"0"+str(h)+"&*"+"\n")
   if h==9:
    h==0
    g+=1

 fichier.close()
except KeyboardInterrupt :
 print("\n[*] Sortie du programme ...\n")
 sys.exit(1)
except IOError :
 print("\n[*] Le fichier dico.txt est introuvable !")
 print("\n[*] Le fichier doit etre dans le meme répertoire que le script.")
 print("\n[*] Sortie du programme ...\n")
 os.system("pause")
 sys.exit(1)

# affichage du resultat et d'informations
try:
 print "\n[*]Dictionnnaire : dico.txt "
 print "\n[*]Le nom d'utilisateur est : {0}".format(pseudo)
 log()
 os.system("pause")
except KeyboardInterrupt  :
 print("\n[*] Sortie du programme ...\n")
 os.system("pause")
 sys.exit(1)