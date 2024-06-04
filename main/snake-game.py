# Import packages
import os
import sys
import random
import pygame
from pygame.locals import *

# Define constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUEGRAY = (65, 75, 95)
MESSAGE_FONT_FAMILY = "arialblack"
MESSAGE_FONT_SIZE = 30
SCORE_FONT_FAMILY = MESSAGE_FONT_FAMILY
SCORE_FONT_SIZE = 20


# Initialise variables
snake_size = 10
snake_speed = 30

# Define functions
def print_score(score):
    text = pygame.font.SysFont(SCORE_FONT_FAMILY, SCORE_FONT_SIZE).render(f"Score: {score}", True, WHITE)
    window.blit(text, [0, 0])

def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(window, WHITE, [pixel[0], pixel[1], snake_size, snake_size])

# Initialise PyGame application
clock = pygame.time.Clock()
pygame.init()
window = pygame.display.set_mode(DIMENSIONS)
icon = pygame.image.load((os.path.abspath(os.path.join(__file__, os.pardir)) + "/assets/images/snake.png").replace("\\", "/").replace("main/",""))
pygame.display.set_caption("Snake Game")
pygame.display.set_icon(icon)
font = pygame.font.SysFont("arialblack", 20)

def main_menu():
    while True:
        window.fill(BLUEGRAY)
        font.render("Snake Game", True, WHITE).get_rect().topleft = (20, 20)
        window.blit(font.render("Snake Game", True, WHITE), font.render("Snake Game", True, WHITE).get_rect())
        mx, my = pygame.mouse.get_pos()
        play_button = pygame.Rect(50, 100, 200, 50)
        play_button_text = "Play"
        pygame.draw.rect(window, WHITE, play_button)
        play_button_render = font.render(play_button_text, True, BLACK)
        window.blit(play_button_render, play_button)
        quit_button = pygame.Rect(50, 200, 200, 50)
        quit_button_text = "Quit"
        pygame.draw.rect(window, WHITE, quit_button)
        quit_button_render = font.render(quit_button_text, True, BLACK)
        window.blit(quit_button_render, quit_button)
        if play_button.collidepoint(mx, my):
            if click:
                game()
        if quit_button.collidepoint(mx, my):
            if click:
                quit()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(snake_speed)

def game():
    running = True
    score = 0
    while running:
        window.fill(BLUEGRAY)
        font.render(f"Score: {score}", True, WHITE).get_rect().topleft = (20, 20)
        window.blit(font.render(f"Score: {score}", True, WHITE), font.render("Snake Game", True, WHITE).get_rect())
        game_over = False
        game_close = False
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        x_speed = 0
        y_speed = 0
        snake_pixels = []
        snake_length = 1
        target_x = int(random.randrange(0, SCREEN_WIDTH - snake_size) / 10.0) * 10
        target_y = int(random.randrange(0, SCREEN_HEIGHT - snake_size) / 10.0) * 10
        window.fill(BLUEGRAY)
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        while not game_over:
            while game_close:
                window.fill(BLUEGRAY)
                game_over_message = pygame.font.SysFont(MESSAGE_FONT_FAMILY, MESSAGE_FONT_SIZE).render("Game Over!", True, WHITE)
                window.blit(game_over_message, [SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3])
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_1:
                            quit()
                        if event.key == K_2:
                            main_menu()
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT and x_speed == 0:
                        x_speed = -snake_size
                        y_speed = 0
                    if event.key == K_RIGHT and x_speed == 0:
                        x_speed = snake_size
                        y_speed = 0
                    if event.key == K_UP and y_speed == 0:
                        x_speed = 0
                        y_speed = -snake_size
                    if event.key == K_DOWN and y_speed == 0:
                        x_speed = 0
                        y_speed = snake_size
            if x < 0:
                x += SCREEN_WIDTH
            if x >= SCREEN_WIDTH:
                x %= SCREEN_WIDTH
            if y < 0:
                y += SCREEN_HEIGHT
            if y >= SCREEN_HEIGHT:
                y %= SCREEN_HEIGHT
            x += x_speed
            y += y_speed

            window.fill(BLUEGRAY)
            pygame.draw.rect(window, RED, [target_x, target_y, snake_size, snake_size])
            snake_pixels.append([x, y])
            
            if len(snake_pixels) > snake_length:
                del snake_pixels[0]
            
            for pixel in snake_pixels[:-1]:
                if pixel == [x, y]:
                    game_close = True
            
            draw_snake(snake_size, snake_pixels)
            print_score(snake_length - 1)
            pygame.display.update()

            if max(abs(x - target_x), abs(y - target_y)) <= 5:
                target_x = round(random.randrange(0, SCREEN_WIDTH - snake_size) / 10.0) * 10
                target_y = round(random.randrange(0, SCREEN_HEIGHT - snake_size) / 10.0) * 10
                score += 1
                snake_length += 1
            clock.tick(snake_speed)
            pygame.display.update()

def quit():
    pygame.quit()
    sys.exit()

main_menu()