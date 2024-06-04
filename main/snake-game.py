# Import packages
import os
import sys
import time
import random
import pygame
import pygame_menu
from pygame.locals import *

# Define constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
BLUEGRAY = (65, 75, 95)

# Initialise variables
snake_length = 1
score = 0
running = False

# Define functions

# Initialise PyGame application
main_clock = pygame.time.Clock()
pygame.init()
window = pygame.display.set_mode(DIMENSIONS)
icon = pygame.image.load("C:/Users/Zakar/Desktop/General/projects/letsgrowmore/LGMVIP-Python-Task-2/assets/images/snake.png")
background = pygame.image.load("C:/Users/Zakar/Desktop/General/projects/letsgrowmore/LGMVIP-Python-Task-2/assets/images/background.png")
pygame.display.set_caption("Snake Game")
pygame.display.set_icon(icon)
font = pygame.font.SysFont("arialblack", 20)
# Credit: <a href="https://www.flaticon.com/free-icons/snake" title="snake icons">Snake icons created by Freepik - Flaticon</a>

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
        main_clock.tick(60)

def game():
    running = True
    while running:
        window.fill(BLUEGRAY)
        font.render("Game", True, WHITE).get_rect().topleft = (20, 20)
        window.blit(font.render("Game", True, WHITE), font.render("Snake Game", True, WHITE).get_rect())
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        main_clock.tick(60)

def quit():
    pygame.quit()
    sys.exit()

main_menu()