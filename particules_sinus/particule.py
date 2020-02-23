class Particle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sz = 10
        # V for velocity  vilocity x (-5, 5)
        self.v_x = 0
        self.v_y = 0
        
    def randomize(self):
        # should randomize position x from 0 to width
        self.x = random(0,width)
        # position y from 0 to height
        self.y = random(0,height)
        # velocity x from -5 to 5
        self.v_x = random(-5,5)
        # velocity y from -5 to 5
        self.v_y = random(-5,5)
        pass

    def move(self):
        # Should move the particle according to its velocity.
        self.x += self.v_x
        self.y += self.v_y
        # Should wrap around the screen if off limits.
        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0
            
        if self.x < 0:
             self.x = width
        if self.y < 0:
             self.y = height
        pass
    
    def draw_it(self):
        # Should draw a circle where the particle is.
        fill(255)
        circle(self.x,self.y,self.sz)
        pass
