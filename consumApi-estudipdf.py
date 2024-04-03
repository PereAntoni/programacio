import requests
import json
import random
from tabulate import tabulate
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import os

#595X842

class Carta:
    def mostrar(self):
        pass

# Subclasses per a diferents tipus de cartes
class CartaPoker(Carta):
    def mostrar(self):
        print("Carta de pòquer")

class CartaTrumfu(Carta):
    def mostrar(self):
        print("Carta de trumfu")

# Factory Method
class FabricaCartes:
    def crear_carta(self, tipus):
        if tipus == "poker":
            return CartaPoker()
        elif tipus == "trumfu":
            return CartaTrumfu()
        else:
            return None

# Exemple d'ús
fabrica = FabricaCartes()
carta1 = fabrica.crear_carta("poker")
carta2 = fabrica.crear_carta("trumfu")

#https://github.com/codemaker1999/BCards
def consumeix():
    resp = requests.get('http://api.gimnesia.net/especie/read.php')
    return json.loads(resp.content)

def obriAnalisi():
    df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6], 'c':[7,8,9]})
    show(df)


def creaPdf2(l):
    c = canvas.Canvas("content_pdf.pdf", pagesize=A4)
    c.setFillColor(colors.grey)
    c.setFont("Helvetica-Bold", 24)
    
    #c.drawString(50, 700, "Creating PDFs with Python")
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 14)
    """
    c.drawString(0,0, "+ (0,0)")
    c.drawString(10,0, "+ (10,0)")
    c.drawString(20,0, "+ (20,0)")
    c.drawString(100,0, "+ (100,0)")
    c.drawString(200,0, "+ (200,0)")
    c.drawString(10,800, "+ (10,800)")
    c.drawString(0,100, "+ (0,100)")
    c.drawString(10,200, "+ (10,200)")
    c.drawString(400,500, "+ (400,500)")
    c.drawString(500,800, "+ (500,800)")
    c.drawString(200,220, "+ (200,220)")
    """
    #recorregut de la llista que coloqui totes les
    #cartes damunt un canva
    #mida a4: 595X842
    # 3 columnes x 3 files
    files=3
    columnes = 3

    columna = 0
    fila = 0
    p=0
    for i in l:
        #columna
        p = p + 1
        print("fila: " + str(fila) + ", columna: "+ str(columna))
        if columna == 3:
            columna=0
            fila += 1
        posx = columna * 190
        posx += 20 #marge
        columna +=1
        #fila
        posy = 560 - (fila * 260)
        posy -= 20 #marge
        c.rect(4 + posx, posy, 185, 255, stroke=1, fill=0) 
        image_path = os.path.join(os.getcwd(), "fotos/" + str(p) + ".jpg")
        print(image_path)
        c.drawImage(image_path, 10 + posx, 670 - posy, width=180, height=113)
        if p ==10:
            break
    c.save()
        

"""
    for i in range(3):
        posx = (i * 190) + 10
        #posy = (560 / i ) - 5
        c.rect(4 + posx, 560, 190, 280, stroke=1, fill=0) 
        image_path = os.path.join(os.getcwd(), "fotos/" + str(i+1) + ".jpg")
        print(image_path)
        c.drawImage(image_path, 10 + posx, 670, width=180, height=113)
"""        
    #image_path = os.getcwd() + "fotos/12.jpg"
    #print(image_path)
    #c.drawImage(image_path, 130, 350)
"""
    a = 0 
    for i in l:
        c.drawString(10, 800 + a, i["nom"])
        a = a - 20
    #image_path = os.path.join(os.getcwd(), "/fotos/12.jpg")
    """
    
    

def creaPdf(l,w,h):
    c = canvas.Canvas("content_pdf.pdf", pagesize=A4)
    c.setFillColor(colors.grey)
    c.setFont("Helvetica-Bold", 24)
    
    #c.drawString(50, 700, "Creating PDFs with Python")
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 14)
    c.drawString(10,800, l[0]["nom"])
    c.drawString(0,0, "+ (0,0)")
    c.drawString(10,0, "+ (10,0)")
    c.drawString(20,0, "+ (20,0)")
    c.drawString(100,0, "+ (100,0)")
    c.drawString(200,0, "+ (200,0)")
    
    c.drawString(0,100, "+ (0,100)")
    c.drawString(10,200, "+ (10,200)")
    c.drawString(400,500, "+ (400,500)")
    c.drawString(500,800, "+ (500,800)")
    c.drawString(200,0, "+ (200,0)")
    
    
    #image_path = os.getcwd() + "fotos/12.jpg"
    #print(image_path)
    image_path = os.path.join(os.getcwd(), "fotos/1.jpg")
    print(image_path)
    #c.drawImage(image_path, 50, 400, width=int(w), height=int(h))
    c.drawImage(image_path, 10, 850)

    """
    a = 0 
    for i in l:
        c.drawString(10, 800 + a, i["nom"])
        a = a - 20
    #image_path = os.path.join(os.getcwd(), "/fotos/12.jpg")
    """
    
    c.save()

def imprimeixrespecie(l):
    i = int(input("Escriu la posició: "))
    element = l['records'][i-1]
    #nomcientific = 
    return str("Espècie posició " + str(i) + " és " + element["nom"] + ", científic: ")


def getRandom(l):
    especie = l['records'][random.randint(0, 92)]
    return especie["nom"]

def llistatTots(l):
    for i in l['records']:
        print (i["codi"], ":",i["nom"], ", ", i["cientific"])

def comprova(a,b):
    #retorna true si fan cadena
    if (a["h1"]==b["h1"]):
        if a["h1"]!="no.gif":
            return True
    if (a["h1"]==b["h2"]):
        if a["h1"]!="no.gif":
            return True
    if (a["h1"]==b["h3"]):
        if a["h1"]!="no.gif":
            return True
    if (a["h2"]=="no.gif"):
        return False
    if (a["h2"]==b["h1"]):
        if a["h2"]!="no.gif":
            return True
    if (a["h2"]==b["h2"]):
        if a["h2"]!="no.gif":
            return True
    if (a["h2"]==b["h3"]):
        if a["h2"]!="no.gif":
            return True
    if (a["h3"]=="no.gif"):
        return False
    if (a["h3"]=="no.gif"):
        return False
    if (a["h3"]==b["h1"]):
        if a["h3"]!="no.gif":
            return True
    if (a["h3"]==b["h2"]):
        if a["h3"]!="no.gif":
            return True
    if (a["h3"]==b["h3"]):
        if a["h3"]!="no.gif":
            return True
    return False

def convertTuple(tup):
        # initialize an empty string
    s = ''
    for item in tup:
        
        s = s + str(item)
    s = s + "\n"
    return s

def ferCadenes(l):
    #feim cinc llistes
    print("SOM A CALCULAR CADENES")
    l1=[] 
    for i in l:
        if (i["nivell"]=="0"):
            l1.append(i)
    l2=[]
    for i in l:
        if (i["nivell"]=="1"):
            l2.append(i)
    l3=[]
    for i in l:
        if (i["nivell"]=="2"):
            l3.append(i)
    l4=[]
    for i in l:
        if (i["nivell"]=="3"):
            l4.append(i)
    l5=[]
    for i in l:
        if (i["nivell"]=="4"):
            l5.append(i)
    
    print(tabulate(l1))
    print(tabulate(l2))
    print(tabulate(l3))
    print(tabulate(l4))
    print(tabulate(l5))

    mi_path = "cadenes.txt"
    f = open(mi_path, 'a+')

        

    codiCadena=0
    cadenes=[]
    for i in l1:
        for j in l2:
            for k in l3:
                for m in l4:
                    for n in l5:
                        if comprova(i,j) and comprova(j,k) and comprova(k,m) and comprova(m,n):
                        #if i["h1"]==j["h1"]==k["h1"]==m["h1"]==n["h1"]:
                            codiCadena +=1
                            cadena = "codi ",codiCadena,":",i["nom"],"-",j["nom"],"-",k["nom"],"-",m["nom"],"-",n["nom"]
                            cadenes.append(cadena)
                            f.write(convertTuple(cadena))
                            
    f.close()

    #print(tabulate(cadenes))
    

def mostraOpcions():
    print ("-----------------------------")
    print ("0: Surt del programa")
    print ("1: Element a triar")
    print ("2: Consumeix dades")
    print ("3: llista totes les dades")
    print ("4: Cerca una espècie")
    print ("5: Crea Pdf")
    print ("6: Calcula aparicions")
    print ("-----------------------------")
    return int(input("Inserta el valor:"))



def neteja(llista,elementsBorrar):
    #neteja els camps elementsBorrar
    #de la llista 
    for i in llista:
        for j in elementsBorrar:
            del i[j]

def calculaAparicions():
    #demanam els camps que volem que surtin
    #llistaBreuDict=dict(llistaBreu)
    print("Tria els camps a cercar")
    print(llistaBreu.jsonToPython['nom'])
    #print(llistaBreuDict.keys())

def mostraLlistaBrut():
    print(llistaBreu)

"""
def convertirJsonDiccionari(l):
    with open('data.json') as json_file:
        data = json.load(json_file)
    
        # Print the type of data variable
        print("Type:", type(data))
"""

#DADES ESTRUCTURA DEL PROGRAMA
llista=[]
llistaBreu=dict(llista)
llista = consumeix()
llistaBreu = llista["records"]
neteja(llistaBreu,["imatge","poema","info"])
creaPdf2(llistaBreu)

opcio=-1
#PROGRAMA PRINCIPAL
while opcio!=0:
    if opcio==1:
        print(imprimeixrespecie(llista))
    if opcio==2:
        llista= consumeix()
    if opcio==3:
        llistaBreu= llista["records"]
        neteja(llistaBreu,["imatge","poema","info"])
        print(tabulate(llistaBreu))
    if opcio==4:
        print("ha de mostrar un missatge on demana quin element es vol cercar")
    if opcio==5:
        w=input("dona weight")
        h=input("dona height")
        creaPdf(llista["records"],w,h)
    if opcio==6:
        calculaAparicions()
    if opcio==7:
        mostraLlistaBrut()
    if opcio==8:
        ferCadenes(llistaBreu)
    
    opcio = mostraOpcions()
