"""
Will start the main menu implementation
Give basic tetris functionality as well
"""
from Helpers import HelpingMethods

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
font = py.font.SysFont("Arial", 20, True)
text1 = font.render(" START ", True, "Orange")

buttonPadding = 20
newButtonDim = [text1.get_width() + buttonPadding * 2, text1.get_height() + buttonPadding * 2]
buttonNewSurface = py.Surface(newButtonDim)
buttonNewSurface.fill("black")
buttonNewSurface.blit(text1, (buttonPadding, buttonPadding))

newButtonOutline = py.Rect(0, 0, newButtonDim[0], newButtonDim[1])
py.draw.rect(buttonNewSurface, "red", newButtonOutline, 1)

rect1 = buttonNewSurface.get_rect(topleft=(100, 100))

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
            if rect1.collidepoint(event.pos):
                print("Button was pressed!")
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                running = False
            if event.key == py.K_F1:
                py.display.set_mode((widthf, heightf), py.FULLSCREEN)

    # Fill in the screen black, this is our background color that will not change.
    screen.fill("black")
    screen.blit(buttonNewSurface, (100, 100))
    py.draw.rect(screen, (255, 0, 0), rect1, 1)

    # Dimensions will be a ratio of screen size

    if positionLogo.y < 200:
        positionLogo.y += logoVelocity

    screen.blit(scaledLogo, positionLogo.topleft)
    py.display.flip()

    # if positionLogo.y == 200:

    clock.tick(60)

py.quit()
