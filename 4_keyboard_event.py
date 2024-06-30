import pygame

pygame.init()

screen_width= 480
screen_height= 640

screen = pygame.display.set_mode((screen_width,screen_height))

#타이틀 설정
pygame.display.set_caption("Nado Game")

#배경 이미지 불러오기
background = pygame.image.load(r'C:\Users\wldn2\PycharmProjects\pygame_basic\background.png')

#캐릭터 불러오기
character=pygame.image.load(r"C:\Users\wldn2\PycharmProjects\pygame_basic\character.png")
character_size= character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos= (screen_width-70)/2
character_y_pos=screen_height-70

#이동할 좌표
to_x=0
to_y=0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창닫기 검증
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos+=to_x
    character_y_pos+=to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos+70 > screen_width:
        character_x_pos = screen_width-70

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos+70 > screen_height:
        character_y_pos = screen_height-70

    screen.blit(background,(0,0)) #배경그리기

    screen.blit(character, (character_x_pos,character_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기


pygame.quit()