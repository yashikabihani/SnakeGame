#importing libraries
import pygame
import time
import random

#Initialize the library
pygame.init()

#Initialize the window size on which the game would be played
window_x = 900
window_y = 600

#Defining Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
yellow_1 = (213, 200, 80)
green = (0, 255, 0)
red = (255, 0, 0)

#Displaying the title in the particular window
title = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Snake Game")

#Adding the timer - FPS(frames per second) Controller
#Objective : As soon as the food is eaten, the timer sets it again
fps = pygame.time.Clock()

snake_block = 10
snake_speed = 10

display_style = pygame.font.SysFont("Arial", 30, "Bold")
score_font = pygame.font.SysFont("Arial", 45, "Bold")

def show_score(score):
    value = score_font.render("Enjoy the Snake Game. Your Score is "+str(score), True, yellow)
    title.blit(value, [0, 0])

def make_snake(snake_block, list_snake):
    for x in list_snake:
        pygame.draw.rect(title, black, (x[0], x[1], snake_block, snake_block))


def display_msg(msg, color):
    msg = display_style.render(msg, True, color)
    title.blit(msg, [window_x/6, window_y/3])

def game_start():
    game_over = False
    game_close = False

    value_x1 = window_x/2
    value_y1 = window_y/2

    new_x1 = 0
    new_y1 = 0

    list_snake =  []
    snake_len = 1

    food_pos_x = round(random.randrange(0, window_x-snake_block)/ 10.0)* 10.0
    food_pos_y = round(random.randrange(0, window_y-snake_block)/ 10.0)* 10.0

    while not game_over:
        while game_close == True:
            title.fill(red)
            display_msg("You lost, Would like to play again? Press C else press Q", yellow_1)
            show_score(snake_len -1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_start()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_x1 = -snake_block
                    new_y1 = 0
                elif event.key == pygame.K_RIGHT:
                    new_x1 = snake_block
                    new_y1 = 0
                elif event.key == pygame.K_UP:
                    new_y1 = -snake_block
                    new_x1 = 0
                elif event.key == pygame.K_DOWN:
                    new_y1 = snake_block
                    new_x1 = 0
        
        if value_x1 >= window_x or value_x1<=0 or value_y1>= window_y or value_y1 < 0:
            game_close = True

        value_x1 = value_x1 + new_x1
        value_y1 = value_y1 + new_y1
        title.fill(red)

        pygame.draw.rect(title, green, (food_pos_x, food_pos_y, snake_block, snake_block))
        snake_head = []
        snake_head.append(value_x1)
        snake_head.append(value_y1)
        list_snake.append(snake_head)
        if len(list_snake)> snake_len:
            del list_snake[0]

        for x in list_snake[:-1]:
            if x == snake_head:
                game_close = True

        make_snake(snake_block, list_snake)
        show_score(snake_len - 1)

        pygame.display.update()

        if value_x1 == food_pos_x and value_y1 == food_pos_y:
            food_pos_x = round(random.randrange(0, window_x-snake_block)/10.0)*10.0
            food_pos_y = round(random.randrange(0, window_y-snake_block)/10.0)*10.0
            snake_len = snake_len+1

        fps.tick(snake_speed)
    pygame.quit()
    quit()

game_start()
        
        






