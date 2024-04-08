import pygame
#import buildozer

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1280, 748))
pygame.display.set_caption("-game-")
icon = pygame.image.load("images/icon_game.png").convert_alpha()
pygame.display.set_icon(icon)

bg = pygame.image.load("images/bg.png").convert_alpha()
walk_left = [
    pygame.image.load("images/sprites_player/Walk_01.png"),
    pygame.image.load("images/sprites_player/Walk_02.png"),
    pygame.image.load("images/sprites_player/Walk_03.png"),
    pygame.image.load("images/sprites_player/Walk_04.png"),
    pygame.image.load("images/sprites_player/Walk_05.png"),
    pygame.image.load("images/sprites_player/Walk_06.png"),
    pygame.image.load("images/sprites_player/Walk_07.png"),
    pygame.image.load("images/sprites_player/Walk_08.png"),
]
walk_right = [
    pygame.image.load("images/sprites_player/Walk_01.png"),
    pygame.image.load("images/sprites_player/Walk_02.png"),
    pygame.image.load("images/sprites_player/Walk_03.png"),
    pygame.image.load("images/sprites_player/Walk_04.png"),
    pygame.image.load("images/sprites_player/Walk_05.png"),
    pygame.image.load("images/sprites_player/Walk_06.png"),
    pygame.image.load("images/sprites_player/Walk_07.png"),
    pygame.image.load("images/sprites_player/Walk_08.png"),
]

ghost = pygame.image.load("images/ghost_icon.png").convert_alpha()
ghost_x = 1300
ghost_list_in_game = []

player_speed = 6
player_x = 500
player_y = 500

is_jump = False
jump_count = 9

player_anim_count = 0
bg_x = 0

bg_sound = pygame.mixer.Sound("music/bg_sound.wav")
bg_sound.play(-1)


ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 5000)

label = pygame.font.Font('fonts/Roboto-BlackItalic.ttf', 40)
lose_label = label.render('You Lose!', False, (193, 196, 199))
restart_label = label.render('Restart the game', False, (193, 196, 148))
restart_label_rect = restart_label.get_rect(topleft=(550, 400))

bullets_left = 5
bullet = pygame.image.load("images/icon_bullet_1.png").convert_alpha()
bullets = []

gameplay = True

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1280, 0))
    screen.blit(ghost, (ghost_x, 560))

    if gameplay:

        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -= 10

                if el.x < -10:
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False

        screen.blit(walk_right[player_anim_count], (player_x, player_y))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_x > 30:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 1050:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -9:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 9

        if player_anim_count == 7:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 3
        if bg_x <= -1280:
            bg_x = 0

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 15

                if el.x > 1280:
                    bullets.pop(i)

                if ghost_list_in_game:
                    for (index, ghost_el) in enumerate(ghost_list_in_game):
                        if el.colliderect(ghost_el):
                            ghost_list_in_game.pop(index)
                            bullets.pop(i)

    else:
        screen.fill((87, 88, 89,))
        screen.blit(lose_label, (530, 200))
        screen.blit(restart_label, (480, 400))

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            ghost_list_in_game.clear()
            bullets.clear()
            bullets_left = 5

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(1300, 560)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_f and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 60, player_y + 70)))
            bullets_left -= 1

    clock.tick(15)
