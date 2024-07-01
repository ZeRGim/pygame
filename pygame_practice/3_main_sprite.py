import pygame

pygame.init()

screen_width= 480
screen_height= 640

screen = pygame.display.set_mode((screen_width,screen_height))

#타이틀 설정
pygame.display.set_caption("Nado Game")

#배경 이미지 불러오기
background = pygame.image.load(r'/pygame_practice/background.png')

#캐릭터 불러오기
character=pygame.image.load(r"/pygame_practice/character.png")
character_size= character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos= (screen_width-70)/2
character_y_pos=screen_height-70


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창닫기 검증
            running = False

    screen.blit(background,(0,0)) #배경그리기

    screen.blit(character, (character_x_pos,character_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기


pygame.quit()