#El programa ha de llegir una paraula d'un llistat de paraules

import requests
import json
import random

def consumeix():
    resp = requests.get('http://api.gimnesia.net/especie/read.php')
    return json.loads(resp.content)

def getRandom(l):
    especie = l['records'][random.randint(0, 92)]
    return especie["nom"]

def llistatTots(l):
    for i in l['records']:
        print (i["codi"], ":",i["nom"])

def mostraOpcions():
    print ("-----------------------------")
    print ("0: Surt del programa")
    print ("1: Element a triar")
    print ("2: Consumeix dades")
    print ("3: llista totes les dades")
    print ("4: Cerca una espècie")
    print ("-----------------------------")
    return int(input("Inserta el valor:"))

#DADES ESTRUCTURA DEL PROGRAMA
llista=[]
opcio=-1
#PROGRAMA PRINCIPAL
while opcio!=0:
    if opcio==1:
        print("ha de mostrar un missatge on demana quin nombre d'element es vol veure")
    if opcio==2:
        llista= consumeix()
    if opcio==3:
        llistatTots(llista)
    if opcio==4:
        print("ha de mostrar un missatge on demana quin element es vol cercar")
    opcio = mostraOpcions()

