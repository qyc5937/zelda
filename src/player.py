
import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.idle_image = pygame.image.load(os.path.join('assets', 'player_idle.png')).convert_alpha()
        self.walk_images = [pygame.image.load(os.path.join('assets', f'player_walk_{i}.png')).convert_alpha() for i in range(4)]
        self.image = self.idle_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5  # Adjust as needed for movement speed
        self.frame = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.image = self.walk_images[self.frame]
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.image = self.walk_images[self.frame]
        elif keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.image = self.walk_images[self.frame]
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.image = self.walk_images[self.frame]
        else:
            self.image = self.idle_image
        
        self.frame = (self.frame + 1) % 4  # Cycle through frames for walking animation