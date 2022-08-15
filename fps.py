import pygame

class Fps:

    def __init__(self, nb_fps):
        self.nb_fps = nb_fps
        self.clock = pygame.time.Clock()

    def set_fps(self):
        self.clock.tick(self.nb_fps)