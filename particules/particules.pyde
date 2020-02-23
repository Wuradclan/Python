import particule
def setup():
    size(500,500)
    global p,ps,s
    ps = []
    s = sqrt(width**2+height**2)
    #p = particule.Particle()
    #p.randomize()
    for i in range (10):
         p = particule.Particle()
         ps.append(p)
         ps[i].randomize()

    
def draw():
    background(0)
    
    stroke(255)
    global p,ps
    for j in range(len(ps)):
        ps[j].draw_it()
        ps[j].move()
        for i in range(len(ps)-1):
            d= dit(ps[i],ps[i+1])
            m =  255-map(d,0,s,100,255)
            print m
            stroke(m)
            line(ps[j].x,ps[j].y,ps[i].x,ps[i].y)
   

def dit(a,b):
    d = dist(a.x,a.y,b.x,b.y)
    return d

  
