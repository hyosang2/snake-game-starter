import pygame
import random

# Initialize pygame
pygame.init()
SIZE = (500, 400)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
running = True
direction = ""

class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, ishead=False, length=20):
        super().__init__()
        self.length = length
        self.image = pygame.Surface([self.length, self.length])
        self.image.fill("blue4")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.ishead = ishead

    def update(self):
        
        # TODO: Implement snake movement based on direction
        # Hint: Use direction variable to move the snake head
        # Remember to handle up, down, left, and right movements
        pass

class Apple(pygame.sprite.Sprite):
    def __init__(self, length = 20):
        super().__init__()
        self.length = length
        
        self.image = pygame.Surface([self.length, self.length], pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.rect = pygame.draw.circle(self.image, "red", (self.length//2, self.length//2), self.length//2)

        self.teleport()

    def teleport(self):
        # TODO: Implement apple respawning logic
        # Hint: Use random positions within the playable area
        # Make sure the apple doesn't spawn on the snake
        pass
        


# Initialize game objects
snakegroup = pygame.sprite.Group()
head = Snake(SIZE[0]//2//20*20, SIZE[1]//2//20*20, True)
snakegroup.add(head)
snakeposition = []
snakeposition.append((head.rect.x, head.rect.y))

applegroup = pygame.sprite.GroupSingle()
apple = Apple()
applegroup.add(apple)
print (apple.rect.x, apple.rect.y)

# Score display setup
score_font = pygame.font.Font(None, 30)
score_text = score_font.render(f"Score: {len(snakeposition)}", True, (0, 0, 0))

def game_over_screen():
    # TODO: Implement game over screen
    # Hint: Display "Game Over" text and final score
    # Wait for a few seconds before quitting
    pass

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO: Implement keyboard controls
    # Hint: Use pygame.key.get_pressed() to check for arrow key presses
    # Remember to prevent 180-degree turns
    pass

    # Update snake position
    snakegroup.update()

    # TODO: Implement snake body movement
    # Hint: Update each body segment's position based on the previous segment. Use the snakeposition list to store the positions of the snake.
    pass
           
    # TODO: Implement collision detection
    # Hint: Check for:
    # 1. Snake hitting itself
    pass

    # 2. Snake hitting boundaries
    pass

    # 3. Snake eating the apple
    pass

    # Update score display
    score_text = score_font.render(f"Score: {len(snakeposition)}", True, (0, 0, 0))
    score_text_rect = score_text.get_rect(center=(SIZE[0] - 100, SIZE[1] // 7))
    
    # Drawing
    screen.fill("black")
    play_area = pygame.Surface((SIZE[0] - head.length * 2, SIZE[1] - head.length * 2))
    play_area.fill("white")
    screen.blit(play_area, (head.length, head.length))
    pygame.draw.rect(screen, "blue4", (head.length, head.length, SIZE[0] - head.length * 2, SIZE[1] - head.length * 2), 2)
    
    snakegroup.draw(screen)
    applegroup.draw(screen)
    screen.blit(score_text, score_text_rect)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()