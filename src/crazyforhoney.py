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

def keydown_event(event,stepX,stepY):
    if event.key == pygame.K_RIGHT:
        stepX = 10
    elif event.key == pygame.K_LEFT:
        stepX = -10
    elif event.key == pygame.K_UP:
        stepY = -10
    elif event.key == pygame.K_DOWN:
        stepY = 10
    return stepX, stepY

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

pygame.init()
size = weight, height = 1024, 577
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Crazy for honey")

while 1:
    bearX = bearX + stepX
    bearY = bearY + stepY

    screen.blit(background,(0,0))
    screen.blit(bear,(bearX,bearY))
    honey_objs = honey_show(honey_objs)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            stepX, stepY = keydown_event(event,stepX,stepY)

    pygame.display.update()
