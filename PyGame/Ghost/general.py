import pygame


clock = pygame.time.Clock()
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
screen = pygame.display.set_mode((618, 359))#flags=pygame.NOFRAME
pygame.display.set_caption('Pygame Project')
icon = pygame.image.load('images/icogame.png').convert_alpha()
pygame.display.set_icon(icon)

# square = pygame.Surface((50, 170))
# square.fill('Blue')

# myfont = pygame.font.Font('fonts/Roboto-Black.ttf', 40)
# text_surface = myfont.render('itPROJECT', False, 'Magenta')

#Player
bg = pygame.image.load('images/backg.png').convert_alpha()
walk_right = [
pygame.image.load('images/right1.png').convert_alpha(),
pygame.image.load('images/right1.png').convert_alpha(),
pygame.image.load('images/right1.png').convert_alpha(),
pygame.image.load('images/right1.png').convert_alpha(),
pygame.image.load('images/right2.png').convert_alpha(),
pygame.image.load('images/right2.png').convert_alpha(),
pygame.image.load('images/right2.png').convert_alpha(),
pygame.image.load('images/right2.png').convert_alpha(),
pygame.image.load('images/right3.png').convert_alpha(),
pygame.image.load('images/right3.png').convert_alpha(),
pygame.image.load('images/right3.png').convert_alpha(),
pygame.image.load('images/right3.png').convert_alpha(),
pygame.image.load('images/right4.png').convert_alpha(),
pygame.image.load('images/right4.png').convert_alpha(),
pygame.image.load('images/right4.png').convert_alpha(),
pygame.image.load('images/right4.png').convert_alpha()
]
walk_left = [
pygame.image.load('images/left1.png').convert_alpha(),
pygame.image.load('images/left1.png').convert_alpha(),
pygame.image.load('images/left1.png').convert_alpha(),
pygame.image.load('images/left1.png').convert_alpha(),
pygame.image.load('images/left2.png').convert_alpha(),
pygame.image.load('images/left2.png').convert_alpha(),
pygame.image.load('images/left2.png').convert_alpha(),
pygame.image.load('images/left2.png').convert_alpha(),
pygame.image.load('images/left3.png').convert_alpha(),
pygame.image.load('images/left3.png').convert_alpha(),
pygame.image.load('images/left3.png').convert_alpha(),
pygame.image.load('images/left3.png').convert_alpha(),
pygame.image.load('images/left4.png').convert_alpha(),
pygame.image.load('images/left4.png').convert_alpha(),
pygame.image.load('images/left4.png').convert_alpha(),
pygame.image.load('images/left4.png').convert_alpha()
]

ghost = pygame.image.load('images/ghost.png').convert_alpha()

ghost_list_in_game = []

player_anim_count = 0
bg_x = 0

player_speed = 4
player_x = 150
player_y = 250

is_jump = False
jump_count = 8

bg_sound = pygame.mixer.Sound('sounds/song1.mp3')
bg_sound.play()

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 3000)

label = pygame.font.Font('fonts/Roboto-Black.ttf', 40)
losel = label.render('Вы проиграли!', False, 'White')
restart = label.render('Играть снова', False, 'White')
restart_rect = restart.get_rect(topleft=(190, 200))

bullets_left = 5
bullet = pygame.image.load('images/bullet.png').convert_alpha()
bullets = []

gameplay = True
run = True
while run:
    screen.blit(bg, (bg_x - 618, 0))
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 618, 0))

    if gameplay:


        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -= 5

                if el.x < -10:
                    ghost_list_in_game.pop(i)
                if player_rect.colliderect(el):
                    gameplay = False
                    bg_sound.stop()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            bg_x -= 4
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
        if keys[pygame.K_a]:
            bg_x += 4
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))


        if keys[pygame.K_a] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_d] and player_x < 550:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -8:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 8



        if player_anim_count == 12:
            player_anim_count = 0
        else:
            player_anim_count += 1

        if bg_x <= -618 or bg_x >= 618:
            bg_x = 0

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 15

                if el.x > 630:
                    bullets.pop(i)
                if ghost_list_in_game:
                    for (index, ghost_el) in enumerate(ghost_list_in_game):
                        if el.colliderect(ghost_el):
                            ghost_list_in_game.pop(index)
                            bullets.pop(i)
    else:
        screen.fill('Red')
        screen.blit(losel, (180, 100))
        pygame.draw.rect(screen, (95, 98, 96), (160, 200, 320, 50))
        screen.blit(restart, restart_rect)
        mouse = pygame.mouse.get_pos()
        if restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            ghost_list_in_game.clear()
            bg_sound.play()
            bullets.clear()
            bullets_left = 5
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        elif event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(620, 250)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_r and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 10, player_y + 10)))
            bullets_left -= 1

    clock.tick(30)