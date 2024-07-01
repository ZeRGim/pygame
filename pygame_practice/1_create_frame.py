import pygame

pygame.init()

screen_width= 480
screen_height= 640

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Nado Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창닫기 검증
            running = False

pygame.quit()