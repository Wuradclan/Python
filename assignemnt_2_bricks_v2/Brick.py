class Brick:
    
            
    def __init__(self, pos_x, pos_y, w, h, active, bcolor):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        #self.active = True
        self.active = active
        self.hit = False
        self.col = bcolor
    
    def hit_test(self, x, y):
        # Returns true if the coordinate x, y is within the brick.\
        if x < (self.pos_x+self.w+10) and x > self.pos_x-10 and y < (self.pos_y+self.h+10) and y > self.pos_y-10 and self.active == True:
            self.active = False
            self.hit = True
        #print(self.active)
        
    def drawbrick(self):
        # Draws the brick on the screen
        self.bcol = int(self.col)
        fill(self.bcol)
        rect(self.pos_x, self.pos_y, self.w, self.h)
        
        
