from tkinter import *
from tkinter import font
from tkinter.font import names
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
    def __init__(self, master):

        self.master = Frame(master)
        master.title("Snakes and Ladders Know it All")

        self.label = Label(master, text="Snakes and Ladders, KNOW IT ALL!!! " , font= ("Corbel" , 42) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.label.place(x=300 , y = 200)

        self.greet_button = Button(master, text="Let's Begin, Hajimasho!",font=("Roboto",24), padx=10 , pady=10 , command=self.proceed)
        self.greet_button.place(x=600, y=320)

        self.close_button = Button(master, text="Quit Game", command=master.quit , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.close_button.place(x=1000,y=600)

    def proceed(self,name):
        name.tkraise()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
class Endgameframe:
    def __init__(self, master):
        self.master = Frame(master)
        master.title("Thanks for playing!")

        self.label = Label(master, text="Rate us on Playstore 5/5, Hope you enjoyed the game​" , font= ("Corbel" , 36) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.label.place(x=250 , y = 200)

        self.greet_button = Button(master, text="Restart?", command=self.proceed , height= 4 , width= 40 , padx= 10 , pady = 10 , font=("roboto" , 24) , background="#f991cc" , foreground="#110b11")
        self.greet_button.place(x=400 , y=320)

        self.close_button = Button(master, text="Quit Game", command=master.quit , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.close_button.place(x=1000,y=700)

    def proceed(self):
        pass
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class QuestionframeMCQ :
    def __init__(self,master,mcq1 = "MCQ1 QUESTION ",mcq2="MCQ2 QUESTION ",mcq3="MCQ3 QUESTION ",mcq4="MCQ4 QUESTION ",questionlabel=" Insert something here") -> None:
        self.master = Frame(master)
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
        self.master = Frame(master)
        master.title("Question Time!")
        self.questionlabel= questionlabel

        #Declaration of all necessary labels
        self.qlabel = Label(master, text= self.questionlabel, font= ("Corbel" , 16) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.nextbutton = Button(master, text="Continue", command=self.nextpg() , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.answerbox = Entry(master,textvariable= " HELP " , foreground="#110b11" ,font= ("roboto" , 16) , width=100 ,   )
        #placements
        self.qlabel.place(x=200 , y=100)
        self.nextbutton.place(x=1000,y=650)
        self.answerbox.place(x=200,y=300)
    def nextpg(self):
        pass
class Answerframe :
    def __init__(self,master,answerstring =" You didn't specify a question",userboolean = None) -> None:
        self.master = Frame(master)
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
    def __init__(self,master) -> None:
        self.canvas = Canvas(master , width=600 , height= 600 , background="#53599a")
        self.labeltitle = Label(master , text= " THE SHOWDOWN BOARD " , font=("Corbel" , 36), foreground="#110b11" , padx = 10 ,pady = 10 )
        self.player1label = Label(master , text="Player 1 ",font=("Corbel" ,24),background="#52d1dc")
        self.player2label = Label(master , text= "Player 2",font=("Corbel" ,24),background="#52d1dc")
        self.dice1 = Label(master , text= "1" , background="#fee1c7" , font = ("Roboto" , 36 ),height=2 , width= 4 )
        self.dice2 = Label(master , text= "1" , background="#fee1c7",height=2 , width= 4 ,font = ("Roboto" , 36 ))
        self.player1point=Label(master, text="Player 1 Points" , font=("Corbel" ,24),background="#52d1dc")
        self.player2point=Label(master, text="Player 2 Points" , font=("Corbel" ,24),background="#52d1dc")
        self.player1counter = Label(master, text="0" , font=("Corbel" ,24),background="#52d1dc")
        self.player2counter = Label(master, text="0" , font=("Corbel" ,24),background="#52d1dc")
        self.close_button = Button(master, text="Quit Game", command=master.quit , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
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

#code below to be inserted at gui initialization


#pages = {1:Introframe(master) , 2:QuestionframeOPEN(master) , 3: QuestionframeMCQ(master) , 4:Answerframe(master) , 5: Endgameframe(master)}

master = Tk()
master.geometry("1280x720")
master.configure(background="#52d1dc")
start  = Playingboard(master)
master.mainloop()

