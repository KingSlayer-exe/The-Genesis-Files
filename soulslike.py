import pygame
import sys

# Initialize pygame
pygame.init()

# Define game settings
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (100, 100, 100)  # Dark gray background

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Elden Ring-like Game")

# Generate a simple pixelated background
def generate_background():
    background = pygame.Surface((WIDTH, HEIGHT))
    for y in range(0, HEIGHT, 32):
        for x in range(0, WIDTH, 32):
            color = (34, 177, 76) if (x + y) % 64 == 0 else (50, 50, 50)  # Alternating grass/stone tiles
            pygame.draw.rect(background, color, pygame.Rect(x, y, 32, 32))
    return background

# Create a simple 2D pixel player sprite
def create_player_sprite():
    player = pygame.Surface((32, 32))  # Player is a 32x32 pixel sprite
    player.fill(RED)  # Red square as placeholder
    pygame.draw.rect(player, BLUE, pygame.Rect(8, 8, 16, 16))  # Draw a blue body inside the red square
    return player

# Create a simple 2D pixel enemy sprite
def create_enemy_sprite():
    enemy = pygame.Surface((32, 32))  # Enemy is a 32x32 pixel sprite
    enemy.fill(BLUE)  # Blue square as placeholder
    pygame.draw.rect(enemy, RED, pygame.Rect(8, 8, 16, 16))  # Draw a red body inside the blue square
    return enemy

# Game character class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = create_player_sprite()  # Use the generated player sprite
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 4
        self.health = 100
        self.attack_range = 50

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def attack(self):
        # Create a simple attack range (a rectangle in front of the player)
        attack_rect = pygame.Rect(self.rect.centerx, self.rect.centery - self.attack_range // 2,
                                  self.attack_range, self.attack_range)
        return attack_rect

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = create_enemy_sprite()  # Use the generated enemy sprite
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.health = 50
        self.speed = 2

    def update(self, player):
        # Basic AI: Move towards the player
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        if self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        if self.rect.y > player.rect.y:
            self.rect.y -= self.speed

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()

# Main game loop
def game_loop():
    player = Player()
    enemy1 = Enemy(300, 200)
    enemy2 = Enemy(500, 400)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player, enemy1, enemy2)

    enemies = pygame.sprite.Group()
    enemies.add(enemy1, enemy2)

    # Generate the background
    background = generate_background()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check if the player presses space to attack
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    attack_rect = player.attack()
                    for enemy in enemies:
                        if attack_rect.colliderect(enemy.rect):
                            enemy.take_damage(10)
                            print(f"Enemy hit! Health: {enemy.health}")

        # Update game state
        player.update()

        for enemy in enemies:
            enemy.update(player)  # Pass player to update each enemy's movement

        # Draw everything
        screen.blit(background, (0, 0))  # Draw the background
        all_sprites.draw(screen)  # Draw all sprites (player, enemies)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

# Run the game loop
if __name__ == "__main__":
    game_loop()




