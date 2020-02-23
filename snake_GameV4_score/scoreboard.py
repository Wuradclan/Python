class ScoreBoard:
    
    def __init__(self):
        self.currentScore = 0
        self.highScore = 0
    
    # reset score function     
    def reset(self):
        self.currentScore = 0
        
    # increment current score function by +1     
    def score(self):
         self.currentScore+=1
         if self.currentScore > self.highScore:
             self.highScore+=1
    
    # draw the scorebaord function      
    def draw_score(self):
        fill(0)
        
        textSize(50)
        text(self.currentScore, 50, 50);
        text(self.highScore, width-100, 50);
        
        
    
