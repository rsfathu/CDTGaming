from tkinter import *
from tkinter import font
from tkinter.font import names
import time
import random
"""
Below are classes defined for the tinkter pages. Welcome page and end game pages are static.
Question and Answer pages are dynamic.
Fonts: Corbel - title , Roboto - body
Colours 
f991cc- Pink
53599a- Darker blue
fee1c7- Beige
52d1dc- cyan 
110b11- midnight blue
 """
class Round:
    def __init__(self):
        self.userboolean = False # True is for Player 1, False is for Player 2
        self.player1index,self.player2index = 0,0 #This indicates player position on the board and is passed into the playing board to display
        #positions
        self.player1score,self.player2score = 0,0 #This indicates overall questions answered correctly.
        self.endgameboolean = False #Will always be false until the end turn check returns true.
        #Upon being True, the game will show the endgame frame and the next move if any, is to reset the Round.
        self.questionstring = ""
        self.mcq1,self.mcq2,self.mcq3,self.mcq4="","","",""
        self.correctans = ""
        self.useranscorrect = None #This is for the display on the answer screen.
        #above are all the variables required to run questionframemcq and to serve to the answer screen
        self.excludedlistofqns = [] #All elements in this list can not be called again.

    def reset(self):
        self.userboolean = False 
        self.player1index,self.player2index = 0,0 
        self.player1score,self.player2score = 0,0 
        self.endgame = False 
        self.questionstring = ""
        self.mcq1,self.mcq2,self.mcq3,self.mcq4="","","",""
        self.correctans = ""
        self.useranscorrect = None 
        self.excludedlistofqns = [] 
    
    def endgame(self):
        if self.index1index or self.player2index >= 100:
            self.endgameboolean = True
        else:
            return False 

"""class GUILOOP():
    def __init__(self) :
        self.roundstart = Round() #roundstart is the object for holding all information
        self.rootmaster = Tk()
        self.rootmaster.geometry("1280x720")
        self.rootmaster.configure(background="#52d1dc")
        #self.nextframe = Playingboard(self.rootmaster,10,1,'ladder',None,None)
        self.nextframe = Answerframe(self.rootmaster)
        self.start  = Introframe(self.rootmaster,self.nextframe)
        self.rootmaster.mainloop()"""
# roundstart = Round() #roundstart is the object for holding all information
# rootmaster = Tk()
# rootmaster.geometry("1280x720")
# rootmaster.configure(background="#52d1dc")
# #self.nextframe = Playingboard(self.rootmaster,10,1,'ladder',None,None)
# nextframe = Answerframe(self.rootmaster)
# start  = Introframe(self.rootmaster,self.nextframe)
# rootmaster.mainloop()
class SNLFrame():
    def __init__(self, master):
        self.master = Frame(master, width=1280 , height=720,background="#52d1dc")

    def changeframe(self,future):
        future.master.grid(row=0,column=0)
        self.master.grid_forget()
        future.master.tkraise()


class Introframe(SNLFrame):
    def __init__(self, master, greet_nextframe):
        super().__init__(master)
        master.title("Snakes and Ladders Know it All")

        self.label = Label(self.master, text="Snakes and Ladders, KNOW IT ALL!!! " , font= ("Corbel" , 42) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.label.place(x=300 , y = 200)

        self.greet_nextframe = greet_nextframe
        self.greet_button = Button(self.master, text="Let's Begin, Hajimasho!",font=("Roboto",24), padx=10 , pady=10 , command=self.greet_button_pressed)
        self.greet_button.place(x=600, y=320)

        self.close_button = Button(self.master, text="Quit Game", command=master.quit , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.close_button.place(x=1000,y=600)
        self.master.grid(row=0,column=0)
    def greet_button_pressed(self):
        self.changeframe(self.greet_nextframe)


class Endgameframe(SNLFrame):
    def __init__(self, master):
        super().__init__(master)
        master.title("Thanks for playing!")

        self.label = Label(self.master, text="Rate us on Playstore 5/5, Hope you enjoyed the game​" , font= ("Corbel" , 36) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.label.place(x=250 , y = 200)

        self.restart_button = Button(self.master, text="Restart?", command=self.restartthegame , height= 4 , width= 40 , padx= 10 , pady = 10 , font=("roboto" , 24) , background="#f991cc" , foreground="#110b11")
        self.restart_button.place(x=400 , y=320)

        self.close_button = Button(master, text="Quit Game", command=master.quit , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.close_button.place(x=1000,y=700)
    def restartthegame(self): #problem with accessing the object 
        self.roundstart.reset()
        self.changeframe(Introframe(self.rootmaster))


    
class QuestionframeMCQ :
    def __init__(self,master,mcq1 = "MCQ1 QUESTION ",mcq2="MCQ2 QUESTION ",mcq3="MCQ3 QUESTION ",mcq4="MCQ4 QUESTION ",questionlabel=" Insert something here") -> None:
        self.master = Frame(master, width=1280 , height=720,background="#52d1dc")
        master.title("Question Time!")
        self.questionlabel,self.mcq1,self.mcq2,self.mcq3,self.mcq4 = questionlabel,mcq1,mcq2,mcq3,mcq4

        #Declaration of all necessary labels
        self.qlabel = Label(self.master, text= self.questionlabel, font= ("Corbel" , 16) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.mcqbutton1 = Button(self.master, text=self.mcq1, command= None, height= 2 , width= 10 , padx= 2 , pady = 2 , font=("roboto" , 12) , background="#f991cc" , foreground="#110b11")
        self.mcqbutton2 = Button(self.master, text=self.mcq2, command= None, height= 2 , width= 10 , padx= 2 , pady = 2 , font=("roboto" , 12) , background="#f991cc" , foreground="#110b11")
        self.mcqbutton3 = Button(self.master, text=self.mcq3, command= None, height= 2 , width= 10 , padx= 2 , pady = 2 , font=("roboto" , 12) , background="#f991cc" , foreground="#110b11")
        self.mcqbutton4 = Button(self.master, text=self.mcq4, command= None , height= 2 , width= 10 , padx= 2 , pady = 2 , font=("roboto" , 12) , background="#f991cc" , foreground="#110b11")
        self.nextbutton = Button(self.master, text="Continue", command=self.nextpg("test") , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")

        #placements
        self.qlabel.place(x=200 , y=100)
        self.mcqbutton1.place(x=300,y=300)
        self.mcqbutton2.place(x=800,y=300)
        self.mcqbutton3.place(x=300,y=500)
        self.mcqbutton4.place(x=800,y=500)
        self.nextbutton.place(x=1000,y=650)


#Class below optional
class QuestionframeOPEN:
    def __init__(self,master,questionlabel = "Question to be inserted") -> None:
        super().__init__(master)
        master.title("Question Time!")
        self.questionlabel= questionlabel

        #Declaration of all necessary labels
        self.qlabel = Label(self.master, text= self.questionlabel, font= ("Corbel" , 16) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.nextbutton = Button(self.master, text="Continue", command=self.nextpg() , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.answerbox = Entry(self.master,textvariable= " HELP " , foreground="#110b11" ,font= ("roboto" , 16) , width=100 ,   )
        #placements
        self.qlabel.place(x=200 , y=100)
        self.nextbutton.place(x=1000,y=650)
        self.answerbox.place(x=100,y=300)

    def nextpg(self):
        pass
class Answerframe(SNLFrame) :
    def __init__(self,master,answerstring =" You didn't specify a question",userboolean = None, playerturn = None,player1points = 0,player2points = 0) -> None:
        super().__init__(master)
        self.answer = answerstring
        self.boolean = userboolean #this thing is a boolean that will display different messages for correct or wrong messages.
        if self.boolean == True:
            self.displaytext = "Omedetou Gozaimasu"
        elif self.boolean == False:
            self.displaytext = "Awwwwwwww...."
        else:
            self.displaytext = "Amazing you managed to find a loophole."
        #declaration
        self.answerlabel = Label(self.master,text= "ANSWER HERE",font= ("Corbel" , 36) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.nextbutton = Button(self.master, text="Continue", command=None, font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.congratulations = Label(self.master,text= self.displaytext,font= ("Corbel" , 36) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        if self.boolean == True:
            self.useriscorrect = True
        else:
            self.useriscorrect = False
        #placements
        self.answerlabel.place(x=200,y=100)
        self.congratulations.place(x=200,y=300)
        self.nextbutton.place(x=1000,y=650)

    def addpoints(self):
        if self.userboolean:
            self.currentpts = self.currentpts + 1
        elif self.correctanot == False:
            pass
        else:
            return None ### fullproof code in case input is neither True/False
        return (self.player, self.currentpts) ### use tuple to reduce hacking risks as values is not mutable
    
class Explanationframe() :
    def __init__(self,master) -> None:
        self.master = Frame(master, width=1280 , height=720,background="#52d1dc")
        super().__init__(master)
        self.explanation= """
        You roll a dice. Then you move that many steps​
        \n
        If you land upon a square with a question, you must answer it, else you will regress 1 step.​
        \n
        If you land at the bottom of the ladder, you must answer the question to proceed upwards, 
        \n
        if you land on the mouth of a snake, you must answer the question correctly to not proceed downwards.​
        \n
        The questions get increasingly tougher.​
        \n
        First to reach square 100 wins.
        \n
        """
        self.explanationheader = Label(self.master, text= "Rules As Below...", font= ("Corbel" , 32) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.explanationtext = Label(self.master,text= self.explanation,font= ("Roboto",12) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.continuebutton = Button(self.master, text="Continue", command=lambda : self.changeframe(self.nextframe), font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.continuebutton.place(x=1000,y=650)
        self.explanationtext.place(x=100,y=200)
        self.explanationheader.place(x=100,y=50,anchor="w")

class Playingboard(SNLFrame) :
    def __init__(self,master,attributes) :
        self.attributes = attributes
        self.attributes.player1position = 1
        super().__init__(master)
        self.playernumber = self.attributes.userboolean#This is the player turn indicator
        self.player1position,self.player2position = self.attributes.player1index,self.attributes.player2index
        self.variable = 0        

        #canvas grid system
        self.canvas = Canvas(self.master , width=600 , height= 600 , background="#53599a")
        def create_grid(event=None):
            w = self.canvas.winfo_width() # Get current width of canvas
            h = self.canvas.winfo_height() # Get current height of canvas
            self.canvas.delete('grid_line') # Will only remove the grid_line

            # Creates all vertical lines at intevals of 100
            for i in range(0, w, 60):
                self.canvas.create_line([(i, 0), (i, h)], tag='grid_line' , fill='white' )

            # Creates all horizontal lines at intevals of 100
            for i in range(0, h, 60):
                self.canvas.create_line([(0, i), (w, i)], tag='grid_line',fill='white')
        self.canvas.bind('<Configure>', create_grid)
        #player demarcation below
        self.canvas.create_rectangle(0,600,30,570,fill="red")



        #label declarations
        self.labeltitle = Label(self.master , text= " THE SHOWDOWN BOARD " , font=("Corbel" , 36), foreground="#110b11" , padx = 10 ,pady = 10 )
        self.player1label = Label(self.master , text="Player 1 ",font=("Corbel" ,24),background="#52d1dc")
        self.player2label = Label(self.master , text= "Player 2",font=("Corbel" ,24),background="#52d1dc")
        self.dice1 = Label(self.master , text= self.variable , background="#fee1c7" , font = ("Roboto" , 36 ),height=2 , width= 4 )
        self.dice2 = Label(self.master , text= self.variable , background="#fee1c7",height=2 , width= 4 ,font = ("Roboto" , 36 ))
        self.player1point=Label(self.master, text="Player 1 Points" , font=("Corbel" ,24),background="#52d1dc")
        self.player2point=Label(self.master, text="Player 2 Points" , font=("Corbel" ,24),background="#52d1dc")
        self.player1counter = Label(self.master, text="0" , font=("Corbel" ,24),background="#52d1dc")
        self.player2counter = Label(self.master, text="0" , font=("Corbel" ,24),background="#52d1dc")
        self.close_button = Button(self.master, text="Quit Game", command=master.quit , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.rolldicebutton = Button(self.master, text="Roll Dice", command=lambda :self.rollinganimation(playerturn) , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        #Popup system with waiting here
        self.popupsnake = Label(self.master)
        self.popupladder = Label(self.master)
        self.popupnextplayer = Label(self.master)
        self.popuprandomhit = Label(self.master)
        """if self.popuptype == 'nextplayer':
            self.popupnextplayer.place(x=300,y=300)
        elif self.popuptype == "snake" :
            self.popupsnake.place(x=300,y=300)
        elif self.popuptype == "ladder":
            self.popupladder.place(x=300,y=300)
        elif self.popuptype == 'gotquestion' :
            self.popuprandomhit.place(x=300,y=300)
        else:
            pass"""

        
        #Below Are positional placements
        self.canvas.place(x=340,y=100)
        self.labeltitle.place(x=350 , y=10)
        self.player1label.place(x=50,y=150)
        self.dice1.place(x=100,y=200)
        self.player2label.place(x=50,y=350)
        self.dice2.place(x=100, y=400)
        self.close_button.place(x=1000,y=600)
        self.player1point.place(x=1000,y=100)
        self.player2point.place(x=1000,y=300)
        self.player1counter.place(x=1000,y=150)
        self.player2counter.place(x=1000,y=350)
        self.rolldicebutton.place(x=100,y=600)
        roundstart.player1score


    def rollinganimation(self,playernumber):
        """self.variable  = random.randint(1,6)
        self.dice1 = Label(self.master , text= self.variable , background="#fee1c7" , font = ("Roboto" , 36 ),height=2 , width= 4 )
        self.dice1.place(x=100,y=200)"""
        time.sleep(0.5)
        outcomenumber = random.randint(1,6)
        #Reminder that true is player1, player2
        if playernumber == True:
            self.dice1 = Label(self.master , text= outcomenumber , background="#fee1c7" , font = ("Roboto" , 36 ),height=2 , width= 4 )
            self.dice1.place(x=100,y=200)
        elif playernumber == False:
            self.dice2 = Label(self.master , text= outcomenumber , background="#fee1c7",height=2 , width= 4 ,font = ("Roboto" , 36 ))
            self.dice2.place(x=100, y=400)
        self.changeframe(Answerframe(self.rootmaster))



#code below to be inserted at gui initialization
#pages = {1:Introframe(master) , 2:QuestionframeOPEN(master) , 3: QuestionframeMCQ(master) , 4:Answerframe(master) , 5: Endgameframe(master)}

roundstart = Round() #roundstart is the object for holding all information
rootmaster = Tk()
rootmaster.geometry("1280x720")
rootmaster.configure(background="#52d1dc")
#self.nextframe = Playingboard(self.rootmaster,10,1,'ladder',None,None)
#nextframe = Playingboard(rootmaster,roundstart)
#start  = Introframe(rootmaster,nextframe)
nextframe = Playingboard(rootmaster,roundstart)

print(roundstart.player1position)
b = True
count = 0
# while b:
#     nextframe = Playingboard(rootmaster,roundstart)
#     #roundstart = Round()
#     if count == 0:
#         #
#         count += 1
#     elif count == 1:
#         pass
#     elif count == 2:
#         count = 0
#         b = roundstart.endgameboolean
#print(roundstart.a)
rootmaster.mainloop()
