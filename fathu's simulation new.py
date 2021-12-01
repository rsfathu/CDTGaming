#Fathu's turn simulator
import random
class p1_turn():
    def __init__(self,index):
        self.index = index
    def bot_left(self):
        j = self.index % 20
        if j > 0 and j < 11:
            x = 60 * (j-1)
        elif j == 0:
            x = 0
        else:
            x = 540 - 60 * (j - 11)
        m = x + 30
        k = int((self.index-1)/ 10)
        y = 600 - 60 * k
        n = y - 30
        return x, y, m, n
    def roll_dice(self):
        start = input("P1's turn go: ")
        if start != "0":
            pass
        else:
            print("DIE")
        die_num = int(random.randint(1, 1))
        self.index = self.index + die_num
        print(self.index)
        return

class p2_turn():
    def __init__(self, index):
        self.index = index
    def bot_left(self):
        j = self.index % 20
        if j > 0 and j < 11:
            x = 60 * (j-1)
        else:
            x = 540 - 60 * (j - 11)
        m = x + 30
        k = int(self.index / 20)
        y = 600 - 120 * k
        n = y - 30
        return x, y, m, n
    def roll_dice(self):
        start = input("P2's turn go: ")
        if start != "0":
            pass
        else:
            print("DIE")
        die_num = int(random.randint(1, 1))
        self.index = self.index + die_num
        print(self.index)
        return

def snake():
    print("You stepped on snake! Ans this qn")
    print(easyqn_dic['E4Q'])

def ladder():
    print("You stepped on ladder! Ans this qn")
    print(easyqn_dic['E5Q'])

def surprise():
    print("You stepped on surprise! Ans this qn")
    print(easyqn_dic['E6Q'])

snake_dc = {
    4:1,
    7:3 ,
    9:6,
    21:5,
    32:20,
    45:30,
    78:40,
    99:54,
}

ladder_dc = {
    3:18,
    12:27,
    15:29,
    35:50,
    49:75,
}

surprise_dc = [
    2,11,24,26,37,33,43,51,61,97
]

easyqn_dic = {

'E1Q' : 'What is the fastest animal in the world?',
'E1S' : ['Tiger', 'Cheetah', 'Puma', 'Peregrine Falcon'],
'E1A' : 'Peregrine Falcon',

'E2Q' : 'What is the year the First World War ended?',
'E2S' : ['', '', '', ''],
'E2A' : '1918',

'E3Q' : 'What is the smallest planet in our solar system?',
'E3S' : ['Pluto', 'Jupiter', 'Mercury', 'Saturn'],
'E3A' : 'Pluto',


'E4Q' : 'When did the SARS outbreak occur?',
'E4A' : '2002',

'E5Q' : 'How many continents are there in the World?',
'E5S' : ['6', '7', '8', '9'],
'E5A' : '7',

'E6Q' : 'How many states are there in the United States?',
'E6A' : '50',

'E7Q' : 'Where are the Himalayans located?',
'E7S' : ['India', 'Nepal', 'China', 'Russia'],
'E7A' : 'India',

'E8Q' : 'How many playing cards are there in a regular deck?',
'E8A' : '52',
}

hi = True
end = 0
p1 = p1_turn(1)
p2 = p2_turn(1)
while end == 0:
    if hi == True:
        p1.roll_dice()
        print(p1.bot_left())
        """
        if p1.index in snake_dc:
            snake()
        elif p1.index in ladder_dc:
            ladder()
        elif p1.index in surprise_dc:
            surprise()
        else:
            """
        print("p1 turn done")
        #hi = False
    else:
        p2.roll_dice()
        """
        if p2.index in snake_dc:
            snake()
        elif p2.index in ladder_dc:
            ladder()
        elif p2.index in surprise_dc:
            surprise()
        else:
            """
        print(p2.bot_left())
        print("p2 turn done")
        hi = True