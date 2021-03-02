# Mouse_position
---
개요
---
키보드를 누른 위치를 알수 있는 프로그램.

---
1. 가장 먼저 Python을 설치를 해야 합니다. 
[Python 설치 링크](https://www.python.org/)

2. 콘솔창에 아래와 같은 Python 모듈을 설치해야 합니다.
```
> pip install pygame
```
3.실행 취소는 Ctrl-C누르면 실행이 자동으로 취소가 됩니다.

---

  #pygame.event.get() : 키를 눌렀을때 이벤트
```
 while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
```
 #pygame.key.get_pressed() - 전체 키배열중 현재 눌려져있는 키를 bool형식의 튜플로 반환
```
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] :
        print("왼쪽 키 누르기")
    elif keys[pygame.K_RIGHT] :
        print("오른쪽 키 누르기")
    elif keys[pygame.K_UP] :
        print("위 키 누르기")
    elif keys[pygame.K_DOWN] :
        print("아래 키 누르기")
```

참고 자료
---
[GUI 자동화를 통해 키보드 및 마우스 제어 자료](https://automatetheboringstuff.com/chapter18/)
