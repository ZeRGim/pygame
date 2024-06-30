import pygame

pygame.init()

screen_width= 480
screen_height= 640

screen = pygame.display.set_mode((screen_width,screen_height))

#타이틀 설정
pygame.display.set_caption("Nado Game")

#FPS
clock=pygame.time.Clock()

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

#이동속도
character_speed=0.6

#적
enemy=pygame.image.load(r"C:\Users\wldn2\PycharmProjects\pygame_basic\enemy.png")
enemy_size= character.get_rect().size
enemy_width=character_size[0]
enemy_height=character_size[1]
enemy_x_pos= (screen_width-70)/2
enemy_y_pos=(screen_height-70)/2

#폰트정의
game_font=pygame.font.Font(None, 40)

#시간
total_time=10
start_ticks=pygame.time.get_ticks()



#이벤트 루프
running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창닫기 검증
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos+=to_x * dt
    character_y_pos+=to_y * dt

    #경계값 설정
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos+70 > screen_width:
        character_x_pos = screen_width-70

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos+70 > screen_height:
        character_y_pos = screen_height-70

    #충돌처리를 위한 rect 정보 업데이트
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌처리
    if character_rect.colliderect(enemy_rect):
        print("충돌했어욤")
        running = False



    screen.blit(background,(0,0)) #배경그리기

    screen.blit(character, (character_x_pos,character_y_pos))

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    #타이머 , 경과시간
    elapsed_time= (pygame.time.get_ticks()-start_ticks) / 1000

    timer = game_font.render(str(int(total_time-elapsed_time)), True,(255,255,255))
    #출력할 글자 , True, 글자 색상
    screen.blit(timer, (10,10))

    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running=False


    pygame.display.update() # 게임화면을 다시 그리기

pygame.time.delay(2000)

pygame.quit()