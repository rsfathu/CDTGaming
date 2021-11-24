
import random 

class logic :
    def __init__(self,index1,index2,player,correctanot,currentpts,dictionary,key,data_set):
        self.index1 = index1
        self.index2 = index2
        self.player = player
        self.correctanot = correctanot
        self.currentpts = currentpts 
        self.dict = dictionary 
        self.key = key
        self.set = data_set
           


    ### Dice
    def dice(self):
        a = random.randint(1,6)
        return a


    ### End game once either player wins
    def endgame(self):
        if self.index1 >= 100:
            return True


        elif self.index2 >= 100:
            return True

        else:
            return False 

    ### No. of points 
    def addpoints(self):
        if self.correctanot:
            self.currentpts = self.currentpts + 1
        elif self.correctanot == False:
            pass
        else:
            return None ### fullproof code in case input is neither True/False
        return (self.player, self.currentpts) ### use tuple to reduce hacking risks as values is not mutable



    ### Returning set from key
    def returnkeyset(self):
        self.set = self.dict[self.key]
        return self.set

    ### Extracting Questions
    def extractqn(self):
        qn = "{}".format(self.set[0][0])
        return qn

    ### Extracting MCQ options
    def extractmcq(self):
        qn = "{}".format(self.set[0][0])
        op1 = "{}".format(self.set[1][0])
        op2 = "{}".format(self.set[1][1])
        op3 = "{}".format(self.set[1][2])
        op4 = "{}".format(self.set[1][3])
        return qn, op1, op2, op3, op4

a = logic()

a,b,c,d,e = extractmcq([["question"],[1,2,3,4],[1]])
print(a,b,c,d,e)

