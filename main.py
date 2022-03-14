import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Cria a tela do jogo
screen = Screen()
screen.setup(width=600, height=600)

# Desliga as atualizações automáticas da tela
screen.tracer(0)

# Cria um jogador
player = Player()

# Cria um controlador de carros
car_manager = CarManager()

# Cria um Scoreboard
scoreboard = Scoreboard() 

# Controla os botões do jogo
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    # Seta um tempo de pausa
    time.sleep(0.1)
    # Atualiza a tela
    screen.update()

    # Cria um carro
    car_manager.create_cars()

    # Movimenta os carros
    car_manager.move_cars()

    # Detecta colisão da tartaruga com os carros
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detecta a travessia completa e envia o player pro início
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update_scoreboard()

# Evita que a tela se feche após a execução. Ela se fechará com um clique
screen.exitonclick()