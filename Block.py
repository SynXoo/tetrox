# shapes.py

import pygame


class Block:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self, window):
        window.blit(self.image, (self.x * self.image.get_width(), self.y * self.image.get_height()))


class Tetromino:
    def __init__(self, x, y, blocks):
        self.x = x
        self.y = y
        self.blocks = blocks  # List of Block objects

    def draw(self, window):
        for block in self.blocks:
            block.draw(window)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        for block in self.blocks:
            block.x += dx
            block.y += dy

    def rotate(self):
        # Implement rotation logic here
        pass
