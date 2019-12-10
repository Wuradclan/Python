def setup():
    size(500,500)
    
# def tree():
#   triangle(15, 0, 0, 15, 30, 15)
#   #rect(0, 15, 30, 30)
#   #rect(12, 30, 10, 15)
  
# def house():
#   triangle(15, 0, 0, 15, 30, 15)
#   rect(0, 15, 30, 30)
#   rect(12, 30, 10, 15)
  
def draw():
    if mousePressed:
        fill(0)
        #circle(mouseX,mouseY,5)
        line(pmouseX,pmouseY,mouseX,mouseY)
   
    
    # for i in range (width):
    
    #     pushMatrix()
    #     translate(40*i, 40*i)
    #     house()
    #     popMatrix()  
    # noLoop()
