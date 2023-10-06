import pygame as py


class Button:
    def __init__(self, text, center_pos, font_size=20):
        self.font = py.font.SysFont("Arial", font_size, True)
        self.text_surface = self.font.render(text, True, "Orange")
        self.button_padding = 20
        self.dimensions = [self.text_surface.get_width() + self.button_padding * 2,
                           self.text_surface.get_height() + self.button_padding * 2]

        self.center_position = center_pos

        self.update_dimensions()

    def update_dimensions(self, ratio=1):
        self.rect = py.Rect(0, 0, *self.dimensions)
        self.rect.center = self.center_position

    def draw(self, screen):
        button_surface = py.Surface(self.dimensions)
        button_surface.fill("black")
        button_surface.blit(self.text_surface, (self.button_padding, self.button_padding))
        screen.blit(button_surface, self.rect.topleft)
        py.draw.rect(screen, "navy", self.rect, 1)
