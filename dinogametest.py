import pygame
import random
import sys
WIDTH = 800
HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
dino_width = 69
dino_height = 69
dino_x = 50
dino_y = HEIGHT - dino_height - 50
dino_color = (100, 100, 100)
dino_jump_speed = 10
cactus_width = 32
cactus_height = 69
cactus_x = WIDTH
cactus_y = HEIGHT - cactus_height - 50
cactus_color = (0, 100, 0)
cactus_speed = 5
score = 0
is_jumping = False
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
def draw_dinosaur():
    pygame.draw.rect(window, dino_color, (dino_x, dino_y, dino_width, dino_height))
def draw_cactus():
    pygame.draw.rect(window, cactus_color, (cactus_x, cactus_y, cactus_width, cactus_height))
def check_collision():
    if dino_x + dino_width >= cactus_x and dino_x <= cactus_x + cactus_width:
        if dino_y + dino_height >= cactus_y:
            return True
    return False
def game_over():
    font = pygame.font.Font(None, 69)
    text = font.render("Game Over, Lucas x Alden", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
        window.fill(BLACK)
    draw_dinosaur()
    draw_cactus()
    cactus_x -= cactus_speed
    if cactus_x + cactus_width < 0:
        cactus_x = WIDTH
        score += 1
        if score % 5 == 0:
            cactus_speed += 1
        if is_jumping:
        dino_y -= dino_jump_speed
        dino_jump_speed -= 1
        if dino_y >= HEIGHT - dino_height - 50:
            dino_y = HEIGHT - dino_height - 50
            is_jumping = False
            dino_jump_speed = 10
    if check_collision():
        game_over()
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, WHITE)
    window.blit(text, (20, 20))
    pygame.display.flip()
    clock.tick(60)
    # taboritsy funni clock man lol
    #also lucas is female
