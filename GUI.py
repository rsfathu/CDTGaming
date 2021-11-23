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

class Introframe:
    def __init__(self, master,nextframe):

        self.master = Frame(master, width=1280 , height=720,background="#52d1dc")
        
        master.title("Snakes and Ladders Know it All")

        self.label = Label(self.master, text="Snakes and Ladders, KNOW IT ALL!!! " , font= ("Corbel" , 42) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.label.place(x=300 , y = 200)

        self.greet_button = Button(self.master, text="Let's Begin, Hajimasho!",font=("Roboto",24), padx=10 , pady=10 , command=lambda : self.changeframe(nextframe))
        self.greet_button.place(x=600, y=320)

        self.close_button = Button(self.master, text="Quit Game", command=master.quit , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.close_button.place(x=1000,y=600)
        self.master.grid(row=0,column=0)
    def changeframe(self,future):
        future.master.grid(row=0,column=0)
        self.master.grid_forget()
        future.master.tkraise()
    def proceed(self):
        pass

class Endgameframe():
    def __init__(self, master):
        self.master = Frame(master, width=1280 , height=720,background="#52d1dc")
        master.title("Thanks for playing!")

        self.label = Label(master, text="Rate us on Playstore 5/5, Hope you enjoyed the game​" , font= ("Corbel" , 36) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.label.place(x=250 , y = 200)

        self.greet_button = Button(master, text="Restart?", command=None , height= 4 , width= 40 , padx= 10 , pady = 10 , font=("roboto" , 24) , background="#f991cc" , foreground="#110b11")
        self.greet_button.place(x=400 , y=320)

        self.close_button = Button(master, text="Quit Game", command=master.quit , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.close_button.place(x=1000,y=700)

    def changeframe(self,future):
        future.master.grid(row=0,column=0)
        self.master.grid_forget()
        future.master.tkraise()

class QuestionframeMCQ :
    def __init__(self,master,mcq1 = "MCQ1 QUESTION ",mcq2="MCQ2 QUESTION ",mcq3="MCQ3 QUESTION ",mcq4="MCQ4 QUESTION ",questionlabel=" Insert something here") -> None:
        self.master = Frame(master, width=1280 , height=720,background="#52d1dc")
        master.title("Question Time!")
        self.questionlabel,self.mcq1,self.mcq2,self.mcq3,self.mcq4 = questionlabel,mcq1,mcq2,mcq3,mcq4

        #Declaration of all necessary labels
        self.qlabel = Label(master, text= self.questionlabel, font= ("Corbel" , 16) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.mcqbutton1 = Button(master, text=self.mcq1, command= None, height= 2 , width= 10 , padx= 2 , pady = 2 , font=("roboto" , 12) , background="#f991cc" , foreground="#110b11")
        self.mcqbutton2 = Button(master, text=self.mcq2, command= None, height= 2 , width= 10 , padx= 2 , pady = 2 , font=("roboto" , 12) , background="#f991cc" , foreground="#110b11")
        self.mcqbutton3 = Button(master, text=self.mcq3, command= None, height= 2 , width= 10 , padx= 2 , pady = 2 , font=("roboto" , 12) , background="#f991cc" , foreground="#110b11")
        self.mcqbutton4 = Button(master, text=self.mcq4, command= None , height= 2 , width= 10 , padx= 2 , pady = 2 , font=("roboto" , 12) , background="#f991cc" , foreground="#110b11")
        self.nextbutton = Button(master, text="Continue", command=self.nextpg("test") , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")

        #placements
        self.qlabel.place(x=200 , y=100)
        self.mcqbutton1.place(x=300,y=300)
        self.mcqbutton2.place(x=800,y=300)
        self.mcqbutton3.place(x=300,y=500)
        self.mcqbutton4.place(x=800,y=500)
        self.nextbutton.place(x=1000,y=650)

    def nextpg(self, pagename):
        pass

class QuestionframeOPEN:
    def __init__(self,master,questionlabel = "Question to be inserted") -> None:
        self.master = Frame(master, width=1280 , height=720,background="#52d1dc")
        master.title("Question Time!")
        self.questionlabel= questionlabel

        #Declaration of all necessary labels
        self.qlabel = Label(master, text= self.questionlabel, font= ("Corbel" , 16) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.nextbutton = Button(master, text="Continue", command=self.nextpg() , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.answerbox = Entry(master,textvariable= " HELP " , foreground="#110b11" ,font= ("roboto" , 16) , width=100 ,   )
        #placements
        self.qlabel.place(x=200 , y=100)
        self.nextbutton.place(x=1000,y=650)
        self.answerbox.place(x=100,y=300)
    def nextpg(self):
        pass
class Answerframe :
    def __init__(self,master,answerstring =" You didn't specify a question",userboolean = None) -> None:
        self.master = Frame(master, width=1280 , height=720,background="#52d1dc")
        self.answer = answerstring
        self.boolean = userboolean #this thing is a boolean that will display different messages for correct or wrong messages.
        if self.boolean == True:
            self.displaytext = "Omedetou Gozaimasu"
        elif self.boolean == False:
            self.displaytext = "Awwwwwwww...."
        else:
            self.displaytext = "Amazing you managed to find a loophole."
        #declaration
        self.answerlabel = Label(master,text= "ANSWER HERE",font= ("Corbel" , 36) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.nextbutton = Button(master, text="Continue", command=self.nextpg() , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.congratulations = Label(master,text= self.displaytext,font= ("Corbel" , 36) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)


        #placements
        self.answerlabel.place(x=200,y=100)
        self.congratulations.place(x=200,y=300)
        self.nextbutton.place(x=1000,y=650)

    def nextpg(self):
        pass

class Playingboard :
    def __init__(self,master,player1position,player2position,popuptype,playernumber) :
        self.master = Frame(master, width=1280 , height=720,background="#52d1dc")
        self.playernumber = playernumber#This is the player turn indicator
        self.player1position,self.player2position = player1position,player2position
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
        self.rolldicebutton = Button(self.master, text="Roll DIce", command=lambda :self.rollinganimation(2) , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        #Popup system with waiting here
        self.popupsnake = Label(self.master)
        self.popupladder = Label(self.master)
        self.popupnextplayer = Label(self.master)
        self.popuprandomhit = Label(self.master)
        self.popuptype = popuptype
        if self.popuptype == 'nextplayer':
            self.popupnextplayer.place(x=300,y=300)
        elif self.popuptype == "snake" :
            self.popupsnake.place(x=300,y=300)
        elif self.popuptype == "ladder":
            self.popupladder.place(x=300,y=300)
        elif self.popuptype == 'gotquestion' :
            self.popuprandomhit.place(x=300,y=300)
        else:
            pass

        
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

    def rollinganimation(self,outcomenumber,playernumber):
        
        """self.variable  = random.randint(1,6)
        self.dice1 = Label(self.master , text= self.variable , background="#fee1c7" , font = ("Roboto" , 36 ),height=2 , width= 4 )
        self.dice1.place(x=100,y=200)"""
        time.sleep(0.5)
        if playernumber == 1:
            self.dice1 = Label(self.master , text= outcomenumber , background="#fee1c7" , font = ("Roboto" , 36 ),height=2 , width= 4 )
            self.dice1.place(x=100,y=200)
        elif playernumber == 2:
            self.dice2 = Label(self.master , text= outcomenumber , background="#fee1c7",height=2 , width= 4 ,font = ("Roboto" , 36 ))
            self.dice2.place(x=100, y=400)



#code below to be inserted at gui initialization
#pages = {1:Introframe(master) , 2:QuestionframeOPEN(master) , 3: QuestionframeMCQ(master) , 4:Answerframe(master) , 5: Endgameframe(master)}



class GUILOOP() :
    def __init__(self) :
        self.master = Tk()
        self.master.geometry("1280x720")
        self.master.configure(background="#52d1dc")
        self.nextframe = Playingboard(self.master,10,1,'ladder',1)
        self.start  = Introframe(self.master,self.nextframe)
        self.master.mainloop()
a = GUILOOP()


