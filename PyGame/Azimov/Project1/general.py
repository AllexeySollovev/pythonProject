import pygame
FPS = 60
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
pygame.display.update()
pygame.init()
run = True
while run:

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    clock.tick(FPS)

