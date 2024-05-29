import random

class Animal:
    #classe que insytancia un animal. 
    def __init__(self, nom, edat):
        print (f"He creat un animal {nom},{edat}")
        self.nom = nom
        self.edat = edat
        self.posicio = 0

    def mou(self,x):
        self.posicio += x
        print(f'{self.nom} és a la posició {self.posicio}')

    def mostraPosicio(self):
        print(f"L'animal {self.nom} és a la posició {self.posicio}")

animal1 = Animal("Pere",24)
animal2 = Animal("Pep",67)

print("la posicio de animal1 és: ",animal1.posicio)
animal1.mou(random.randint(1,6))
print("la posicio de animal1 és: ", animal1.posicio)

print("la posicio de animal2 és: ",animal2.posicio)
animal2.mou(random.randint(1,6))
print("la posicio de animal2 és: ", animal2.posicio)

for i in range(10):
    animal1.mou(random.randint(1,6))
    animal2.mou(random.randint(1,6))
    


