from tkinter import *
from tkinter import font
from tkinter import messagebox
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
class Questiondatabase:
    def __init__(self) -> None:
        self.data_set = {
        'E1' : [['What is the fastest animal in the world?'], ['Tiger', 'Cheetah', 'Puma', 'Peregrine Falcon'], ['Peregrine Falcon']],
        'E2' : [['What is the year the First World War ended?'], [], ['1918']],
        'E3' : [['What is the smallest planet in our solar system?'], ['Pluto', 'Jupiter', 'Mercury', 'Saturn'], ['Pluto']],
        'E4' : [['When did the SARS outbreak occur?'], [], ['2002']],
        'E5' : [['How many continents are there in the World?'], ['6', '7', '8', '9'], ['7']],
        'E6' : [['How many states are there in the United States?'], ['50', '', '', ''], ['']],
        'E7' : [['Where are the Himalayans located?'], ['India', 'Nepal', 'China', 'Russia'], ['India']],
        'E8' : [['How many playing cards are there in a regular deck?'], [], ['52']],
        'M1' : [['Which animal has no bones?'], ['Shark', 'Whale', 'Dolphin', 'Frog'], ['Shark']],
        'M2' : [['The name "Singapore" is derived from Sanskrit. What is the meaning?'], [], ['Lion City']],
        'M3' : [['Who has the strongest passport?'], ['Japan', 'Singapore', 'South Korea', 'Australia'], ['Japan']],
        'M4' : [['What is the name of Singapores International Airport?'], ['Changi Airport' , "Changi Village" , "Changi Corner" , "Changi Road"], ['Changi Airport']],
        'M5' : [['How many terminals does Singapores Airport have?'], ["4","3","5","6"], ['5']],
        'M6' : [['What is the fastest growing social media platform as of today?'], ['Instagram', 'Twitter', 'TikTok', 'Snapchat'], ['TikTok']],
        'M7' : [['What is the name of the area between your eyebrows?'], ['Glabella', 'Weenis', 'Poplitealm Fossa', 'Hallux'], ['Glabella']],
        'M8' : [['How many teeth does an adult human have?'], ["1","24","32","40"], ['32']],
        'M9' : [['What is the most spoken language in the world?'], ['Mandarin', 'Spanish', 'English', 'German'], ['Mandarin']],
        'M10' : [['In what stage of life, do humans have the most bones?'], ['Baby', 'Child', 'Adult', 'Elderly'], ['Baby']],
        'M11' : [['What is the end of your shoelace called?'], ['Phalanx', 'Tip', 'End', 'Aglet'], ['Aglet']],
        'M12' : [['Who bombed Pearl Harbour?'], ['The Japanese', 'The US', 'The Russians', 'The Germans'], ['The Japanese']],
        'M13' : [['What is the most practiced religion in the World?'], ['Islam', 'Judaism', 'Christianity', 'Buddhism'], ['Christianity']],
        'M14' : [['Which of the following is the largest and the deepest ocean of the world?'], ['Arctic', 'Atlantic', 'Pacific', 'Indian'], ['Pacific']],
        'M15' : [['Which country has a negative carbon index?'], ['Sweden', 'Bhutan', 'Rwanda', 'Singapore'], ['Bhutan']],
        'M16' : [['What is the main contributor to plastic waste?'], ['food wrappers', 'drink bottles', 'grocery bags', 'cigarette butts'], ['cigarette butts']],
        'M17' : [['What does QR stand for?'], ['Qualified Read', 'QR', 'Quick Response', 'Quality Reference'], ['Quick Response']],
        'M18' : [['What is the most abundant naturally occuring gas in the air?'], ['Carbon dioxide', 'Nitrogen', 'Oxygen', 'Argon'], ['Nitrogen']],
        'M19' : [['What country has less sheep than people?'], ['Australia', 'Nepal', 'New Zealand', 'Scotland'], ['Nepal']],
        'M20' : [['Which country has the highest happiness index? (as of 2020) '], ['Denmark', 'Greenland', 'Switzerland', 'Finland'], ['Finland']],
        'M21' : [['What does Wi-Fi stand for?'], ['Wireless Fidelity', 'Wireless Fi', 'Wi-Fi', 'Wireless Fix'], ['Wireless Fidelity']],
        'M22' : [['What is Singapore’s National Flower?'], ['Vanda Miss Joaquim', 'Orchid', 'Peony', 'Sunflower'], ['Vanda Miss Joaquim']],
        'M23' : [['What is Singapore’s Land Area?'], ['725', '800', '600', '500'], ['725']],
        'M24' : [['Which cannot be considered Singapore’s National Dish?'], ['Singapore Chilli Crab', 'Hainanese Chicken Rice', 'Singapore Laksa', 'Singapore Satay'], ['Hainanese Chicken Rice']],
        'M25' : [['Who are the Peranankans?'], ['Straits-Born Chinese', 'Malaysian', 'Indonesians', 'Singaporeans'], ['Straits-Born Chinese']],
        'M26' : [['How many islands in Singapore?'], ['60', '62', '64', '1'], ['64']],
        'M27' : [['Where is Changi Jewel?'], ['Changi Airport', 'Upper Changi', 'Changi Village', 'Changi Road'], ['Changi Airport']],
        'M28' : [['What is Singlish?'], ['Singlish are colloquial catchphrases', 'Singlish is just English', 'Singlish is Chinese', 'Singlish is a world language'], ['Singlish are colloquial catchphrases']],
        'M29' : [['Who pioneered the first F1 race?'], ['Singapore', 'Saudi Arabia', 'UAE', 'Qatar'], ['Singapore']],
        'M30' : [['Singapore’s city concept?'], ['City in a garden', 'Garden city', 'Asian city', 'Flower town'], ['City in a garden']],
        'M31' : [['Singapore Botanic Gardens is a:'], ['UNESCO World Heritage Site', 'UNCLOS AREA', 'FTZ', 'ASEAN'], ['UNESCO World Heritage Site']],
        'M32' : [['Are Durians allowed on trains?'], ['Yes', 'No', 'Maybe', 'What are Durians?'], ['']],
        'M33' : [['Singapore is part of :'], ['ASEAN', 'China', 'Malaysia', 'Malacca Straits'], ['ASEAN']],
        'M34' : [['What is not true about Pulau Tekong?'], ['You can have fun and leisure activities here.', 'Military training area', 'Recruits Live here', 'Its notorious'], ['You can have fun and leisure activities here.']],
        'M35' : [['Singapore Population Figure?'], ['5.6million', '4 million', '10 million', '6.7 million'], ['5.6million']],
        'M36' : [['What is a NSMAN?'], ['Someone who is old and retired', 'Someone who has to serve reservist', 'Someone who is in NS', 'I am not sure...'], ['Someone who has to serve reservist']],
        'M37' : [['What is a Hawker Centre?'], ['A place where Hawker sell food', 'A place to cook food for others', 'A Centre for hawkers to relax', 'An Office Name'], ['A place where Hawker sell food']],
        'M38' : [['Which is not a City State?'], ['Singapore', 'Monaco', 'Philippines', 'Vatican'], ['Philippines']],
        'M39' : [['Which of the following isn’t a form of legal punishment?'], ['Caning', 'Fines', 'Jail-Term', 'Public-Shaming'], ['Public-Shaming']],
        'M40' : [['What is NEWater?'], ['Highly treated reclaimed wastewater', 'Newly created water', 'Salt water', 'Weird water'], ['Highly treated reclaimed wastewater']],
        'M41' : [['Which Film did not feature Singapore?'], ['Hitman: Agent 47', 'Crazy Rich Asians', 'Ah Boys to Man', 'I Kinda Stupid'], ['I Kinda Stupid']],
        'M42' : [['What is the Singapore Sling?'], ['An alcoholic drink', 'A Sling Shot', 'A rifle sling', 'Singapore’s geographical location'], ['An alcoholic drink']],
        }
        self.randomkey = "M"+str(random.randint(1,40)) #this gives the random starting question
    def extractqn(self):
        self.qn = "{}".format(self.set[0][0])
    def returnkeyset(self):
        qns= self.data_set[self.key]
        return qns
    ### Extracting MCQ options
    def extractmcq(self):
        self.randomkey = "M"+str(random.randint(1,40))
        self.key = self.randomkey
        
        ## input data set input key
        self.qnlist = self.returnkeyset()
        self.qn = "{}".format(self.qnlist[0][0])
        op1 = "{}".format(self.qnlist[1][0])
        op2 = "{}".format(self.qnlist[1][1])
        op3 = "{}".format(self.qnlist[1][2])
        op4 = "{}".format(self.qnlist[1][3])
        ans = "{}".format(self.qnlist[2][0])
        return self.qn, op1, op2, op3, op4, ans
    
class Round:
    def __init__(self,rootmaster):
        self.rootmaster = rootmaster
        self.queryobject = Questiondatabase()
        self.userboolean = False # True is for Player 1, False is for Player 2
        self.player1index,self.player2index =1,1 #This indicates player position on the board and is passed into the playing board to display
        #positions
        self.player1score,self.player2score = 0,0 #This indicates overall questions answered correctly.
        self.endgameboolean = False #Will always be false until the end turn check returns true.
        #Upon being True, the game will show the endgame frame and the next move if any, is to reset the Round.
        self.questionstring,self.mcq1,self.mcq2,self.mcq3,self.mcq4,self.correctans=self.queryobject.extractmcq()#first question
        self.useranscorrect = False #This is for the display on the answer screen.
        #above are all the variables required to run questionframemcq and to serve to the answer screen
        self.excludedlistofqns = [] #All elements in this list can not be called again.
        self.nextframe = None
        self.count = 1 #count 1 for intro frame
        self.startframe  = Introframe(rootmaster,self)
        self.count += 1
        self.setnextframe(rootmaster)
        if self.endgameboolean == False:
            print(self.nextframe)
        rootmaster.mainloop()
    def setnextframe(self,rootmaster):
        if self.count == 2:
            self.nextframe = Explanationframe(rootmaster,self)
            self.count+=1
        elif self.count == 3 :
            self.nextframe= Playingboard(rootmaster,self)
            #roundstart = Round()
        elif self.count ==3.5:
            self.nextframe= Playingboard(rootmaster,self)
            self.count = 3
        elif self.count == 4: #at playing board
            self.nextframe = QuestionframeMCQ(rootmaster,self)
        elif self.count== 5: #at question screen
            self.nextframe = Answerframe(rootmaster,self)
        elif self.count == 6: #at answer screen
            self.nextframe=Playingboard(rootmaster,self)
            self.count= 4
        elif self.count == 7 :
            self.nameframe = Endgameframe(rootmaster,self)

    def reset(self):
        self.userboolean = False 
        self.player1index,self.player2index = 0,0 
        self.player1score,self.player2score = 0,0 
        self.endgameboolean = False 
        self.questionstring = ""
        self.mcq1,self.mcq2,self.mcq3,self.mcq4="","","",""
        self.correctans = ""
        self.useranscorrect = None 
        self.excludedlistofqns = [] 
        self.count = 0
    
    def checkendgame(self):
        if self.player1index>= 100 or self.player2index >= 100:
            self.endgameboolean = True
        else:
            return False 


class SNLFrame():
    def __init__(self, master,attributes):
        self.master = Frame(master, width=1280 , height=720,background="#52d1dc")
        self.attributes = attributes
    def changeframe(self):
        self.attributes.nextframe.master.grid(row=0,column=0)
        self.master.grid_forget()
        self.attributes.nextframe.master.tkraise()
        self.attributes.setnextframe(self.attributes.rootmaster)
        print(self.attributes.nextframe)


class Introframe(SNLFrame):
    def __init__(self, master,attributes):#this is to run the explanation frame solely)
        super().__init__(master,attributes)
        self.attributes = attributes
        master.title("Snakes and Ladders Know it All")

        self.label = Label(self.master, text="Snakes and Ladders, KNOW IT ALL!!! " , font= ("Corbel" , 42) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.label.place(x=300 , y = 200)

        self.greet_nextframe = attributes.nextframe
        self.greet_button = Button(self.master, text="Let's Begin, Hajimasho!",font=("Roboto",24), padx=10 , pady=10 , command=self.greet_button_pressed)
        self.greet_button.place(x=600, y=320)

        self.close_button = Button(self.master, text="Quit Game", command=master.quit , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.close_button.place(x=1000,y=600)
        self.master.grid(row=0,column=0)
    def greet_button_pressed(self):
        self.changeframe()


class Endgameframe(SNLFrame):
    def __init__(self, master ,attributes ): #resetframe to restart game
        super().__init__(master)
        self.resetframe = attributes.nextframe
        master.title("Thanks for playing!")

        self.label = Label(self.master, text="Rate us on Playstore 5/5, Hope you enjoyed the game​" , font= ("Corbel" , 36) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.label.place(x=250 , y = 200)

        self.restart_button = Button(self.master, text="Restart?", command=self.restartthegame , height= 4 , width= 40 , padx= 10 , pady = 10 , font=("roboto" , 24) , background="#f991cc" , foreground="#110b11")
        self.restart_button.place(x=400 , y=320)

        self.close_button = Button(master, text="Quit Game", command=master.quit , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.close_button.place(x=1000,y=700)
    def restartthegame(self): #problem with accessing the object 
        self.roundstart.reset()#clean all variables and attributes
        self.changeframe(self.resetframe)


    
class QuestionframeMCQ(SNLFrame) :
    def __init__(self,master,attributes) -> None:
        super().__init__(master,attributes)
        self.attributes = attributes
        self.attributes.questionstring,self.attributes.mcq1,self.attributes.mcq2,self.attributes.mcq3,self.attributes.mcq4,self.attributes.correctans=self.attributes.queryobject.extractmcq()
        self.attributes.useranscorrect = False#Reset correct or wrong each turn
        master.title("Question Time!")
        self.questionlabel,self.mcq1,self.mcq2,self.mcq3,self.mcq4 = self.attributes.questionstring,self.attributes.mcq1,self.attributes.mcq2,self.attributes.mcq3,self.attributes.mcq4

        #Declaration of all necessary labels
        self.qlabel = Label(self.master, text= self.questionlabel, font= ("Corbel" , 16) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20,wraplength=500)
        self.mcqbutton1 = Button(self.master, text=self.mcq1, command= lambda: self.setuserans(self.mcq1), height= 4 , width= 40 , padx= 10 , pady = 10 , font=("roboto" , 12) , background="#f991cc" , foreground="#110b11")
        self.mcqbutton2 = Button(self.master, text=self.mcq2, command= lambda: self.setuserans(self.mcq2), height= 4 , width= 40 , padx= 10 , pady = 10 , font=("roboto" , 12) , background="#f991cc" , foreground="#110b11")
        self.mcqbutton3 = Button(self.master, text=self.mcq3, command= lambda: self.setuserans(self.mcq3), height= 4 , width= 40, padx= 10 , pady = 10 , font=("roboto" , 12) , background="#f991cc" , foreground="#110b11")
        self.mcqbutton4 = Button(self.master, text=self.mcq4, command= lambda: self.setuserans(self.mcq4) , height= 4 , width= 40 , padx= 10 , pady = 10 , font=("roboto" , 12) , background="#f991cc" , foreground="#110b11")
        #self.nextbutton = Button(self.master, text="Continue", command=self.next_button , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        
        #placements
        self.qlabel.place(x=200 , y=100)
        self.mcqbutton1.place(x=300,y=300)
        self.mcqbutton2.place(x=800,y=300)
        self.mcqbutton3.place(x=300,y=500)
        self.mcqbutton4.place(x=800,y=500)
        #self.nextbutton.place(x=1000,y=650)
    def setuserans(self,buttonstring):
        self.userchoice = buttonstring
        self.check_answer()
        self.attributes.count += 1
        self.changeframe()
        print(self.attributes.useranscorrect)
    def next_button(self):
        self.changeframe(self.attributes.nextframe)
    def check_answer(self):
        if str(self.userchoice) == str(self.attributes.correctans) :
            self.attributes.useranscorrect = True
        else:
            self.attributes.useranscorrect = False
#Class below optional
"""class QuestionframeOPEN:
    def __init__(self,master,attributes) -> None:
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
        pass"""
class Answerframe(SNLFrame) :
    def __init__(self,master,attributes) -> None:
        super().__init__(master,attributes)
        self.attributes = attributes
        if self.attributes.useranscorrect == True:
            self.displaytext = "Omedetou Gozaimasu"
        elif self.attributes.useranscorrect == False:
            self.displaytext = "Awwwwwwww...."
        else:
            self.displaytext = "Amazing you managed to find a loophole."
        #declaration
        self.answerlabel = Label(self.master,text= self.attributes.correctans,font= ("Corbel" , 36) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        self.nextbutton = Button(self.master, text="Continue", command=self.next_button, font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.congratulations = Label(self.master,text= self.displaytext,font= ("Corbel" , 36) , foreground="#110b11", background="#fee1c7" ,padx=10,pady=20)
        #placements
        self.answerlabel.place(x=200,y=100)
        self.congratulations.place(x=200,y=300)
        self.nextbutton.place(x=1000,y=650)
    def next_button(self) :
        self.addpoints()
        self.attributes.count = 6
        self.changeframe()

    def addpoints(self):
        if self.attributes.userboolean == True and self.attributes.useranscorrect == True:
            self.attributes.player1points += 1
        elif self.attributes.userboolean == False and self.attributes.useranscorrect == True:
            self.attributes.player2points += 1
        self.attributes.useransrcorrect = False
        self.attributes.checkendgame()
        
    
class Explanationframe(SNLFrame) :
    def __init__(self,master,attributes) -> None:
        self.master = Frame(master, width=1280 , height=720,background="#52d1dc")
        super().__init__(master,attributes)
        self.attributes = attributes
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
        self.continuebutton = Button(self.master, text="Continue", command=lambda : self.changeframe(), font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.continuebutton.place(x=1000,y=650)
        self.explanationtext.place(x=100,y=200)
        self.explanationheader.place(x=100,y=50,anchor="w")
        

class Playingboard(SNLFrame) :
    def __init__(self,master,attributes) :
        super().__init__(master,attributes)
        self.attributes = attributes
        self.userboolean = self.attributes.userboolean#This is the player turn indicator
        self.player1position,self.player2position = self.attributes.player1index,self.attributes.player2index        

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
        self.player1initial =self.canvas.create_rectangle(self.indextoboardlocation(self.attributes.player1index),fill="red")
        self.x1,self.y1,self.x2,self.y2 =self.indextoboardlocation(self.attributes.player2index)
        self.player2initial=self.canvas.create_rectangle(self.x1+30,self.y1-30,self.x2+30,self.y2-30,fill="Blue")



        #label declarations
        self.labeltitle = Label(self.master , text= " THE SHOWDOWN BOARD " , font=("Corbel" , 36), foreground="#110b11" , padx = 10 ,pady = 10 )
        self.player1label = Label(self.master , text="Player 1 ",font=("Corbel" ,24),background="#52d1dc")
        self.player2label = Label(self.master , text= "Player 2",font=("Corbel" ,24),background="#52d1dc")
        self.dice1 = Label(self.master , text= 0 , background="#fee1c7" , font = ("Roboto" , 36 ),height=2 , width= 4 )
        self.dice2 = Label(self.master , text= 0 , background="#fee1c7",height=2 , width= 4 ,font = ("Roboto" , 36 ))
        self.player1point=Label(self.master, text="Player 1 Points" , font=("Corbel" ,24),background="#52d1dc")
        self.player2point=Label(self.master, text="Player 2 Points" , font=("Corbel" ,24),background="#52d1dc")
        self.player1counter = Label(self.master, text=self.attributes.player1score , font=("Corbel" ,24),background="#52d1dc")
        self.player2counter = Label(self.master, text=self.attributes.player2score , font=("Corbel" ,24),background="#52d1dc")
        self.close_button = Button(self.master, text="Quit Game", command=master.quit , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        self.rolldicebutton = Button(self.master, text="Roll Dice", command=lambda :self.rollinganimation() , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")
        #Popup system with waiting here
        self.popupsnake = Label(self.master)
        self.popupladder = Label(self.master)
        self.popupnextplayer = Label(self.master)
        self.popuprandomhit = Label(self.master)

        
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
        self.snake_ls = [
        (26,13),(41,22),(68,51),(78,15),(98,61)
        ]

        self.ladder_ls = [
        (2,24),(12,71),(32,46),(43,84),(66,88)
        ]
        self.surprise_ls = [
        (7, 6), (9, 8), (11, 10), (16, 15), (21, 20), (26, 25),
        (29, 28), (35, 34), (38, 37), (50, 49), (45, 44),
        (54, 53), (56, 55), (59, 58), (63, 62), (72, 71),
        (76, 75), (78, 77), (82, 81), (86, 85), (90, 89), (93, 92)
        ]

    def rollinganimation(self):
        """self.variable  = random.randint(1,6)
        self.dice1 = Label(self.master , text= self.variable , background="#fee1c7" , font = ("Roboto" , 36 ),height=2 , width= 4 )
        self.dice1.place(x=100,y=200)"""
        time.sleep(0.2)
        outcomenumber = random.randint(1,6)
        #Reminder that true is player1, player2 is false
        if self.attributes.userboolean == True:
            self.dice1 = Label(self.master , text= outcomenumber , background="#fee1c7" , font = ("Roboto" , 36 ),height=2 , width= 4 )
            self.dice1.place(x=100,y=200)
            self.attributes.player1index+=outcomenumber
            print(self.attributes.player1index)
        elif self.attributes.userboolean == False:
            self.dice2 = Label(self.master , text= outcomenumber , background="#fee1c7",height=2 , width= 4 ,font = ("Roboto" , 36 ))
            self.dice2.place(x=100, y=400)
            self.attributes.player2index+=outcomenumber
            print(self.attributes.player2index)
        self.attributes.checkendgame()#incase someone wins immediate
        if self.attributes.endgameboolean == True:
            print("Someonewon")
            self.changeframe(self.attributes.nextframe)
             #some code here to straightforward all the way to the endgamescreen
        else:
            pass
        #Now displace the movement. Player 1 is by default red, Player 2 is by default Blue
        if self.attributes.userboolean == True:
            x1,y1,x2,y2 = self.indextoboardlocation(self.attributes.player1index)
            self.canvas.create_rectangle(x1,y1,x2,y2,fill="red")
            self.gotquestion = self.check_prompt(self.attributes.player1index)
            self.canvas.delete(self.player1initial)
            self.attributes.count = 3.5
        elif self.attributes.userboolean == False:
            x1,y1,x2,y2 = self.indextoboardlocation(self.attributes.player2index)
            self.canvas.create_rectangle(x1+30,y1-30,x2+30,y2-30,fill="Blue")
            
            self.canvas.delete(self.player2initial)
            self.gotquestion= self.check_prompt(self.attributes.player2index)
            if self.gotquestion :
                self.attributes.count =4
            elif self.gotquestion== False:
                self.attributes.count= 3.5
        print(True)
        self.changeframe()
        #Below is to check if hit question, and if yes, what type of prompt to show
        #self.showprompt()


        
    def check_prompt(self,index):
        for i in range(len(self.snake_ls)):
            if index == self.snake_ls[i][0]:
                i1 = self.snake_ls[i][1]
                b = self.snake(i1)
                return True
            else:
                pass
        for i in range(len(self.ladder_ls)):
            if index == self.ladder_ls[i][0]:
                i1 = self.ladder_ls[i][1]
                b = self.ladder(i1)
                return True
            else:
                pass
        for i in range(len(self.surprise_ls)):
            if index == self.surprise_ls[i][0]:
                i1 = self.surprise_ls[i][1]
                b = self.surprise(i1)
                return True
            else:
                pass
        if self.attributes.userboolean == True:
            messagebox.showerror("Next Player" , "Player 2, Now it's your turn")
            self.attributes.userboolean = False
        else:
            messagebox.showerror("Next Player" , "Player 1, Now it's your turn")
            self.attributes.userboolean = True
        return False
    def snake(self,i1):
         messagebox.showerror("Snake","You stepped on snake! Answer this qn correctly or else you will have to fall back to tile {}".format(i1))

    def ladder(self,i1):
         messagebox.showerror("Ladder","You stepped on ladder! Answer this qn correctly to move to tile {}".format(i1))

    def surprise(self,i1):
         messagebox.showerror("Surprise","You stepped on surprise! Answer this qn correctly or else you will have to fall back to tile {}".format(i1))


        
    def indextoboardlocation(self,index):
        j = index% 20
        if j > 0 and j < 11:
            x = 60 * (j-1)
        elif j == 0:
            x = 0
        else:
            x = 540 - 60 * (j - 11)
        m = x + 30
        k = int((index-1)/ 10)
        y = 600 - 60 * k
        n = y - 30
        return x, y, m, n#x,y bottom coords, m,n topright coords



rootmaster = Tk()
rootmaster.geometry("1280x720")
rootmaster.configure(background="#52d1dc")
roundstart = Round(rootmaster) #roundstart is the object for holding all information
rootmaster.mainloop()
#Above all tkinter initiation








