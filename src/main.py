import pygame
from player import Player
from enemy import Enemy

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Zelda-like Game")

# Set up the game clock
clock = pygame.time.Clock()

# Create player
player = Player(screen_width // 2, screen_height // 2)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Create enemies
enemies = pygame.sprite.Group()
for _ in range(3):  # Adjust the number of enemies as needed
    enemy = Enemy(random.randint(0, screen_width), random.randint(0, screen_height))
    all_sprites.add(enemy)
    enemies.add(enemy)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Check for collisions between player and enemies
    if pygame.sprite.spritecollide(player, enemies, False):
        # Handle collision logic here (e.g., decrease player health, reset position, etc.)
        pass

    # Draw
    screen.fill((0, 0, 0))  # Clear the screen
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()