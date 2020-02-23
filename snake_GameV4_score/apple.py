import random
class Apple:
    def __init__(self,x,y):
        self.x = x*300+250
        self.y = y
        #size of teh apple = ridus of the cicle
        self.sz = 25
        self.active = True
        self.eaten = False
        self.id = 0
                
    def draw_apple(self):
        if self.eaten == False:
            #background(255)
            fill(255,0,0)
            ellipseMode(CENTER)
            ellipse(self.x,self.y,self.sz,self.sz)
            fill(255)
            #printinh the id of each part of the snake
            textSize(14);
            text(self.id, self.x, self.y)
            #circle(self.x,self.y,self.sz)
            #print("appleX: ",self.x)
            
    def eat_test(self, x, y):
        sz = 50
        # Returns true if the coordinate x, y is within the brick.\
        #if x < (self.x+sz) and x > self.x-sz and y < (self.y+self.sz+sz) and y > self.y-sz and self.active == True and self.eaten == False:
        if x < (self.x+sz) and x > self.x-sz and y < (self.y+sz) and y > self.y-sz :
            self.eaten = True
            self.active = False
            return self.eaten
        
    def randX(self):
        xs =[]
        for i in range(50,800,50):
            xs.append(i)
        rx = random.choice(xs)
        return rx
    
    #destroy the instance of the apple after being eaten
    def kill(self):
        del self
