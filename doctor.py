import pygame, random

class Doctor(pygame.sprite.Sprite):
    def __init__(self, pos):
        self.image = pygame.image.load('doctor.png')