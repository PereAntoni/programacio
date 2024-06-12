import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Simulació de carrera d'animals"

# Constants per als animals
ANIMAL_COUNT = 5
ANIMAL_SPEED_MIN = 1
ANIMAL_SPEED_MAX = 3

class Animal:
    def __init__(self, image, start_x, start_y):
        self.texture = arcade.load_texture(image)
        self.x = start_x
        self.y = start_y
        self.width= 100  
        self.height= 100


        self.imatge=image
        
        self.speed = random.randint(ANIMAL_SPEED_MIN, ANIMAL_SPEED_MAX)
        

    def setSpeed(self):
        self.speed = random.randint(ANIMAL_SPEED_MIN, ANIMAL_SPEED_MAX)

    def update(self):
        self.x += self.speed

    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y, self.width, self.height, self.texture)
    
    def combina(altre):
        pass

class Milana(Animal):
    def __init__(self, image, start_x, start_y):
        super().__init__(image, start_x, start_y)
        self.texture = arcade.load_texture("Red_Kite8-500.jpg")

    def setSpeed(self):
        self.speed = random.randint(2, 8)

     

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.winner = 0
        self.animals = []
        start_y = 100
        for i in range(ANIMAL_COUNT):
            #CREAM ELS DIFERENTS ANIMALS
            imatgeAnimal = "animal" + str(i) + ".png"
            if i == 2:
                animal = Milana(imatgeAnimal, 50, start_y)
            
            elif i==3:
                animal = Tortuga(imatgeAnimal, 50, start_y)
            
            elif i==4:
                animal = Serp(imatgeAnimal, 50, start_y)

            else:
                animal = Animal(imatgeAnimal, 50, start_y)
            self.animals.append(animal)
            start_y += 100
        

    def on_draw(self):
        arcade.start_render()
        for animal in self.animals:
            animal.draw()

    def update(self, delta_time):
        for animal in self.animals:
            animal.setSpeed()
            animal.update()
            if animal.x > SCREEN_WIDTH:
                if self.winner ==0:
                    print("ha arribat",animal.imatge)
                    self.winner = 1
                animal.x = SCREEN_WIDTH

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    #COMENÇA LA PROGRAMACIÓ DEL PROGRAMA
    arcade.run()

if __name__ == "__main__":
    main()
