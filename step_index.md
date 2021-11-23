#Fathu's code
#p1_turn
#p2_turn
#take turns using while loop
import random
class p1_turn():
    def __init__(self,index):
        self.index = index
    def check_index(self):
        if self.index in [1,4,7,9,10,32,45,78]:
            print("snake")
        elif self.index in [3,12,15,35,49]:
            print("ladder")
        else:
            pass
    def roll_dice(self):
        start = input("Start?: ")
        if start != "0":
            pass
        else:
            print("DIE")
        die_num = int(random.randint(1, 6))
        self.index = self.index + die_num
        print(self.index)
        return

class p2_turn():
    def __init__(self, index):
        self.index = index
    def check_index(self):
        if self.index in [1, 4, 7, 9, 10, 32, 45, 78]:
            print("snake")
        elif self.index in [3, 12, 15, 35, 49]:
            print("ladder")
        else:
            pass
    def roll_dice(self):
        start = input("Start?: ")
        if start != "0":
            pass
        else:
            print("DIE")
        die_num = int(random.randint(1, 6))
        self.index = self.index + die_num
        print(self.index)
        return

hi = True
end = 0
p1 = p1_turn(1)
p2 = p2_turn(1)
while end == 0:
    if hi == True:
        p1.roll_dice()
        print("p1 turn done")
        hi = False
    else:
        p2.roll_dice()
        print("p2 turn done")
        hi = True
