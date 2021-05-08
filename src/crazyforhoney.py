import sys, pygame, random

bear = pygame.image.load('/Users/bob/Desktop/my_pygames/res/bear.png')
honey = pygame.image.load('/Users/bob/Desktop/my_pygames/res/honey.png')
coin = pygame.image.load('/Users/bob/Desktop/my_pygames/res/coin.png')
eat = pygame.image.load('/Users/bob/Desktop/my_pygames/res/eat.png')
background = pygame.image.load('/Users/bob/Desktop/my_pygames/res/background.png')

bearX = 512
bearY = 200
stepX = 0
stepY = 0
honey_speed=2
honey_objs=[]
coins_pos = []


def keydown_event(event,stepX,stepY,bear_pos):
    coin_pos = []
    if event.key == pygame.K_RIGHT:
        stepX = 5
    elif event.key == pygame.K_LEFT:
        stepX = -5
    elif event.key == pygame.K_UP:
        stepY = -5
    elif event.key == pygame.K_DOWN:
        stepY = 5
    elif event.key == pygame.K_SPACE:
        coin_pos = [bear_pos[0],bear_pos[1]+10]
    return stepX, stepY, coin_pos

def honey_show(honey_objs,startY=-60):
    if len(honey_objs)<5:
        honey_X = random.randint(0,800)
        honey_pos = [honey_X,startY]
        screen.blit(honey,honey_pos)
        honey_objs.append(honey_pos)
    else:
        i = 0
        for pos in honey_objs:
            screen.blit(honey,pos)
            honey_objs[i] = [pos[0],pos[1]+honey_speed]
            i = i + 1
    return honey_objs

def distance(cx,cy,hx,hy):
    a = cx - hx
    b = cy - hy
    return math.sqrt(a*a+b*b)

def screen_border(X,Y):
    if X < 0:
        X = 0
    elif X > 1024:
        X = 1024
    if Y < 0:
        Y = 0
    elif Y > 577:
        Y = 577
    return X, Y

pygame.init()
size = weight, height = 1024, 577
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Crazy for honey")

while 1:
    coin_pos_ = []
    bearX = bearX + stepX
    bearY = bearY + stepY
    bearX,bearY = screen_border(bearX,bearY)

    screen.blit(background,(0,0))
    screen.blit(bear,(bearX,bearY))
    honey_objs = honey_show(honey_objs)

    i = 0
    for v in coins_pos:
        coins_pos[i] = [v[0],v[1]-10]
        screen.blit(coin,(coins_pos[i][0]+45,coins_pos[i][1]))
        distance_c = [coins_pos[i][0]+45,coins_pos[i][1]]
        hi = 0
        for hp in honey_objs:
            if distance(distance_c[0],distance_c[1],hp[0],hp[1]) < 60:
                screen.blit(eat,(hp[0],hp[1]))
                honey_objs[hi] = [random.randint(0,900),-50]
            hi = hi + 1
        i = i + 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            stepX, stepY, coin_pos_ = keydown_event(event,stepX,stepY,[bearX,bearY])
            if len(coin_pos_) > 0:
                coins_pos.append(coin_pos_)

    pygame.display.update()
