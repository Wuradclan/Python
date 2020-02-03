import Ball
import Brick
import random

x = 0

MouseMove = False
FirstTime = True
lpointX = list()
lpointY = list()
lSz = list()

black_rect_height = 25
grey_frame_width = 8
blue_grey_height = black_rect_height + grey_frame_width

pannel_red_width = 100
pannel_grey_width = 80
pannel_height = 20

def setup():
     #config ball and brick
    brick_h = 50
    brick_w = 100
    global myball
    global mybrick
    global myshape
    myshape="__x____x_____x__x_____xxxxxx___xx_xx_xx_xxxxxxxxxxx_xxxxxx_xx_x____x_x___xxxx_______xx____"
           #"__x____x_____x__x_____xxxxxx___xx_xx_xx_xxxxxxxxxxx_xxxxxx_xx_x____x_x___xxxx_______xx____"
           #"xxxxxxxxxx____xx________xx________xx________xx________xx________xx________xx________xx____"
    global listshape
    listshape=[]
    active= False
    for i in myshape:
        listshape.append(i)
    for i in range(len(listshape)):
        if listshape[i]=="x":
            listshape[i]=True
        if listshape[i]=="_":
            listshape[i]=False
    print(listshape)
    print(len(listshape))
 
    myball = Ball.Ball()
    #mybrick = Brick.Brick(0,0,brick_w,brick_h,random.random)
    
    #draw the bricks
    space = 1
    brick_width = ((width - grey_frame_width *2) / 10) + 0.3
    brick_height = brick_width / 2
    global bricks
    bricks=[] 
    global hitbricks
    hitbricks=[]
    global activebricks
    activebricks=[]
    global active
    for j in range (9):
        for i in range(10):
            fill(random.randint(240, 255), random.randint(10, 50), random.randint(10, 50))
            stroke(0,0,0)
            #rect((grey_frame_width + space) + i * (brick_width), blue_grey_height + j * (brick_height), brick_width - space, brick_height-space)
            
            #draw instanciate brick and draw the bricks
            mybrick = Brick.Brick((grey_frame_width + space) + i * (brick_width), blue_grey_height + j * (brick_height), brick_width - space, brick_height-space,listshape[j*10+i],225)
            bricks.append(mybrick)
            print(bricks[j*10+i].active)
            if bricks[j*10+i].active==True:
                activebricks.append(bricks[j*10+i])
                
            # mybrick.hit_test(myball.x,myball.y)
            # print(bricks[j*10+i].active)
            # if bricks[j*10+i].active==True:
            #     mybrick.drawbrick()
    
   
    background(0)
    size(600, 800)
    global x
    x = width / 2 - pannel_red_width / 2
    frameRate(50)
        
def draw_rect_grey():
    fill(119, 117, 125)
    rect(0, black_rect_height, width, height - black_rect_height)

def draw_rect_blue():
    fill(23, 15, 87)
    rect(grey_frame_width, blue_grey_height, width - grey_frame_width * 2, height - blue_grey_height)

def draw_rect_small_red():
    fill(240, 10, 10)
    stroke(0)
    rect(grey_frame_width, blue_grey_height,(width - grey_frame_width * 2) / 10, (width - grey_frame_width * 2) / 10 / 2)

def draw_sparkle():
    noFill()
    stroke(255)
    rect(-4, -4, 8, 8)

def draw_star():
    global lpointX 
    global lpointY 
    global lSz

    col2 =- 1676082
    FirstTime = False
    for i in range(1):
        x = map(random.random(), 0, 1, 8, 580)
        y = map(random.random(), 0, 1, 40, 600)
       
        if get(int(x), int(y)) == col2:
            continue
        pushMatrix()
        translate(x, y)
        sz = map(random.random(), 0, 1 , 0.5, 1)
        
        scale(sz, sz)
        draw_sparkle()
        popMatrix()
        lpointX.append(x)
        lpointY.append(y)
        lSz.append(sz)
    
    for i in range(len(lpointX) - 1):
        x = lpointX[len(lpointX) - i - 1]
        y = lpointY[len(lpointX) - i - 1]
        if get(int(x), int(y)) == col2:
            continue
        pushMatrix()
        translate(x, y)
        sz = lSz[len(lpointX) - i - 1]
        scale(sz - 0.4, sz - 0.4)
        draw_sparkle()
        popMatrix()
        
    if len(lpointX) > 100:
        lpointX.pop(0)
        lpointY.pop(0)
        lSz.pop(0)
        
def draw():
    global x
    global MouseMove
    global mybrickstatus

    time = millis()
    delta = 5
    


    draw_rect_grey()
    draw_rect_blue()
    draw_star()
    global bricks
    global hitbricks
    hitbricks=[]
    global activebricks
    
    global win
    global result
    result = 0
    global res
    res = 0
    win = False
    
    for j in range (9):
        for i in range(10):
            fill(random.randint(240, 255), random.randint(10, 50), random.randint(10, 50))
            stroke(0,0,0)
            #rect((grey_frame_width + space) + i * (brick_width), blue_grey_height + j * (brick_height), brick_width - space, brick_height-space)
            
            #test the hit test for every frame for every brick and draw the brick if the active is True
            bricks[j*10+i].hit_test(myball.x,myball.y)
            #bricks.append(mybrick)
            if len(hitbricks)>0 :
                print(len(hitbricks))

            if bricks[j*10+i].active==True:
                bricks[j*10+i].drawbrick()
                
            if bricks[j*10+i].hit==True and bricks[j*10+i].active==False :
                hitbricks.append(bricks[j*10+i])
                result = int(len(hitbricks))

    if len(hitbricks)==len(activebricks):        
        global win
        win = True
        youwin() 
            


    if keyPressed:
        if keyCode == LEFT:
            x-=delta
        if keyCode == RIGHT:
            x+=delta
        MouseMove=False
    else:
        if mousePressed:
            if mouseButton == LEFT:
                MouseMove=True
                
    if MouseMove:
        x=mouseX 

    if x > width - grey_frame_width - pannel_red_width:
        x = width - grey_frame_width - pannel_red_width
    if x < grey_frame_width:
        x = grey_frame_width
    bx=x+(pannel_red_width/2)

    pannel(x)
     # draw the ball
    myball.show()   
    myball.update(bx,x,win)
    Myresult()
    
def Myresult():
    global result
    fill(0, 102, 153);
    textSize(25);
    text(result, 20, 650);
    text(" / ",45,650); 
    text(len(activebricks),70,650);
             
def youwin():
    fill(3, 169, 252);
    textSize(90);
    text("You Win", (width/2)-200, height/2);
        
def pannel(x):
    
    fill(255, 51, 0)
    rect(x, height * 0.9, pannel_red_width, pannel_height, 10, 10, 10, 10)
    fill(119, 117, 125)
    rect(x + 10, height * 0.9, pannel_grey_width, pannel_height)
