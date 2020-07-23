import pygame,sys,time,math,random
from scripts.color import *
from scripts.texture import *
from scripts.globals import *
from scripts.Timer import *
from randomgen import *

#Initialize Pygame
pygame.init()

#CLock Setup
clock=pygame.time.Clock()

#FPScount Function
def count_fps():
    global FPS
    FPS=clock.get_fps()
    if FPS>0:
        Globals.deltatime=1/FPS


#Window Setup    
font=pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)
pygame.display.set_caption("BallSwing")
window=pygame.display.set_mode((400,600),pygame.HWSURFACE|pygame.DOUBLEBUF)
scene="menu"


    
#BAckGround Variables
x=0
screenHeight=600

#CLock Variables
#tck=200
#count=1
#myTime=1

#Window Loop VAriable
isRunning=True
count=0

#Timer Setup
myTimer=Timer(1)
myTimer.Start()
ObsTimer=Timer()
ObsTimer.Start()
#Movement Variables
pos=300
move=100
swing=False
done=False

#Running Loop
while isRunning:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            isRunning=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            swing = not swing
    #if count%100==0:
        #myTime+=1
    #if myTime%29==0:
        #tck+=.01

    #Timer Time.IncSeconds
    myTimer.Update()
    ObsTimer.Update()
    Time=int(ObsTimer.Value)

    if Time==16:
        ObsTimer.Value=0
        done=False
    #Tick Update 
    if (int(myTimer.Value+1))%5==0:
        pass

    #BackGroundSetup
    back=TextureTags["3"]
    back2=TextureTags["3"]
    obx=random.randrange(150,250)
    #random.choice((150,157,198,176,166,240,192,234,230,245,184,215,223,246,188,164,175,197,250))
    i=str(random.randrange(1,3))
    j=random.choice((back,back2))
    #Count
    count+=1
    print(Time)

    #BackGround
    if Time==15 and done==False:
        j.blit(TextureTags[i],(obx,0))
        window.blit(back,(0,x))
        window.blit(back2,(0,x-screenHeight))
        x=x+1
        print("hi")
        done=True
        
        if x==screenHeight:
            x=0
    else:
        window.blit(back,(0,x))
        window.blit(back2,(0,x-screenHeight))
        x=x+1
        if x==screenHeight:
            x=0

    #Player Movement
    if move<300 and swing==False:
        window.blit(TextureTags["4"],(pos,450))
        move+=1
        pos-=1
        if pos==100:
            swing=True
    elif move>100 and swing==True:
        window.blit(TextureTags["4"],(pos,450))
        move-=1
        pos+=1
        if pos==300:
            swing=False

    #Set Tick
    msElapsed=clock.tick(100)
    
    #window.blit(Player,(185,450))
    #Scene Selection
    if scene=="menu":
        pass
    elif scene=="pause":
        pass
    elif scene=="gameover":
        pass
    elif scene=="play":
        window.fill(Color.Black)
    #FPS COUNT
    count_fps()
    #DisplayTickIncrease
    #FPS=str(tck)
    fps_overlay=font.render(str(FPS),True,Color.Goldenrod)
    window.blit(fps_overlay,(0,0))

    #LastValue
    if myTimer.Value%15==0:
        LastValue=myTimer.Value
    #Update Display
    pygame.display.update()
    
    #for i in range(1,101):
        #if i%100==0:
            #count+=1
pygame.quit()
sys.exit()
