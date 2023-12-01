import pygame
import random
import os

#initialisation
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(2)



c=pygame.image.load('icon.ico')
#colors
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
yellow = (154,205,50)


#gamebox
scrht=720
scrwt=1280
gameWindow = pygame.display.set_mode((scrwt,scrht))
pygame.display.set_caption('Snake Xenzia Retro By SadharanXD')
pygame.display.set_icon(c)
pygame.display.update()
bgimg = pygame.image.load('background.jpg')
bgimg = pygame.transform.scale(bgimg,(1280,720)).convert_alpha()


#game variables
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55,bold=True,italic=True)


#game functions
def txtscreen(text,color,x,y):
    screentext=font.render(text,True,color)
    gameWindow.blit(screentext,[x,y])

def plotsnake(gameWindow,color,snakelist,snakesize):
    for x,y in snakelist:
        pygame.draw.rect(gameWindow,color,[x,y,snakesize,snakesize])

def welcome():
    fps = 144
    exitgame = False
    while not exitgame:
        gameWindow.fill(black)
        txtscreen('Welcome To Snakes!!',green,400,360)
        txtscreen('Press Enter to Play!!',green,400,400)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    exitgame = True
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('back.mp3'))
                    
                    gameloop()
                
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

#gameloop
def gameloop(): 
    
    
    
    if (not os.path.exists('highscore.txt')):
        with open('highscore.txt','w') as f:
            f.write('0')
    with open('highscore.txt','r') as f:
        highscore = f.read()
    exitgame = False
    gameover = False
    snakex = 640
    snakey = 360
    snakesize = 30
    fps = 144
    velocityx = 0
    velocityy = 0
    velocity = 2
    foodx = random.randint(20,scrwt-20)
    foody = random.randint(20,scrht-20)
    foodsize = 30
    score = 0
    snakelist=[]
    snakelength=1
    while not exitgame:
        if gameover:
            with open('highscore.txt','w') as f:
                f.write(str(highscore))

            gameWindow.fill(black)
            txtscreen('Game Over!!! Press Enter to Continue',yellow,300,360)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exitgame = True
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:    
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exitgame = True
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        # snakex+=5
                        velocityx=velocity
                        velocityy = 0
                    elif event.key == pygame.K_a:
                        velocityx=-velocity
                        velocityy = 0
                    elif event.key == pygame.K_w:
                        velocityy=-velocity
                        velocityx = 0
                    elif event.key == pygame.K_s:
                        velocityy=velocity
                        velocityx = 0
                # print(event)
            
            
            snakex+=velocityx
            snakey+=velocityy
            
            if abs(snakex - foodx)<20 and abs(snakey - foody)<20:
                score+=10
                pygame.mixer.music.load('beep.mp3')
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('beep.mp3'))
                
                # print('Score: ',score)
                foodx = random.randint(20,scrwt-20)
                foody = random.randint(20,scrht-20)
                snakelength+=5

                if score>int(highscore):
                    highscore=score
            gameWindow.fill(black)
            gameWindow.blit(bgimg,(0, 0))
            txtscreen('Score: '+str(score)  + '  High Score:'+ str(highscore),white,20,50)
            pygame.draw.rect(gameWindow,green,[foodx,foody,foodsize,foodsize])
            
            head=[]
            head.append(snakex)
            head.append(snakey)
            snakelist.append(head)
            
            if len(snakelist)>snakelength:
                del snakelist[0]
            
            if head in snakelist[:-1]:
                gameover = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            if snakex<0 or snakex>scrwt or snakey<0 or snakey>scrht:
                gameover = True
                # print('Game Over!!!')
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()


            # pygame.draw.rect(gameWindow,red,[snakex,snakey,snakesize,snakesize])
            plotsnake(gameWindow,red,snakelist,snakesize)
            
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

welcome()
input()
