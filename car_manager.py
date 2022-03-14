from turtle import Turtle, color
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        
        if random_chance == 1:
            # Cria um novo carro
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))

            # O posiciona adequadamente em local aleatório do eixo y
            random_y = random.randint(-250, 250)
            new_car.goto(320, random_y)

            # O insere dentro da lista
            self.all_cars.append(new_car)

    # Movimenta todos os carros da lista
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    # Sobe o nível do jogo aumentando a velocidade dos carros
    def level_up(self):
        self.car_speed += MOVE_INCREMENT