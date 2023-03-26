import pygame

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)
snowman = pygame.image.load('image/icogame.png')
snowman = pygame.transform.scale(snowman, (100, 100))
BLACK = (0, 0, 0)
clock = pygame.time.Clock()


man_x = 0
man_y = 0

speed_x = 1
speed_y = 1

run = True
while run:
    screen.fill(BLACK)
    screen.blit(snowman, (man_x, man_y))
    if man_x <= 400 and man_y == 0:
        man_x += speed_x
    if man_x >= 400 and man_y <= 400:
        man_y += speed_y
    if man_y >= 400 and man_x <= 400:
        man_x -= speed_x
    if man_x == 0 and man_y <= 400:
        man_y -= speed_y




    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(160)