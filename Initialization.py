"""
To return all initial starting variables required for the game

"""

class initialization:
    def __init__(self) -> None:
        self.player1index,self.player2index,self.player1score,self.player2score =1,1,0,0
        self.endgame = False
        
    def getstartingvalues(self):
        return (self.player1index,self.player2index,self.player1score,self.player2score,self.endgame)
    