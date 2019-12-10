
def setup():
    size(500,500)

delta=10
charlenth=10
x=250
y=250

def draw():
    px=x
    py=y
    global x,y
    
    if keyPressed:
        if keyCode == RIGHT:
            x = x+delta
            
            #line(x,y,x+charlenth,y)
        if keyCode == LEFT:
            x = x-delta

        if keyCode == DOWN:
            y = y+delta
        
            #line(x,y,x,y+charlenth)
        if keyCode == UP:
            y = y-delta
if x     
    line(x,y,px,py)   
            
