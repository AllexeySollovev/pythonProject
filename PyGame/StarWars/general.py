import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 750))

bg = pygame.image.load('images/bg.jpg').convert_alpha()

player = pygame.image.load('images/player.png').convert_alpha()
enemy = pygame.image.load('images/enemy.png').convert_alpha()
enemies_in_game = []

bullets_left = 30
bullet = pygame.image.load('images/bullet.png')
bullets = []

player_x = 450
player_y = 600
player_speed = 1

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 5000)

balls = 0
label = pygame.font.Font('fonts/Roboto-Black.ttf', 40)
info_balls = label.render('очки:', False, 'White')
info_bullets = label.render('снаряды:', False, 'White')

losel = label.render('Вы проиграли!', False, 'White')
restart = label.render('Играть снова', False, 'White')

gameplay = True
run = True
while run:
    label_balls = label.render(str(balls), False, 'White')
    label_bullets = label.render(str(bullets_left), False, 'White')
    screen.blit(bg, (0, 0))
    screen.blit(player, (player_x, player_y))
    screen.blit(info_balls, (0, 0))
    screen.blit(info_bullets, (750, 0))
    screen.blit(label_bullets, (950, 0))
    screen.blit(label_balls, (110, 0))

    if gameplay:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_x > 20:
            player_x -= player_speed
        if keys[pygame.K_d] and player_x < 920:
            player_x += player_speed
        if keys[pygame.K_w] and player_y > 400:
            player_y -= player_speed
        if keys[pygame.K_s] and player_y < 660:
            player_y += player_speed

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x + 15, el.y))
                el.y += -1.9

                if el.y < -10:
                    bullets.pop(i)
                if enemies_in_game:
                    for (index, ghost_el) in enumerate(enemies_in_game):
                        if el.colliderect(ghost_el):
                            enemies_in_game.pop(index)
                            bullets.pop(i)
                            balls += 1

        player_rect = player.get_rect(topleft=(player_x, player_y))

        if enemies_in_game:
            for (i, el) in enumerate(enemies_in_game):
                screen.blit(enemy, el)
                el.x -= 0.7

                if bullets_left <= 0:
                    gameplay = False
                    #bg_sound.stop()
    else:
        screen.fill('Red')
        screen.blit(losel, (400, 200))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        elif event.type == enemy_timer:
            enemies_in_game.append(enemy.get_rect(topleft=(1000, 100)))
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and bullets_left > 0:
            bullets.append(
                bullet.get_rect(topleft=(player_x + 10, player_y + 10)))
            bullets_left -= 1
