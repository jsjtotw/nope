import pygame
import sys
pygame.init()
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
cookie_pos = (WIDTH // 2, HEIGHT // 2)
cookie_radius = 69
cookie_color = (204, 204, 0)
score = 0
font_size = 36
font_color = WHITE
font_pos = (20, 20)
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                distance = ((cookie_pos[0] - mouse_pos[0]) ** 2 +
                            (cookie_pos[1] - mouse_pos[1]) ** 2) ** 0.5
                if distance < cookie_radius:
                    score += 1
        window.fill((0, 0, 0))
        pygame.draw.circle(window, cookie_color, cookie_pos, cookie_radius)
        font = pygame.font.Font(None, font_size)
    text = font.render(f"Score: {score}", True, font_color)
    window.blit(text, font_pos)
    pygame.display.flip()
    clock.tick(60)
