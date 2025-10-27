import pygame
import random

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
        global direction
        
        if self.ishead:
            if direction == "up":
                self.rect.y -= self.length
            elif direction == "down":
                self.rect.y += self.length
            elif direction == "left":
                self.rect.x -= self.length
            elif direction == "right":
                self.rect.x += self.length
            

class Apple(pygame.sprite.Sprite):
    def __init__(self, length = 20):
        super().__init__()
        self.length = length
        
        self.image = pygame.Surface([self.length, self.length], pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.rect = pygame.draw.circle(self.image, "red", (self.length//2, self.length//2), self.length//2)

        self.teleport()

    def teleport(self):
        # Calculate the playable area (inside the boundary)
        playable_width = SIZE[0] - (self.length * 4)  # Subtract boundary width on both sides
        playable_height = SIZE[1] - (self.length * 4)  # Subtract boundary width on both sides
        
        # Calculate maximum grid positions
        max_x = playable_width // self.length
        max_y = playable_height // self.length
        
        # Spawn apple within playable area, offset by boundary width
        self.rect.x = (random.randint(0, max_x) * self.length) + (self.length * 2)
        self.rect.y = (random.randint(0, max_y) * self.length) + (self.length * 2)



snakegroup = pygame.sprite.Group()
head = Snake(SIZE[0]//2//20*20, SIZE[1]//2//20*20, True)
snakegroup.add(head)
snakeposition = []
snakeposition.append((head.rect.x, head.rect.y))

applegroup = pygame.sprite.GroupSingle()

apple = Apple()
applegroup.add(apple)

score_font = pygame.font.Font(None, 30)
score_text = score_font.render(f"Score: {len(snakeposition)}", True, (0, 0, 0))

def game_over_screen():
    global score_text, running
    screen.fill("white")
    font=pygame.font.Font(None, 50)
    game_over_text = font.render("Game Over", True, (0, 0, 0))
    text_rect = game_over_text.get_rect(center=(250,200))
    scoretext_rect = score_text.get_rect(center = (250, 250))
    screen.blit(game_over_text, text_rect)
    screen.blit(score_text, scoretext_rect)
    pygame.display.update()
    pygame.time.wait(3000)
    running = False
    pygame.quit()
    exit()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != "down":
        direction = "up"
    elif keys[pygame.K_DOWN] and direction != "up":
        direction = "down"
    elif keys[pygame.K_LEFT] and direction != "right":
        direction = "left"
    elif keys[pygame.K_RIGHT] and direction != "left":
        direction = "right"

    snakegroup.update()

    snakeposition.append((head.rect.x, head.rect.y))

    while len(snakeposition) > len(snakegroup.sprites()):
        snakeposition.pop(0)

    print(snakeposition)
    for position, snakeblock in zip(snakeposition[::-1], snakegroup.sprites()):
        snakeblock.rect.x = position[0]
        snakeblock.rect.y = position[1]

    
    if (head.rect.x, head.rect.y) in snakeposition[:-1]:
        game_over_screen()
    
    # Check if snake hits any boundary
    if (head.rect.y >= SIZE[1] - head.length or 
        head.rect.y < 20 or 
        head.rect.x >= SIZE[0] - head.length or 
        head.rect.x < 20):
        game_over_screen()

    # Check for collision with apple using rect collision
    if pygame.sprite.collide_rect(head, apple):
        apple.teleport()
        body = Snake(snakeposition[0][0], snakeposition[0][1], length = 20)
        snakegroup.add(body)

    score_text = score_font.render(f"Score: {len(snakeposition)}", True, (0, 0, 0))
    score_text_rect = score_text.get_rect(center=(SIZE[0] - 100, SIZE[1] // 7))
    
    screen.fill("black")  # Fill entire screen with black first
    
    # Draw the play area in white
    play_area = pygame.Surface((SIZE[0] - head.length * 2, SIZE[1] - head.length * 2))
    play_area.fill("white")
    screen.blit(play_area, (head.length, head.length))
    
    # Draw the boundary outline
    pygame.draw.rect(screen, "blue4", (head.length, head.length, SIZE[0] - head.length * 2, SIZE[1] - head.length * 2), 2)
    
    snakegroup.draw(screen)
    applegroup.draw(screen)
    screen.blit(score_text, score_text_rect)
    pygame.display.flip()
    clock.tick(10) 
    
