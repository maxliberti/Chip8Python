import pygame

screen = pygame.display.set_mode((64, 32))
pygame.display.set_caption("CHIP 8")
screen.fill((255,255,255))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

