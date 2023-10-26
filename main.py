from pygame.color import THECOLORS
from classes import *
from send_data import SendData
from read_data import ReadData
import pygame, sys, random, matplotlib.pyplot as plt, numpy as np

pygame.init()

screen = pygame.display.set_mode((1300, 950))
screen.fill(THECOLORS["grey"])

topic_font = pygame.font.SysFont("Arial", 50)
text_font = pygame.font.SysFont("Arial", 30)
square_font = pygame.font.SysFont("Arial", 20)
font = pygame.font.SysFont("Arial", 30)

player_piece_group = pygame.sprite.Group()
ladder_group = pygame.sprite.Group()
snake_group = pygame.sprite.Group()
dice_group = pygame.sprite.Group()

game_on = True
simulation_on = False
first_player_move = True
second_player_move = False
is_moving = False
window_changed = False
hypothesis_testing_on = False

current_interface = "Start Interface"
current_player = "Player1"
current_game_mode = ""
winner = ""

player1_turns_quantity = 0
player2_turns_quantity = 0

player1_wins_quantity = 0
player2_wins_quantity = 0

game_data_dict = {"Total dice throws": 0,
                  "Quantity of received 1": 0,
                  "Quantity of received 2": 0,
                  "Quantity of received 3": 0,
                  "Quantity of received 4": 0,
                  "Quantity of received 5": 0,
                  "Quantity of received 6": 0,
                  "Quantity of received 7-12": 0,
                  "Ladders used": 0,
                  "Snakes used": 0
                  }

def NumberGottenChecker(number_of_steps):
    if not hypothesis_testing_on:
        if number_of_steps == 1:
            game_data_dict["Quantity of received 1"] += 1
        elif number_of_steps == 2:
            game_data_dict["Quantity of received 2"] += 1
        elif number_of_steps == 3:
            game_data_dict["Quantity of received 3"] += 1
        elif number_of_steps == 4:
            game_data_dict["Quantity of received 4"] += 1
        elif number_of_steps == 5:
            game_data_dict["Quantity of received 5"] += 1
        elif number_of_steps == 6:
            game_data_dict["Quantity of received 6"] += 1
        else:
            game_data_dict["Quantity of received 7-12"] += 1
    else:
        if number_of_steps == 1:
            hypothesis_game_data_dict["Quantity of received 1"] += 1
        elif number_of_steps == 2:
            hypothesis_game_data_dict["Quantity of received 2"] += 1
        elif number_of_steps == 3:
            hypothesis_game_data_dict["Quantity of received 3"] += 1
        elif number_of_steps == 4:
            hypothesis_game_data_dict["Quantity of received 4"] += 1
        elif number_of_steps == 5:
            hypothesis_game_data_dict["Quantity of received 5"] += 1
        elif number_of_steps == 6:
            hypothesis_game_data_dict["Quantity of received 6"] += 1
        else:
            hypothesis_game_data_dict["Quantity of received 7-12"] += 1

def SteppedOnTheLadderChecker():
    global player_current_square1, player_current_square2, first_player_move, second_player_move, first_player_piece_posx, first_player_piece_posy, second_player_piece_posx, second_player_piece_posy, player_current_raw1, player_current_raw2

    if player_current_square1 in [2, 4, 8, 21, 28, 50, 71, 80] or player_current_square2 in [2, 4, 8, 21, 28, 50, 71,
                                                                                             80]:
        if first_player_move:
            if player_current_square1 % 2 == 0:
                screen.fill((150, 0, 0), (first_player_piece_posx - 15, first_player_piece_posy - 20, 30, 40))
            else:
                screen.fill((0, 150, 0), (first_player_piece_posx - 15, first_player_piece_posy - 20, 30, 40))

            if player_current_square1 == 2:
                first_player_piece_posx += 80
                first_player_piece_posy -= 240
                player_current_square1 = 38
                player_current_raw1 = 4
            elif player_current_square1 == 4:
                first_player_piece_posx += 240
                first_player_piece_posy -= 80
                player_current_square1 = 14
                player_current_raw1 = 2
            elif player_current_square1 == 8:
                first_player_piece_posx += 160
                first_player_piece_posy -= 160
                player_current_square1 = 30
                player_current_raw1 = 3
            elif player_current_square1 == 21:
                first_player_piece_posx += 80
                first_player_piece_posy -= 160
                player_current_square1 = 42
                player_current_raw1 = 5
            elif player_current_square1 == 28:
                first_player_piece_posx -= 240
                first_player_piece_posy -= 400
                player_current_square1 = 76
                player_current_raw1 = 8
            elif player_current_square1 == 50:
                first_player_piece_posx -= 240
                first_player_piece_posy -= 160
                player_current_square1 = 67
                player_current_raw1 = 7
            elif player_current_square1 == 71:
                first_player_piece_posx -= 80
                first_player_piece_posy -= 160
                player_current_square1 = 92
                player_current_raw1 = 10
            elif player_current_square1 == 80:
                first_player_piece_posx += 80
                first_player_piece_posy -= 160
                player_current_square1 = 99
                player_current_raw1 = 10

        elif second_player_move:
            if player_current_square2 % 2 == 0:
                screen.fill((150, 0, 0), (second_player_piece_posx - 15, second_player_piece_posy - 20, 30, 40))
            else:
                screen.fill((0, 150, 0), (second_player_piece_posx - 15, second_player_piece_posy - 20, 30, 40))

            if player_current_square2 == 2:
                second_player_piece_posx += 80
                second_player_piece_posy -= 240
                player_current_square2 = 38
                player_current_raw2 = 4
            elif player_current_square2 == 4:
                second_player_piece_posx += 240
                second_player_piece_posy -= 80
                player_current_square2 = 14
                player_current_raw2 = 2
            elif player_current_square2 == 8:
                second_player_piece_posx += 160
                second_player_piece_posy -= 160
                player_current_square2 = 30
                player_current_raw2 = 3
            elif player_current_square2 == 21:
                second_player_piece_posx += 80
                second_player_piece_posy -= 160
                player_current_square2 = 42
                player_current_raw2 = 5
            elif player_current_square2 == 28:
                second_player_piece_posx -= 240
                second_player_piece_posy -= 400
                player_current_square2 = 76
                player_current_raw2 = 8
            elif player_current_square2 == 50:
                second_player_piece_posx -= 240
                second_player_piece_posy -= 160
                player_current_square2 = 67
                player_current_raw2 = 7
            elif player_current_square2 == 71:
                second_player_piece_posx -= 80
                second_player_piece_posy -= 160
                player_current_square2 = 92
                player_current_raw2 = 10
            elif player_current_square2 == 80:
                second_player_piece_posx += 80
                second_player_piece_posy -= 160
                player_current_square2 = 99
                player_current_raw2 = 10

        if not hypothesis_testing_on:
            game_data_dict["Ladders used"] += 1
        else:
            hypothesis_game_data_dict["Ladders used"] += 1

        player_piece1.update(first_player_piece_posx, first_player_piece_posy)
        player_piece2.update(second_player_piece_posx, second_player_piece_posy)
        ladder_group.draw(screen)
        snake_group.draw(screen)
        player_piece_group.draw(screen)
        pygame.display.update()

def SteppedOnTheSnakeChecker():
    global player_current_square1, player_current_square2, first_player_move, second_player_move, first_player_piece_posx, first_player_piece_posy, second_player_piece_posx, second_player_piece_posy, player_current_raw1, player_current_raw2

    if player_current_square1 in [32, 36, 48, 62, 88, 95, 97] or player_current_square2 in [32, 36, 48, 62, 88, 95, 97]:
        if first_player_move:
            if player_current_square1 % 2 == 0:
                screen.fill((150, 0, 0), (first_player_piece_posx - 15, first_player_piece_posy - 20, 30, 40))
            else:
                screen.fill((0, 150, 0), (first_player_piece_posx - 15, first_player_piece_posy - 20, 30, 40))

            if player_current_square1 == 32:
                first_player_piece_posx += 80
                first_player_piece_posy += 240
                player_current_square1 = 10
                player_current_raw1 = 1
            elif player_current_square1 == 36:
                first_player_piece_posx += 80
                first_player_piece_posy += 240
                player_current_square1 = 6
                player_current_raw1 = 1
            elif player_current_square1 == 48:
                first_player_piece_posx -= 160
                first_player_piece_posy += 160
                player_current_square1 = 26
                player_current_raw1 = 3
            elif player_current_square1 == 62:
                first_player_piece_posx += 80
                first_player_piece_posy += 400
                player_current_square1 = 18
                player_current_raw1 = 2
            elif player_current_square1 == 88:
                first_player_piece_posx -= 320
                first_player_piece_posy += 480
                player_current_square1 = 24
                player_current_raw1 = 3
            elif player_current_square1 == 95:
                first_player_piece_posx -= 80
                first_player_piece_posy += 320
                player_current_square1 = 56
                player_current_raw1 = 6
            elif player_current_square1 == 97:
                first_player_piece_posx -= 80
                first_player_piece_posy += 160
                player_current_square1 = 78
                player_current_raw1 = 8

        elif second_player_move:
            if player_current_square2 % 2 == 0:
                screen.fill((150, 0, 0), (second_player_piece_posx - 15, second_player_piece_posy - 20, 30, 40))
            else:
                screen.fill((0, 150, 0), (second_player_piece_posx - 15, second_player_piece_posy - 20, 30, 40))

            if player_current_square2 == 32:
                second_player_piece_posx += 80
                second_player_piece_posy += 240
                player_current_square2 = 10
                player_current_raw2 = 1
            elif player_current_square2 == 36:
                second_player_piece_posx += 80
                second_player_piece_posy += 240
                player_current_square2 = 6
                player_current_raw2 = 1
            elif player_current_square2 == 48:
                second_player_piece_posx -= 160
                second_player_piece_posy += 160
                player_current_square2 = 26
                player_current_raw2 = 3
            elif player_current_square2 == 62:
                second_player_piece_posx += 80
                second_player_piece_posy += 400
                player_current_square2 = 18
                player_current_raw2 = 2
            elif player_current_square2 == 88:
                second_player_piece_posx -= 320
                second_player_piece_posy += 480
                player_current_square2 = 24
                player_current_raw2 = 3
            elif player_current_square2 == 95:
                second_player_piece_posx -= 80
                second_player_piece_posy += 320
                player_current_square2 = 56
                player_current_raw2 = 6
            elif player_current_square2 == 97:
                second_player_piece_posx -= 80
                second_player_piece_posy += 160
                player_current_square2 = 78
                player_current_raw2 = 8

        if not hypothesis_testing_on:
            game_data_dict["Snakes used"] += 1
        else:
            hypothesis_game_data_dict["Snakes used"] += 1

        player_piece1.update(first_player_piece_posx, first_player_piece_posy)
        player_piece2.update(second_player_piece_posx, second_player_piece_posy)
        ladder_group.draw(screen)
        snake_group.draw(screen)
        player_piece_group.draw(screen)
        pygame.display.update()

def ShowGraph():
    if current_game_mode == "Simulation":
        titles = ["% of ladders used", "% of snakes used", "% of getting 1", "% of getting 2", "% of getting 3",
                  "% of getting 4", "% of getting 5", "% of getting 6"]
        values = []

        values.append((game_data_dict["Ladders used"] / game_data_dict["Total dice throws"]) * 100)
        values.append((game_data_dict["Snakes used"] / game_data_dict["Total dice throws"]) * 100)
        values.append((game_data_dict["Quantity of received 1"] / game_data_dict["Total dice throws"]) * 100)
        values.append((game_data_dict["Quantity of received 2"] / game_data_dict["Total dice throws"]) * 100)
        values.append((game_data_dict["Quantity of received 3"] / game_data_dict["Total dice throws"]) * 100)
        values.append((game_data_dict["Quantity of received 4"] / game_data_dict["Total dice throws"]) * 100)
        values.append((game_data_dict["Quantity of received 5"] / game_data_dict["Total dice throws"]) * 100)
        values.append((game_data_dict["Quantity of received 6"] / game_data_dict["Total dice throws"]) * 100)

        plt.figure(figsize=(15, 5))

        plt.bar(titles, values, width=0.4)
        plt.xlabel("Data")
        plt.ylabel("Percentage")
        plt.title("Game Data")
        plt.show()
    elif current_game_mode == "Hypothesis Testing":
        titles = ["% of ladders used", "% of snakes used", "% of getting 1", "% of getting 2", "% of getting 3",
                  "% of getting 4", "% of getting 5", "% of getting 6", "% of getting 7-12"]
        values = []
        hypothesis_values = []

        values.append((game_data_dict["Ladders used"] / game_data_dict["Total dice throws"]) * 100)
        values.append((game_data_dict["Snakes used"] / game_data_dict["Total dice throws"]) * 100)
        values.append((game_data_dict["Quantity of received 1"] / game_data_dict["Total dice throws"]) * 100)
        values.append((game_data_dict["Quantity of received 2"] / game_data_dict["Total dice throws"]) * 100)
        values.append((game_data_dict["Quantity of received 3"] / game_data_dict["Total dice throws"]) * 100)
        values.append((game_data_dict["Quantity of received 4"] / game_data_dict["Total dice throws"]) * 100)
        values.append((game_data_dict["Quantity of received 5"] / game_data_dict["Total dice throws"]) * 100)
        values.append((game_data_dict["Quantity of received 6"] / game_data_dict["Total dice throws"]) * 100)
        values.append((game_data_dict["Quantity of received 7-12"] / game_data_dict["Total dice throws"]) * 100)

        hypothesis_values.append((hypothesis_game_data_dict["Ladders used"] / hypothesis_game_data_dict["Total dice throws"]) * 100)
        hypothesis_values.append((hypothesis_game_data_dict["Snakes used"] / hypothesis_game_data_dict["Total dice throws"]) * 100)
        hypothesis_values.append((hypothesis_game_data_dict["Quantity of received 1"] / hypothesis_game_data_dict["Total dice throws"]) * 100)
        hypothesis_values.append((hypothesis_game_data_dict["Quantity of received 2"] / hypothesis_game_data_dict["Total dice throws"]) * 100)
        hypothesis_values.append((hypothesis_game_data_dict["Quantity of received 3"] / hypothesis_game_data_dict["Total dice throws"]) * 100)
        hypothesis_values.append((hypothesis_game_data_dict["Quantity of received 4"] / hypothesis_game_data_dict["Total dice throws"]) * 100)
        hypothesis_values.append((hypothesis_game_data_dict["Quantity of received 5"] / hypothesis_game_data_dict["Total dice throws"]) * 100)
        hypothesis_values.append((hypothesis_game_data_dict["Quantity of received 6"] / hypothesis_game_data_dict["Total dice throws"]) * 100)
        hypothesis_values.append((hypothesis_game_data_dict["Quantity of received 7-12"] / hypothesis_game_data_dict["Total dice throws"]) * 100)

        x_axis = np.arange(len(titles))
        plt.figure(figsize=(17, 5))
        plt.bar(x_axis - 0.2, values, 0.4, label='Normal Game: One dice')
        plt.bar(x_axis + 0.2, hypothesis_values, 0.4, label='Hypothesis Game: Two dices')
        plt.xticks(x_axis, titles)
        plt.xlabel("Data")
        plt.ylabel("Percentage")
        plt.title("Game Data")
        plt.legend()
        plt.show()

def StartInterface():
    topic = topic_font.render("Choose Game Mode", True, THECOLORS["black"])
    screen.blit(topic, (450, 100))

    single_player_icon = pygame.image.load("images/single_player_icon.png")
    single_player_icon = pygame.transform.scale(single_player_icon, (200, 200))
    screen.blit(single_player_icon, (250, 300))
    single_player_text = text_font.render("Single Player", True, THECOLORS["black"])
    screen.blit(single_player_text, (280, 500))

    multiplayer_icon = pygame.image.load("images/multiplayer_icon.png")
    multiplayer_icon = pygame.transform.scale(multiplayer_icon, (200, 200))
    screen.blit(multiplayer_icon, (550, 300))
    multiplayer_text = text_font.render("Multiplayer", True, THECOLORS["black"])
    screen.blit(multiplayer_text, (595, 500))

    simulation_icon = pygame.image.load("images/simulation_icon.png")
    simulation_icon = pygame.transform.scale(simulation_icon, (200, 200))
    screen.blit(simulation_icon, (850, 300))
    simulation_text = text_font.render("Simulation", True, THECOLORS["black"])
    screen.blit(simulation_text, (895, 500))

    hypothesis_testing_icon = pygame.image.load("images/hypothesis_testing_icon.png")
    hypothesis_testing_icon = pygame.transform.scale(hypothesis_testing_icon, (200, 200))
    screen.blit(hypothesis_testing_icon, (550, 600))
    hypothesis_testing_icon = text_font.render("Hypothesis Testing", True, THECOLORS["black"])
    screen.blit(hypothesis_testing_icon, (545, 800))

def SimulationInterface():
    topic = topic_font.render("Choose how many times you want to run the simulation", True,
                              THECOLORS["black"])
    screen.blit(topic, (150, 300))

    one_time_icon = pygame.image.load("images/1_icon.png")
    one_time_icon = pygame.transform.scale(one_time_icon, (100, 100))
    screen.blit(one_time_icon, (200, 500))

    two_times_icon = pygame.image.load("images/2_icon.png")
    two_times_icon = pygame.transform.scale(two_times_icon, (100, 100))
    screen.blit(two_times_icon, (400, 500))

    three_times_icon = pygame.image.load("images/3_icon.png")
    three_times_icon = pygame.transform.scale(three_times_icon, (100, 100))
    screen.blit(three_times_icon, (600, 500))

    four_times_icon = pygame.image.load("images/4_icon.png")
    four_times_icon = pygame.transform.scale(four_times_icon, (100, 100))
    screen.blit(four_times_icon, (800, 500))

    five_times_icon = pygame.image.load("images/5_icon.png")
    five_times_icon = pygame.transform.scale(five_times_icon, (100, 100))
    screen.blit(five_times_icon, (1000, 500))

def GameInerface():
    global dice, player_piece1, player_piece2, start_game, first_player_piece_posx, first_player_piece_posy, second_player_piece_posx, second_player_piece_posy, test_rect, player_current_square1, player_current_square2, player_current_raw1, player_current_raw2

    screen.fill(THECOLORS["grey"])

    dice = Dice(150, 150, 1080, 800, 0)
    dice_group.add(dice)
    dice_group.draw(screen)

    dice_text = text_font.render(f"{current_player} click the dice", True, THECOLORS["black"])
    screen.blit(dice_text, (975, 880))

    player1_wins_text = text_font.render(f"Player1 wins: {player1_wins_quantity}", True, THECOLORS["black"])
    screen.blit(player1_wins_text, (940, 80))

    player2_wins_text = text_font.render(f"Player2 wins: {player2_wins_quantity}", True, THECOLORS["black"])
    screen.blit(player2_wins_text, (940, 130))

    r = pygame.Rect(0, 0, 80, 80)

    rect_num = 100
    color = 100

    start_game = True

    player_current_square1 = 1
    player_current_square2 = 1
    player_current_raw1 = 1
    player_current_raw2 = 1

    for i in range(10):
        r.y += 80
        if i % 2 == 0:
            r.x = 0
        else:
            r.x += 80
        for j in range(10):
            if i % 2 == 0:
                r.x += 80
            else:
                r.x -= 80
            color -= 1
            if color % 2 == 0:
                pygame.draw.rect(screen, (0, 150, 0), r, 0)
            else:
                pygame.draw.rect(screen, (150, 0, 0), r, 0)
            number_of_rect = square_font.render(str(rect_num), True, THECOLORS["black"])
            screen.blit(number_of_rect, (r.x, r.y))
            rect_num -= 1

    first_player_piece_posx = r.x + 25
    first_player_piece_posy = r.y + 40
    second_player_piece_posx = r.x + 55
    second_player_piece_posy = r.y + 40

    player_piece1 = PlayerPiece(first_player_piece_posx, first_player_piece_posy, "images/player_piece1.png")
    player_piece2 = PlayerPiece(second_player_piece_posx, second_player_piece_posy, "images/player_piece2.png")
    player_piece_group.add(player_piece1)
    player_piece_group.add(player_piece2)

    ladder1 = Ladder(40, 200, 150, 200, -30)
    ladder_group.add(ladder1)

    ladder2 = Ladder(40, 200, 800, 200, 30)
    ladder_group.add(ladder2)

    ladder3 = Ladder(40, 280, 720, 450, 50)
    ladder_group.add(ladder3)

    ladder4 = Ladder(40, 450, 550, 480, 30)
    ladder_group.add(ladder4)

    ladder5 = Ladder(40, 200, 150, 600, -30)
    ladder_group.add(ladder5)

    ladder6 = Ladder(40, 280, 250, 710, -20)
    ladder_group.add(ladder6)

    ladder6 = Ladder(40, 280, 480, 800, -70)
    ladder_group.add(ladder6)

    ladder6 = Ladder(40, 250, 750, 770, -40)
    ladder_group.add(ladder6)

    snake1 = Snake(100, 150, 320, 200, 10)
    snake_group.add(snake1)

    snake2 = Snake(200, 300, 490, 280, 20)
    snake_group.add(snake2)

    snake3 = Snake(250, 350, 240, 560, 50)
    snake_group.add(snake3)

    snake4 = Snake(250, 520, 520, 430, -10)
    snake_group.add(snake4)

    snake5 = Snake(150, 250, 480, 720, 50)
    snake_group.add(snake5)

    snake6 = Snake(100, 180, 600, 600, -10)
    snake_group.add(snake6)

    snake7 = Snake(150, 250, 800, 720, 50)
    snake_group.add(snake7)

    ladder_group.draw(screen)
    snake_group.draw(screen)
    player_piece_group.draw(screen)

def WinnerInterface(winner):
    global current_interface

    screen.fill(THECOLORS["grey"])

    if current_game_mode == "Simulation":
        text = text_font.render(f"Simulation ended", True, THECOLORS["black"])
        screen.blit(text, (570, 350))
    elif current_game_mode == "Hypothesis Testing":
        text = text_font.render(f"Hypothesis Testing ended", True, THECOLORS["black"])
        screen.blit(text, (530, 350))
    else:
        winner_text = text_font.render(f"Winner is {winner}", True, THECOLORS["black"])
        screen.blit(winner_text, (550, 350))

    home_page_icon = pygame.image.load("images/home_page_icon.png")
    home_page_icon = pygame.transform.scale(home_page_icon, (200, 200))
    screen.blit(home_page_icon, (350, 450))

    home_page_text = text_font.render(f"Home page", True, THECOLORS["black"])
    screen.blit(home_page_text, (385, 670))

    play_again_icon = pygame.image.load("images/play_again_icon.png")
    play_again_icon = pygame.transform.scale(play_again_icon, (200, 200))
    screen.blit(play_again_icon, (750, 450))

    play_again_text = text_font.render(f"Play again", True, THECOLORS["black"])
    screen.blit(play_again_text, (795, 670))

    current_interface = "Winner Interface"

    ShowGraph()

def FirstPlayerPieceMove():
    global player1_wins_quantity, game_quantity, player1_turns_quantity, current_player, \
        current_interface, winner, game_on, first_player_move, second_player_move, player_piece1,\
        first_player_piece_posx, first_player_piece_posy, \
        player_current_square1, player_current_raw1

    if not hypothesis_testing_on:
        number_of_steps = random.randint(1, 6)
        NumberGottenChecker(number_of_steps)
    else:
        number_of_steps = random.randint(1, 6) + random.randint(1, 6)
        NumberGottenChecker(number_of_steps)

    player1_turns_quantity += 1

    current_player = "Player1"
    screen.fill(THECOLORS["grey"], (970, 650, 250, 50))
    number_of_steps_text = font.render(f"{current_player} Turn: {number_of_steps} steps", True, THECOLORS["black"])
    screen.blit(number_of_steps_text, (970, 650))

    screen.fill(THECOLORS["grey"], (970, 880, 250, 50))
    dice_text = text_font.render("Player2 click the dice", True, THECOLORS["black"])
    screen.blit(dice_text, (975, 880))

    for i in range(number_of_steps):
        if player_current_square1 != 100:
            if player_current_square1 % 2 == 0:
                screen.fill((150, 0, 0), (first_player_piece_posx - 15, first_player_piece_posy - 20, 30, 40))
            else:
                screen.fill((0, 150, 0), (first_player_piece_posx - 15, first_player_piece_posy - 20, 30, 40))

            if player_current_square1 % 10 != 0:
                if player_current_raw1 % 2 != 0:
                    first_player_piece_posx += 80
                else:
                    first_player_piece_posx -= 80
            else:
                first_player_piece_posy -= 80
                player_current_raw1 += 1

            player_piece1.update(first_player_piece_posx, first_player_piece_posy)
            player_piece2.update(second_player_piece_posx, second_player_piece_posy)
            ladder_group.draw(screen)
            snake_group.draw(screen)
            player_piece_group.draw(screen)
            pygame.display.update()
            pygame.time.delay(100)
            player_current_square1 += 1

            if player_current_square1 == 100:
                game_on = False
                winner = "Player 1"
                player1_wins_quantity += 1
                break

    SteppedOnTheLadderChecker()
    SteppedOnTheSnakeChecker()

    first_player_move = False
    second_player_move = True

    pygame.event.clear()

def SecondPlayerPieceMove():
    global player2_wins_quantity, game_quantity, player2_turns_quantity, current_player, \
        current_interface, winner, game_on, first_player_move, second_player_move, \
        player_piece2, second_player_piece_posx, second_player_piece_posy, \
        player_current_square2, player_current_raw2

    if not hypothesis_testing_on:
        number_of_steps = random.randint(1, 6)
        NumberGottenChecker(number_of_steps)
    else:
        number_of_steps = random.randint(1, 6) + random.randint(1, 6)
        NumberGottenChecker(number_of_steps)

    player2_turns_quantity += 1

    current_player = "Player2"
    screen.fill(THECOLORS["grey"], (970, 650, 250, 50))
    number_of_steps_text = font.render(f"{current_player} Turn: {number_of_steps} steps", True, THECOLORS["black"])
    screen.blit(number_of_steps_text, (970, 650))

    screen.fill(THECOLORS["grey"], (970, 880, 250, 50))
    dice_text = text_font.render("Player1 click the dice", True, THECOLORS["black"])
    screen.blit(dice_text, (975, 880))

    for i in range(number_of_steps):
        if player_current_square2 != 100:
            if player_current_square2 % 2 == 0:
                screen.fill((150, 0, 0), (second_player_piece_posx - 15, second_player_piece_posy - 20, 30, 40))
            else:
                screen.fill((0, 150, 0), (second_player_piece_posx - 15, second_player_piece_posy - 20, 30, 40))

            if player_current_square2 % 10 != 0:
                if player_current_raw2 % 2 != 0:
                    second_player_piece_posx += 80
                else:
                    second_player_piece_posx -= 80
            else:
                second_player_piece_posy -= 80
                player_current_raw2 += 1

            player_piece1.update(first_player_piece_posx, first_player_piece_posy)
            player_piece2.update(second_player_piece_posx, second_player_piece_posy)
            ladder_group.draw(screen)
            snake_group.draw(screen)
            player_piece_group.draw(screen)
            pygame.display.update()
            pygame.time.delay(100)
            player_current_square2 += 1

            if player_current_square2 == 100:
                game_on = False
                winner = "Player 2"
                player2_wins_quantity += 1
                break

    SteppedOnTheLadderChecker()
    SteppedOnTheSnakeChecker()

    first_player_move = True
    second_player_move = False

    pygame.event.clear()

def PlayerPieceMove():
    global hypothesis_game_data_dict, hypothesis_testing_on, window_changed, is_moving, simulation_on, game_quantity, player1_turns_quantity, player2_turns_quantity, current_player,\
        current_interface, winner, game_on, first_player_move, second_player_move, player_piece1,\
        player_piece2, first_player_piece_posx, first_player_piece_posy, second_player_piece_posx, second_player_piece_posy,\
        player_current_square1, player_current_square2, player_current_raw1, player_current_raw2

    if current_game_mode == "Single Player":
        is_moving = True

        if game_on:
            FirstPlayerPieceMove()
            game_data_dict["Total dice throws"] += 1

        if game_on:
            SecondPlayerPieceMove()
            game_data_dict["Total dice throws"] += 1

        if not game_on:
            SendData(game_data_dict)

            window_changed = True
            WinnerInterface(winner)

    elif current_game_mode == "Multiplayer":
        is_moving = True

        if game_on:
            if first_player_move:
                FirstPlayerPieceMove()
                game_data_dict["Total dice throws"] += 1
            else:
                SecondPlayerPieceMove()
                game_data_dict["Total dice throws"] += 1

        if not game_on:
            SendData(game_data_dict)

            window_changed = True
            WinnerInterface(winner)
    elif current_game_mode == "Simulation":
        is_moving = True
        simulation_on = True

        for i in range(game_quantity):
            GameInerface()

            while game_on:
                FirstPlayerPieceMove()
                game_data_dict["Total dice throws"] += 1
                if game_on:
                    SecondPlayerPieceMove()
                    game_data_dict["Total dice throws"] += 1
                pygame.event.clear()

            player_piece_group.empty()
            ladder_group.empty()
            snake_group.empty()
            dice_group.empty()

            game_on = True
            first_player_move = True
            second_player_move = False

            current_player = "Player1"
            winner = ""

            player1_turns_quantity = 0
            player2_turns_quantity = 0

        simulation_on = False
        window_changed = True
        SendData(game_data_dict)
        WinnerInterface(winner)
    elif current_game_mode == "Hypothesis Testing":
        while game_on:
            FirstPlayerPieceMove()
            game_data_dict["Total dice throws"] += 1
            if game_on:
                SecondPlayerPieceMove()
                game_data_dict["Total dice throws"] += 1
            pygame.event.clear()

        player_piece_group.empty()
        ladder_group.empty()
        snake_group.empty()
        dice_group.empty()

        game_on = True
        first_player_move = True
        second_player_move = False

        current_player = "Player1"
        winner = ""

        player1_turns_quantity = 0
        player2_turns_quantity = 0
        hypothesis_testing_on = True
        GameInerface()

        while game_on:
            FirstPlayerPieceMove()
            hypothesis_game_data_dict["Total dice throws"] += 1
            if game_on:
                SecondPlayerPieceMove()
                hypothesis_game_data_dict["Total dice throws"] += 1
            pygame.event.clear()

        hypothesis_testing_on = False
        window_changed = True
        SendData(hypothesis_game_data_dict)
        WinnerInterface(winner)

    is_moving = False

StartInterface()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if current_interface == "Game Interface":
            if current_game_mode == "Single Player" and event.type == pygame.MOUSEBUTTONDOWN and not is_moving:
                if first_player_move:
                    if pygame.mouse.get_pos()[0] >= 1000 and pygame.mouse.get_pos()[0] <= 1150 and \
                            pygame.mouse.get_pos()[1] >= 700 and pygame.mouse.get_pos()[1] <= 850:
                        PlayerPieceMove()
            elif current_game_mode == "Multiplayer" and event.type == pygame.MOUSEBUTTONDOWN and not is_moving:
                if pygame.mouse.get_pos()[0] >= 1000 and pygame.mouse.get_pos()[0] <= 1150 and pygame.mouse.get_pos()[
                    1] >= 700 and pygame.mouse.get_pos()[1] <= 850:
                    PlayerPieceMove()
            elif current_game_mode == "Simulation" and not simulation_on:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 300 and pygame.mouse.get_pos()[
                        1] >= 500 and pygame.mouse.get_pos()[1] <= 600:
                        game_quantity = 1
                        PlayerPieceMove()
                    elif pygame.mouse.get_pos()[0] >= 400 and pygame.mouse.get_pos()[0] <= 500 and pygame.mouse.get_pos()[
                        1] >= 500 and pygame.mouse.get_pos()[1] <= 600:
                        game_quantity = 2
                        PlayerPieceMove()
                    elif pygame.mouse.get_pos()[0] >= 600 and pygame.mouse.get_pos()[0] <= 700 and pygame.mouse.get_pos()[
                        1] >= 500 and pygame.mouse.get_pos()[1] <= 600:
                        game_quantity = 3
                        PlayerPieceMove()
                    elif pygame.mouse.get_pos()[0] >= 800 and pygame.mouse.get_pos()[0] <= 900 and pygame.mouse.get_pos()[
                        1] >= 500 and pygame.mouse.get_pos()[1] <= 600:
                        game_quantity = 4
                        PlayerPieceMove()
                    elif pygame.mouse.get_pos()[0] >= 1000 and pygame.mouse.get_pos()[0] <= 1100 and pygame.mouse.get_pos()[
                        1] >= 500 and pygame.mouse.get_pos()[1] <= 600:
                        game_quantity = 5
                        PlayerPieceMove()
        if current_interface == "Start Interface" and event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 250 and pygame.mouse.get_pos()[0] <= 450 and pygame.mouse.get_pos()[
                1] >= 300 and pygame.mouse.get_pos()[1] <= 500:
                current_game_mode = "Single Player"
                current_interface = "Game Interface"
                screen.fill(THECOLORS["grey"])
                GameInerface()
            elif pygame.mouse.get_pos()[0] >= 550 and pygame.mouse.get_pos()[0] <= 750 and pygame.mouse.get_pos()[
                1] >= 300 and pygame.mouse.get_pos()[1] <= 500:
                current_game_mode = "Multiplayer"
                current_interface = "Game Interface"
                screen.fill(THECOLORS["grey"])
                GameInerface()
            elif pygame.mouse.get_pos()[0] >= 850 and pygame.mouse.get_pos()[0] <= 1050 and pygame.mouse.get_pos()[
                1] >= 300 and pygame.mouse.get_pos()[1] <= 500:
                current_game_mode = "Simulation"
                current_interface = "Game Interface"
                screen.fill(THECOLORS["grey"])
                SimulationInterface()
            elif pygame.mouse.get_pos()[0] >= 550 and pygame.mouse.get_pos()[0] <= 750 and pygame.mouse.get_pos()[
                1] >= 600 and pygame.mouse.get_pos()[1] <= 800:
                current_game_mode = "Hypothesis Testing"
                current_interface = "Game Interface"
                hypothesis_game_data_dict = {"Total dice throws": 0,
                                             "Quantity of received 1": 0,
                                             "Quantity of received 2": 0,
                                             "Quantity of received 3": 0,
                                             "Quantity of received 4": 0,
                                             "Quantity of received 5": 0,
                                             "Quantity of received 6": 0,
                                             "Quantity of received 7-12": 0,
                                             "Ladders used": 0,
                                             "Snakes used": 0}


                screen.fill(THECOLORS["grey"])
                GameInerface()
                PlayerPieceMove()
        if current_interface == "Winner Interface" and event.type == pygame.MOUSEBUTTONDOWN and not is_moving:
            if not window_changed or current_game_mode == "Hypothesis Testing":
                if pygame.mouse.get_pos()[0] >= 350 and pygame.mouse.get_pos()[0] <= 550 and pygame.mouse.get_pos()[1] >= 450 and pygame.mouse.get_pos()[1] <= 650:
                    player_piece_group.empty()
                    ladder_group.empty()
                    snake_group.empty()
                    dice_group.empty()

                    game_on = True
                    first_player_move = True
                    second_player_move = False

                    current_interface = "Start Interface"
                    current_player = "Player1"
                    current_game_mode = ""
                    winner = ""

                    player1_turns_quantity = 0
                    player2_turns_quantity = 0

                    player1_wins_quantity = 0
                    player2_wins_quantity = 0

                    game_data_dict = {"Total dice throws": 0,
                                      "Quantity of received 1": 0,
                                      "Quantity of received 2": 0,
                                      "Quantity of received 3": 0,
                                      "Quantity of received 4": 0,
                                      "Quantity of received 5": 0,
                                      "Quantity of received 6": 0,
                                      "Quantity of received 7-12": 0,
                                      "Ladders used": 0,
                                      "Snakes used": 0
                                      }

                    screen.fill(THECOLORS["grey"])

                    StartInterface()
                elif pygame.mouse.get_pos()[0] >= 750 and pygame.mouse.get_pos()[0] <= 950 and pygame.mouse.get_pos()[1] >= 450 and pygame.mouse.get_pos()[1] <= 650:
                    player_piece_group.empty()
                    ladder_group.empty()
                    snake_group.empty()
                    dice_group.empty()

                    game_on = True
                    first_player_move = True
                    second_player_move = False

                    current_interface = "Game Interface"
                    current_player = "Player1"
                    winner = ""

                    player1_turns_quantity = 0
                    player2_turns_quantity = 0

                    player1_wins_quantity = 0
                    player2_wins_quantity = 0

                    game_data_dict = {"Total dice throws": 0,
                                      "Quantity of received 1": 0,
                                      "Quantity of received 2": 0,
                                      "Quantity of received 3": 0,
                                      "Quantity of received 4": 0,
                                      "Quantity of received 5": 0,
                                      "Quantity of received 6": 0,
                                      "Quantity of received 7-12": 0,
                                      "Ladders used": 0,
                                      "Snakes used": 0
                                      }

                    screen.fill(THECOLORS["grey"])

                    if current_game_mode == "Hypothesis Testing":
                        GameInerface()
                        PlayerPieceMove()
                    elif current_game_mode != "Simulation":
                        GameInerface()
                    else:
                        SimulationInterface()
            else:
                window_changed = False

        pygame.display.flip()