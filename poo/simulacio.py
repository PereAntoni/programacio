import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Simulació de carrera d'animals"

# Constants per als animals
ANIMAL_COUNT = 5
ANIMAL_SPEED_MIN = 1
ANIMAL_SPEED_MAX = 5

class Animal:
    def __init__(self, image, start_x, start_y):
        self.texture = arcade.load_texture(image)
        self.x = start_x
        self.y = start_y
        self.speed = random.randint(ANIMAL_SPEED_MIN, ANIMAL_SPEED_MAX)
        #self.texture.width = 100
        #self.texture.height = 100
        

    def update(self):
        self.x += self.speed

    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y, self.texture.width, self.texture.height, self.texture)
        #arcade.draw_texture_rectangle(self.x, self.y, 100, 100, self.texture)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

        self.animals = []
        start_y = 100
        for i in range(ANIMAL_COUNT):
            animal = Animal("animal.png", 50, start_y)
            self.animals.append(animal)
            start_y += 100

    def on_draw(self):
        arcade.start_render()
        for animal in self.animals:
            animal.draw()

    def update(self, delta_time):
        for animal in self.animals:
            animal.update()
            if animal.x > SCREEN_WIDTH:
                animal.x = SCREEN_WIDTH

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
