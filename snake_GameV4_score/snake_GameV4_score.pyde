import snake
import apple
import scoreboard
import random


def setup():
    size(800,600)
    global snake,lst_snake,mysnake,lenth,myapple,apples,num_apples,y,sb
    #SCOREBOARD CLASS CALL
    sb = scoreboard.ScoreBoard()
    sb.reset()
   
    lst_snake = []
    apples = []
    num_apples = 3
    lenth = 2
    y = 100
    for i in range(lenth):
        mysnake = snake.Snake(i,y)
        mysnake.id = i
        lst_snake.append(mysnake)
        
    for i in range(num_apples):
        myapple = apple.Apple(i,y)
        myapple.id=i
        apples.append(myapple)
        
        
        

def draw():
    global lst_snake,lenth,sb
    background(255)
    fill(255,0,0)
    drawSnake()
    #printx()
    for i in range(len(lst_snake)):
        lst_snake[i].Fellow(lst_snake[i-1].oldx,lst_snake[i-1].oldy)
    isApple_eaten()
    for i in range(len(apples)):
        apples[i].draw_apple()
    
    #draw scoreboard 
    sb.draw_score()
           
 

def deletapple():
     global apples,lst_snake
     for i in range(len(apples), 0, -1):
        if apples[i-1].eaten == True:
            apples.pop(i-1)
            print("apple pop")
            
            

def isSnakeHit():
    #if the head of snake hit the snake body you lose 
    #reset the curent score
    sb.reset()        
def isApple_eaten():
    global apples,lst_snake,lenth,sb
    for i in range(len(apples)-1, -1, -1):
        #print(" laste snake X",lst_snake[-1].x+lst_snake[-1].sz)
        #and apples[i].active == True
        if apples[i].eat_test(lst_snake[0].x, lst_snake[0].y) :
            deletapple()
            add_snake()
            sb.score()
            print("snake N :",lst_snake[0].id,"/",len(apples),"==>",lenth)
            

def drawSnake():
    global lenth
    for i in range(len(lst_snake)):
        lst_snake[i].draw_snake()
        lst_snake[i].move_snake()
        

def add_snake():
    
    global lst_snake,lenth,y,var
    # get pos of the first snake
    b = -1*lst_snake[-1].x/50
    y = lst_snake[-1].y
    print("last snake PosY",(lst_snake[-1].y))
    print("last snake PosX",(lst_snake[-1].x))
    #for i in range(lenth+1):
    newsnake = snake.Snake(b,y)
    newsnake.id = lst_snake[-1].id+1
    print("newposX:",newsnake.x)
    newsnake.draw_snake()
    newsnake.move_snake()
    lst_snake.append(newsnake)    
    print(len(lst_snake))

# def gen_apples():
#     #if 
    
# def printx():
#     if frameCount % 30 == 0:
#         print("last snake PosX",(lst_snake[-1].x))  
           
        
        

            

                
                
               
                
               
                
             
        
       
  
                
