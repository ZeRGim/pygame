import pygame

# 스크린 전체 크기 지정

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# pygame 초기화

pygame.init()

# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooting Ball")

# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

FPS = 60

background=pygame.image.load("sources/background.jpg")


class Character(pygame.sprite.Sprite):

    def __init__(self, position):

        super(Character, self).__init__()

        # 이미지를 Rect안에 넣기 위해 Rect의 크기 지정
        # 이미지의 크기와 같게 하거나, 크기를 다르게 한다면 pygame.transform.scale을 사용하여 rect 안에
        # 이미지를 맞추도록 한다.
        size = (30, 70)

        # 여러장의 이미지를 리스트로 저장한다. 이미지 경로는 자신들의 경로를 사용한다.
        images = []

        # 서있는 상태 0 ~ 11
        images.append(pygame.image.load('sources/character/idle/Idle1.png'))
        images.append(pygame.image.load('sources/character/idle/Idle2.png'))
        images.append(pygame.image.load('sources/character/idle/Idle3.png'))
        images.append(pygame.image.load('sources/character/idle/Idle4.png'))
        images.append(pygame.image.load('sources/character/idle/Idle5.png'))
        images.append(pygame.image.load('sources/character/idle/Idle6.png'))
        images.append(pygame.image.load('sources/character/idle/Idle7.png'))
        images.append(pygame.image.load('sources/character/idle/Idle8.png'))
        images.append(pygame.image.load('sources/character/idle/Idle9.png'))
        images.append(pygame.image.load('sources/character/idle/Idle10.png'))
        images.append(pygame.image.load('sources/character/idle/Idle11.png'))

        # 걷기 12 ~ 21
        images.append(pygame.image.load('sources/character/run/Run1.png'))
        images.append(pygame.image.load('sources/character/run/Run2.png'))
        images.append(pygame.image.load('sources/character/run/Run3.png'))
        images.append(pygame.image.load('sources/character/run/Run4.png'))
        images.append(pygame.image.load('sources/character/run/Run5.png'))
        images.append(pygame.image.load('sources/character/run/Run6.png'))
        images.append(pygame.image.load('sources/character/run/Run7.png'))
        images.append(pygame.image.load('sources/character/run/Run8.png'))
        images.append(pygame.image.load('sources/character/run/Run9.png'))
        images.append(pygame.image.load('sources/character/run/Run10.png'))

        images.append(pygame.image.load('./sources/character/attack/Attack_1.png'))
        images.append(pygame.image.load('./sources/character/attack/Attack_1.png'))
        images.append(pygame.image.load('./sources/character/attack/Attack_1.png'))
        images.append(pygame.image.load('./sources/character/attack/Attack_1.png'))


        # rect 만들기
        self.rect = pygame.Rect(position, size)

        # Rect 크기와 Image 크기 맞추기. pygame.transform.scale
        self.images = images

        # 원본 캐릭터 이미지들
        self.images_right = images
        # 캐릭터 이미지가 오른쪽을 보고 있는데, 왼쪽으로 보도록 하기 위해서는
        # 이미지를 세로 기준으로 좌우로 뒤집이 준다. pygame.transform.flip 메서드 사용
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]

        # 캐릭터의 현재 상태
        # 0 - idle 상태, 1 - 걷고 있는 상태
        self.state = 0
        # 방향
        self.direction = 'right'
        # 속도
        self.velocity_x = 0

        # 캐릭터의 첫번째 이미지
        self.index = 0
        self.image = images[self.index]

        # 1초에 보여줄 1장의 이미지 시간을 계산, 소수점 3자리까지 반올림
        self.animation_time = round(100 / len(self.images * 100), 2)

        # mt와 결합하여 animation_time을 계산할 시간 초기화
        self.current_time = 0

        self.position=list(position)

    def update(self, mt):
        # update를 통해 캐릭터의 이미지가 계속 반복해서 나타나도록 한다.

        # 현재 상태에 따라 반복해줄 이미지의 index 설정과 속도
        if self.state == 0:
            count = 11
            start_Index = 0
            self.velocity_x = 0
        elif self.state == 1:
            count = 10
            start_Index = 11
            self.velocity_x = 4
        elif self.state == 2:
            count = 4
            start_Index = 21
            self.velocity_x = 0

        # 방향이 오른쪽이면, 오른쪽 이미지 선택
        if self.direction == 'right':
            self.images = self.images_right
        # 방향이 왼쪽이면 왼쪽 이미지 선택, 진행방향 x축으로 -
        elif self.direction == 'left':
            self.images = self.images_left
            self.velocity_x = abs(self.velocity_x) * -1

        # loop 시간 더하기
        self.current_time += mt

        # loop time 경과가 animation_time을 넘어서면 새로운 이미지 출력
        if self.current_time >= self.animation_time:
            self.current_time = 0

            # 상태에 따라 이미지 index 범위를 다르게 설정한다.

            # idle 상태는 0 ~ 9, 걷기 상태는 10 ~ 19
            self.index = (self.index % count) + start_Index

            self.image = self.images[self.index]
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0

        # 좌우 위치값 변경, 이동
        self.rect.x += self.velocity_x
        self.position[0] += self.velocity_x


class Bullet(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Bullet, self).__init__()
        self.image=pygame.image.load('sources/attack/bullet.png')
        size = (2,7)
        self.rect = pygame.Rect(position, size)


    def update(self, mt):
        self.rect.y -= 5

class Effect(pygame.sprite.Sprite):

    def __init__(self, position, direction):
        super(Effect, self).__init__()
        size = (23,23)

        images = []
        images.append(pygame.image.load('sources/attack/effect1.png'))
        images.append(pygame.image.load('sources/attack/effect2.png'))
        images.append(pygame.image.load('sources/attack/effect3.png'))
        images.append(pygame.image.load('sources/attack/effect4.png'))
        images.append(pygame.image.load('sources/attack/effect5.png'))
        images.append(pygame.image.load('sources/attack/effect6.png'))

        self.rect=pygame.Rect(position, size)

        self.images = images

        self.images_left = self.images
        self.images_right = [pygame.transform.flip(image, True, False) for image in images]

        self.direction = direction

        self.index = 0
        self.image = self.images[self.index]

        self.animation_time = round(100 / len(self.images * 100), 2)

        self.current_time = 0

    def update(self,mt):

        if self.direction == 'right':
            self.images = self.images_right
        elif self.direction == 'left':
            self.images = self.images_left

        self.current_time += mt*10



        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index += 1
        if self.index == len(self.images):
            self.kill()
            self.index -= 1

        self.image = self.images[self.index]






def main():
    # player 생성
    player = Character(position=(100, 385))
    # 생성된 player를 그룹에 넣기
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    running = True
    while running:
        # 각 loop를 도는 시간. clock.tick()은 밀리초를 반환하므로
        # 1000을 나누어줘서 초단위로 변경한다.

        mt = clock.tick(60) / 2000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.direction = "right"
                    player.state = 1
                elif event.key == pygame.K_LEFT:
                    player.direction = "left"
                    player.state = 1

                elif event.key == pygame.K_SPACE:
                    player.state = 2
                    if player.direction == "left":
                        bullet = Bullet(player.position)
                        all_sprites.add(bullet)
                        effect=Effect((player.position[0]-20, player.position[1]-12), player.direction)
                        all_sprites.add(effect)
                    elif player.direction == "right":
                        bullet = Bullet(((player.position[0]+40), player.position[1]))
                        all_sprites.add(bullet)
                        effect = Effect((player.position[0]+40, player.position[1]-12), player.direction)
                        all_sprites.add(effect)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.velocity_x = 0
                    player.state = 0
                elif event.key == pygame.K_SPACE:
                    player.velocity_x = 0

        # all_sprites 그룹안에 든 모든 Sprite update
        all_sprites.update(mt)
        # 배경색
        SCREEN.blit(background, (0,0))
        # 모든 sprite 화면에 그려주기
        all_sprites.draw(SCREEN)
        pygame.display.update()


if __name__ == '__main__':
    main()