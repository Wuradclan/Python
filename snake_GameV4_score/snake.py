class Snake:
    def __init__(self,x,y):
        self.sz = 50
        # -x to position the new parts behine the old one starting from right to left and direction is left to right
        self.x = -x*self.sz
        self.y = y
        self.id = 0
        self.oldx = self.x
        self.oldy = self.y
        self.direction = "right"

        
    def draw_snake(self):
       
        fill(0)
        rectMode(CENTER)
        #if the snake part is the first one = 0 then round the corner of the recangle dipending of the direction by caling draw head function
        if self.id==0 :
            textSize(14);
            self.drawhead()
            fill(255)
            #printinh the id of each part of the snake
            
        else:
            #drawing the rest of the parts of the snake as rectangles
            rect(self.x,self.y,self.sz,self.sz)
            fill(255)
            #printinh the id of each part of the snake
            textSize(14);
            text(self.id, self.x, self.y)
            
       
        
     #function to move the rest of the snake fellowing the head each block fellow the past part    
    def Fellow(self,oldx,oldy):
        if self.id!=0:
            #if frameCount % 30 == 0:
            self.x=oldx
            self.y=oldy
            
    
            
    def move_snake(self):
        self.hitwalls()

        if key == "d" and self.direction != "left":
            self.direction = "right"
        if key == "a" and self.direction != "right":
            self.direction = "left"
        if key=="w" and self.direction != "down":
            self.direction = "up"
        if key== "s" and self.direction != "up":
            self.direction = "down"
        if keyCode == RIGHT and self.direction != "left":
            self.direction = "right"
        if keyCode == LEFT and self.direction != "right":
            self.direction = "left"
        if keyCode == UP and self.direction != "down":
            self.direction = "up"
        if keyCode == DOWN and self.direction != "up":
            self.direction = "down"
            
        if frameCount % 30 == 0:
            if self.direction == "right" :
                
                self.oldx = self.x
                self.oldy = self.y
                #self.hitwalls()
                self.x += self.sz
                
            
                
            if self.direction == "left":
                self.oldx = self.x
                self.oldy = self.y
                #self.hitwalls()
                self.x -= self.sz
                
                
            if self.direction == "up":
                self.oldx = self.x
                self.oldy = self.y
                #self.hitwalls()
                self.y -= self.sz
                
                
            if self.direction == "down":
                self.oldx = self.x
                self.oldy = self.y
                #self.hitwalls()
                self.y += self.sz
                
                
    # check if  the head snake hit the walls 
    def hitwalls(self):
        if self.id == 0:
            if self.x+self.sz > width-50:
                self.x = width
                
            if self.x < 0 :
                self.x = 0
            if self.y+self.sz > height:
                self.y = height
            if self.y-self.sz < 0:
                self.y = 0
           
    def drawGameover(self)                    
    #drwa the corner of the head dipening of its direction
    def drawhead(self):
        r=3
        h=30
        if self.direction =="right":
            rect(self.x,self.y,self.sz,self.sz,r,h,h,r)
            fill(255)
            text(self.id, self.x, self.y-8)
            text(self.id, self.x, self.y+8)
        if self.direction =="left":
            rect(self.x,self.y,self.sz,self.sz,h,r,r,h)
            fill(255)
            text(self.id, self.x, self.y-8)
            text(self.id, self.x, self.y+8)
        if self.direction =="up":
            rect(self.x,self.y,self.sz,self.sz,h,h,r,r)
            fill(255)
            text(self.id, self.x-8, self.y)
            text(self.id, self.x+8, self.y)
        if self.direction =="down":
            rect(self.x,self.y,self.sz,self.sz,r,r,h,h)
            fill(255)
            text(self.id, self.x-8, self.y)
            text(self.id, self.x+8, self.y)
    
        
