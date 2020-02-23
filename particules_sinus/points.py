class Points:
    
    def __init__(self,x,y,d):
        
        self.x = x*d
        self.y = y*d
        self.sz = 10
        # V for velocity  vilocity x (-5, 5)
        self.v_x = 1
        self.v_y = 1
        self.d = d
        self.a = self.y
        

    def move(self):
        # Should move the particle according to its velocity.
        #self.x += self.v_x
        print("YY:",self.y)
        di = height/2 - self.y
        print(di)
        v = float(map(di,0,height/2-40,1,1.5))
        print("V :",v)
        self.y += v
        # Should wrap around the screen if off limits.
        # if self.y <= 100:
        #     self.y += v
        # if self.y >= 350:
        #     self.y -= v
        pass
        
    def movesin(self):
        # controle the speed y 1250 ideal 
        inc = TWO_PI/ 1250
        if mousePressed:
            inc = TWO_PI/100
    
        #maping pos Y to  a0.

        # Should move the particle according to its velocity.
        self.y = height/2- sin(self.a)*150.0
        self.a += inc
        print(self.a)
        
        pass
    
    def draw_it(self):
        # Should draw a circle where the particle is.
        fill(0, 88, 115)
        circle(self.x,self.y,self.sz)
        pass
