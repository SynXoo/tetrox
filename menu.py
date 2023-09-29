"""
Will start the main menu implementation
Give basic tetris functionality as well
"""
import pygame as py

# Pygame setup, basic implementation

py.init()

# Normal and Full screen parameters are set
size = [width, height] = [720, 840]
fullscreen = [widthf, heightf] = [1920, 1080]


def calculateCenter():
    w, h = py.display.get_window_size()
    centW = w // 2
    centH = h // 2
    print(f"These are the center coordinates:\n Width = {centW} pixels \n Height = {centH}")
    return centW, centH


def imageScaler(scale):
    multiplier = scale


# Sets up default dimensions
screen = py.display.set_mode((width, height))
py.display.set_caption("Image Demo")

# Imports a tetris piece
straight_tetro = py.image.load("tetris straight shape.png").convert_alpha()


straight_tetro_rect = straight_tetro.get_rect()

# Dimensions will be centered
straight_tetro_rect.center = calculateCenter()

# Sets tick rate for game
clock = py.time.Clock()

# Starts the game while True
running = True

# Starts the game
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                running = False
            if event.key == py.K_F1:
                py.display.set_mode((widthf, heightf), py.FULLSCREEN)

    screen.fill("black")

    current_width, current_height = py.display.get_window_size()
    screen.blit(straight_tetro, straight_tetro_rect)

    py.display.flip()

    clock.tick(60)

py.quit()

