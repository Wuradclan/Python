char_width =20

def setup():
    size(400, 400)
    
def draw():
    
    for i in range(width/char_width):
        for j in range (height/char_width):
                import random
                r= random.randint(0,1)
                                
                draw_slash(r,char_width * i,char_width * j)            
                
    noLoop()
    SaveFrame('screenshot.png')
# pip install pyautogui    
# import pyautogui

# pic= pyautogui.screenshot()

# pic.save('screenshot.png')

        
def draw_slash(fwd_slash,top,left):
  if fwd_slash:
        line(top,left+char_width/2,top+char_width,left+char_width/2)
  else : 
        line (top+char_width/2,left,top+char_width/2,left+char_width)


    # draw_slash(1,20,20)
    # draw_slash(0,20,20)
