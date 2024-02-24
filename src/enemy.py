
import pygame
import random
import os

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'enemy.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 3

    def update(self):
        # Move the enemy horizontally
        self.rect.x += self.speed

        # If the enemy goes off-screen, reset its position
        if self.rect.right < 0:
            self.rect.left = 800  # Adjust this value based on your screen width
            self.rect.centery = random.randint(0, 600)  # Adjust this value based on your screen height
