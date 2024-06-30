import pygame
import random

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("quiz")

clock = pygame.time.Clock()

background = pygame.image.load(r"C:\Users\wldn2\PycharmProjects\pygame_basic\background.png")

character = pygame.image.load(r"C:\Users\wldn2\PycharmProjects\pygame_basic\character.png")
character_size = character.get_rect()
character_width = character_size[0]
character_height = character_size[1]
character_x = (screen_width-70)/2
character_y = screen_height-70

enemy = pygame.image.load(r"C:\Users\wldn2\PycharmProjects\pygame_basic\enemy.png")
enemy_size = enemy.get_rect()
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x = random.random()*410
enemy_y = 0

font = pygame.font.Font(None,40)

to_x = 0

character_speed=0.6
cnt=0
running = True
while running:
    tick = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            to_x = 0

    enemy_y += 0.5*tick

    character_x += to_x*tick

    if character_x <= 0:
        character_x = 0
    elif character_x >= screen_width-70:
        character_x = screen_width-70

    if enemy_y >= 640:
        enemy_y = 0
        enemy_x = random.random()*410
        cnt += 1

    character_rect=character.get_rect()
    character_rect.left = character_x
    character_rect.top = character_y

    enemy_rect=enemy.get_rect()
    enemy_rect.left = enemy_x
    enemy_rect.top = enemy_y




    screen.blit(background, (0,0))

    screen.blit(character, (character_x,character_y))

    screen.blit(enemy, (enemy_x,enemy_y))

    score = font.render(str(cnt), True, (255,255,255))
    screen.blit(score, (10,10))
    if character_rect.colliderect(enemy_rect):
        print("Game Over")
        running = False
        gameover=font.render("Game Over", True, (255, 255, 255))
        screen.blit(gameover, (240, 320))

    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()