
import points
def setup():
    size(1500,500)
    frameRate(24)
    global p,ps,s,x,y
    d = 50
    y = height/2
    ps = []
    s = sqrt(width**2+height**2)
    #p = points.Points(50,y,1)

    for i in range (width/d):
        p = points.Points(i,i,d)
        # if i%2 == 0:
        #     p = points.Points(i,i,d)
        # else:
        #     #p = points.Points(i,-(height)+i,d)
        #     p = points.Points(i,height/2+i,d)
        ps.append(p)


    
def draw():
    background(0)
    fill(255)    
    stroke(255)
    strokeWeight(1)
    
    global p,ps

    #p.draw_it()
    #p.movesin()
    for j in range(len(ps)):
            
        for i in range(len(ps)-1):
            di= dit(ps[i],ps[j])
            m = map(di,50,400,100,0)
            #print m
            colorMode(HSB,360,100,100)
            stroke(200,100-m,m,m)
            line(ps[i].x,ps[i].y,ps[j].x,ps[j].y)

        ps[j].movesin()
        ps[j].draw_it()
    # draw lines from each point to mouse position 
    for i in range(len(ps)):
        dim = ditMouse(ps[i])     
        # for i in range(len(ps)-1):
        #di= dit(ps[i],ps[j])
        mm = map(dim,50,400,100,0)
        #print m
        colorMode(HSB,360,100,100)
        if mousePressed:
            
            stroke(33,100-mm,mm)
            line(ps[i].x,ps[i].y,mouseX,mouseY)
        else :
            stroke(100,100-mm,mm,mm)
            line(ps[i].x,ps[i].y,mouseX,mouseY)

   

def dit(a,b):
    d = dist(a.x,a.y,b.x,b.y)
    #print d
    return d

def ditMouse(a):
    d = dist(a.x,a.y,mouseX,mouseY)
    #print d
    return d

  
