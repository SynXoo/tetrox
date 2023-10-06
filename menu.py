"""
Will start the main menu implementation
Give basic tetris functionality as well
"""
from Helpers import HelpingMethods
from Button import Button

import pygame as py
import os

import Helpers

# Pygame setup, basic implementation
py.init()

helpers = HelpingMethods()  # Static method modifier

# Normal and Full screen parameters are set
size = [width, height] = [800, 1000]
fullscreen = [widthf, heightf] = [1920, 1080]

# Button creation


# List that stores tetris pieces
tetris_pieces = []
# Defines the playing board
rows, columns = (20, 10)
board = [[False] * columns] * rows
print(board)

# Sets up default dimensions
screen = py.display.set_mode((width, height))
py.display.set_caption("Image Demo")

# Imports menu items
tetrox_logo = py.image.load("tetrox menu items/Tetrox_logo-removebg-preview.png").convert_alpha()
logoVelocity = 3
scaledLogo = helpers.imageScaler(tetrox_logo, 1.5)
positionLogo = scaledLogo.get_rect()
print(f'Before: {positionLogo}')
'''
Hratio is very high because I wanted the logo to start from
above the screen and drop down
'''
positionLogo = helpers.ratioRetainer(positionLogo, 2, -100)

print(f'After: {positionLogo}')

# Sets tick rate for game
clock = py.time.Clock()

# Starts the game while True
running = True

# Starts the game
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.MOUSEBUTTONDOWN:
            if start_button.rect.collidepoint(event.pos):
                print("Button was pressed!")
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                running = False
            if event.key == py.K_F1:
                py.display.set_mode((widthf, heightf), py.FULLSCREEN)

    # Fill in the screen black, this is our background color that will not change.
    screen.fill("black")

    # Dimensions will be a ratio of screen size
    start_button = Button(" START ", helpers.positionReturner(2, 2.5))
    option_button = Button("OPTIONS", helpers.positionReturner(2, 2))
    start_button.draw(screen)
    option_button.draw(screen)

    if positionLogo.y < 200:
        positionLogo.y += logoVelocity

    screen.blit(scaledLogo, positionLogo.topleft)
    py.display.flip()

    # if positionLogo.y == 200:

    clock.tick(60)

py.quit()
