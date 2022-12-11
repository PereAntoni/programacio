#El programa ha de llegir una paraula d'un llistat de paraules

import requests
import json
import random
import operator
import pickle

def guarda(dict):
    with open("myDictionary.pkl", "wb") as tf:
        pickle.dump(dict,tf)


#clients_sort = sorted(clients.items(), key=operator.itemgetter(1), reverse=True)
#cream el diccionari a partir del consum de l'api de gimnesia
print("a")
resp = requests.get('http://api.gimnesia.net/especie/read.php')
person_dict = json.loads(resp.content)
print("a")
#person_dict = sorted(person_dict.records(),key=operator.itemgetter(1),reverse=False)
#person_dict = sorted(person_dict)
#print(person_dict)
# Output: ['English', 'French']
def getRandom():
    especie=person_dict['records'][random.randint(0, 92)]
    return especie["nom"]

def llistatTots():
    for i in person_dict['records']:
        print (i["codi"], ":",i["nom"])
#print(especie['nom'])
#print(especie['cientific'])



for i in range(1,30):
    llista=[]
    for j in range(10):
        #comprovam qe no tengui duplicats:
        ficat = False
        while not ficat:
            nou = getRandom()
            if nou not in llista:
                ficat = True
                llista.append(getRandom())
    print()
    print(str(i), ":")
    print("cadena =", llista)
    print("nom ='" + llista[5] + "'")
    print("cadena2 = [3,5,6,3,2,7,5,9,1]")
    print()
#guarda(person_dict)


#llistatTots()
