import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
# musicsound = pygame.mixer.music.load('game-music.mp3')
# pygame.mixer.music.play(-1) 

width = 640
height = 480

x_snake = int(width/2)
y_snake = int(height/2)

speed = 10
x_control = speed
y_control = 0

x_apple = randint(40,600)
y_apple = randint(50,430)

points = 0
text_font = pygame.font.SysFont('courier', 30, True, False)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('cobrADA')
clock = pygame.time.Clock()

snake_list = []
snake_size = 5

dead = False

def increase_snake(snake_list):
    for XeY in snake_list:
        pygame.draw.rect(screen, (0,255,0), (XeY[0], XeY[1], 20, 20 ))

def restart_game():
    global points, snake_size, x_snake, y_snake, snake_list, head_list, x_apple, y_apple, dead
    points = 0
    snake_size = 5
    x_snake = int(width/2)
    y_snake = int(height/2)
    snake_list = []
    head_list = []
    x_apple = randint(40,600)
    y_apple = randint(50,430)
    dead = False

while True:

    clock.tick(30)
    screen.fill((255,255,255))
    message = f'Points:{points}'
    text_show = text_font.render(message, True, (0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                if x_control == speed:
                    pass
                else:
                    x_control = -speed
                    y_control = 0
            if event.key == K_d or event.key == K_RIGHT:
                if x_control == -speed:
                    pass
                else:
                    x_control = speed
                    y_control = 0
            if event.key == K_s or event.key == K_DOWN:
                if y_control == -speed:
                    pass
                else:
                    x_control = 0
                    y_control = speed
            if event.key == K_w or event.key == K_UP:
                if y_control == speed:
                    pass
                else:
                    x_control = 0
                    y_control = -speed  

    x_snake = x_snake + x_control
    y_snake = y_snake + y_control

    snake = pygame.draw.rect(screen,(0,255,0),(x_snake,y_snake,20,20))
    apple = pygame.draw.rect(screen,(255,0,0),(x_apple,y_apple,20,20))
    
    if apple.colliderect(snake):
        x_apple = randint(40,600)
        y_apple = randint(50,430)
        points = points + 1
        snake_size = snake_size + 1

    head_list = []
    head_list.append(x_snake)
    head_list.append(y_snake)

    snake_list.append(head_list)

    if snake_list.count(head_list) > 1:
        dead_font = pygame.font.SysFont('courier',20, True, False)
        dead_message = 'Game over! Press R to play again!'
        dead_text = dead_font.render(dead_message,True, (0,0,0))
        dead_text_rect = dead_text.get_rect()

        dead = True
        while dead:
            screen.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart_game()

            dead_text_rect.center = (width//2, height//2)        
            screen.blit(dead_text, dead_text_rect) 
            pygame.display.update()
    
    if x_snake > width:
        x_snake = 0
    if x_snake < 0:
        x_snake = width
    if y_snake > height:
        y_snake = 0
    if y_snake < 0:
        y_snake = height


    if len(snake_list) > snake_size:
        del snake_list [0]

    increase_snake (snake_list)

    screen.blit(text_show,(10,20))
    pygame.display.update()