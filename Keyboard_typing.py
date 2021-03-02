import pygame

  pygame.init()

 screen = pygame.display.set_mode((500, 300))

 pygame.display.set_caption("키 이벤트!")
clock = pygame.time.Clock()
run = True

  while run:
    #pygame.event.get() : 키를 눌렀을때 이벤트
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #esc 누르면 종
                run = False

      #pygame.key.get_pressed() - 전체 키배열중 현재 눌려져있는 키를 bool형식의 튜플로 반환
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] :
        print("왼쪽 키 누르기")
    elif keys[pygame.K_RIGHT] :
        print("오른쪽 키 누르기")
    elif keys[pygame.K_UP] :
        print("위 키 누르기")
    elif keys[pygame.K_DOWN] :
        print("아래 키 누르기")

      screen.fill(pygame.color.Color(255,255,255))
     pygame.display.flip()
    clock.tick(60) 
pygame.quit()