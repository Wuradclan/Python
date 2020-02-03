class Ball:
    #global x,y
    
    def __init__(self):
        
        # self.pos_x = pos_x
        # self.pos_y = pos_y
        self.speed_x = 10
        self.speed_y = 10
        self.x = 250
        self.y = 500
        self.sz = 20
        self.ball_released = False

    def update(self,x,px,win):
        # updates the position of the ball according to game physics.
        
        #ball fixed untill we pressed the mouse button to release the ball
        if mousePressed and mouseButton == LEFT :
            self.ball_released = True
        if self.ball_released == False:
            #copied code for moving ball by buttons
            
            self.x = x
            self.y = height * 0.9-self.sz/2
     
        if self.ball_released == True:
            self.x -= self.speed_x
            self.y -= self.speed_y
            if self.x > width - (self.sz/2)-10:
                self.speed_x *= -1
            if self.x < (self.sz/2)+10 :
                self.speed_x *= -1
            if self.y > height * 0.9-10 and self.x > px and self.x < px+80:
                self.speed_y*= -1
                #self.speed_x*= -1
            if self.y > height - (self.sz/2)-20 and win == False:
                self.Gameover()
                #self.speed_y*= -1
            if self.y < (self.sz/2)+35 :
                self.speed_y*= -1
        
        
        # self.show()
        
    def Gameover(self):
        
        fill(252, 23, 3);
        textSize(90);
        text("YOU LOSE", (width/2)-200, height/2);
        
        
        
    def show(self):
        # Draws the ball on the screen
        
        circle(self.x,self.y,self.sz)
