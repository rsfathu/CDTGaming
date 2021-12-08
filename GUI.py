from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.font import names
from copy import deepcopy
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
698B22 - olivedrab4
8B5A00 - orange4
 """


## data attributes as an object
## dictionary is structured list - in dict, can define key (M__)
## everything is class - store attributes and methods
## using classes inside inside methods
## sub class is most specific -
## object is specific
## functions under the class are like lessons under the class
## self is so that i dont need to pass everything individually
## reference attributes to / of myself
## class > functions = attributes (placeholder)
## example of a room(class) - functions(aircon, light) - objects
## call super-class first
## how to do turn based: When Player 1, True. After you roll the dice, return to False. So its player 2's turn.
## How to make it go in a swirly swirly, odd/even (last function in the code (math))
## for i in range(100), self.player(index)
## classes- question, display board ( 7 diff classes ): its now moving the canvas instead of erasing the class
## i dont want memory location to be the same
## deepcopy stores everything differently
## bulk of code, is mainly questions and widget placement
## ):


## key for dictionary is self defined
## key for list is 0, 1, 2, 3, ...
## more information in dictionary
## so for this code, i use M1, M2, so i know where is the medium question 1, medium question 2
# which is better than having to get a key from a list where it is not as defined
# fundamentally, i want to define the question types


class Questiondatabase:
    def __init__(self) -> None:
        self.data_set = {
            'M1' : [['Name the city that is located in two countries.'], ['Istanbul', 'Dubai', 'Paris', 'Singapore'], ['Istanbul']],
            'M2': [['The name "Singapore" is derived from Sanskrit. What is the meaning?'],
                   ['Garden City', 'Lion City', 'City surrounded by Seas', 'Red Dot'], ['Lion City']],
            'M3': [['Who has the strongest passport?'], ['Japan', 'Singapore', 'South Korea', 'Australia'], ['Japan']],
            'M4': [['What is the name of Singapores International Airport?'],
                   ['Changi Airport', "Changi Village", "Changi Corner", "Changi Road"], ['Changi Airport']],
            'M5': [['How many terminals does Singapores Airport have?'], ["4", "3", "5", "6"], ['5']],
            'M6' : [['Which is the tallest mountain in the world?'], ['Mount Faber', 'Mount Everest', 'Mount Kilimanjaro', 'Swiss Alps'], ['Mount Everest']],
            'M7' : [['What is the name of the longest river in Africa'], ['Yellow River', 'Amazon River', 'Mississippi River', 'The Nile River'], ['The Nile River']],
            'M8' : [['What country are the Great Pyramids of Giza located in?'], ['Sudan', 'Mexico', 'Egypt', 'Iraq'], ['Egypt']],
            'M9': [['What is the most spoken language in the world?'], ['Mandarin', 'Spanish', 'English', 'German'],
                   ['Mandarin']],
            'M10' : [['What is the coldest place on Earth? '], ['Antarctica ', 'South pole', 'North Pole', 'Switzerland'], ['Antarctica ']],
            'M11' : [['How many time zones does Russia have? '], ['9', '11', '15', '10'], ['11']],
            'M12': [['Who bombed Pearl Harbour?'], ['The Japanese', 'The US', 'The Russians', 'The Germans'],
                    ['The Japanese']],
            'M13': [['What is the most practiced religion in the World?'],
                    ['Islam', 'Judaism', 'Christianity', 'Buddhism'], ['Christianity']],
            'M14': [['Which of the following is the largest and the deepest ocean of the world?'],
                    ['Arctic', 'Atlantic', 'Pacific', 'Indian'], ['Pacific']],
            'M15': [['Which country has a negative carbon index?'], ['Sweden', 'Bhutan', 'Rwanda', 'Singapore'],
                    ['Bhutan']],
            'M16': [['What is the main contributor to plastic waste?'],
                    ['food wrappers', 'drink bottles', 'grocery bags', 'cigarette butts'], ['cigarette butts']],
            'M17' : [['What is the name of the longest river in the US? '], ['Columbia River', 'Hudson River', 'Tennessee River', 'Missouri River'], ['Missouri River']],
            'M18': [['What is the most abundant naturally occuring gas in the air?'],
                    ['Carbon dioxide', 'Nitrogen', 'Oxygen', 'Argon'], ['Nitrogen']],
            'M19': [['What country has less sheep than people?'], ['Australia', 'Nepal', 'New Zealand', 'Scotland'],
                    ['Nepal']],
            'M20': [['Which country has the highest happiness index? (as of 2020) '],
                    ['Denmark', 'Greenland', 'Switzerland', 'Finland'], ['Finland']],
            'M21' : [['Mt. Fuji is the highest point located in which Asian country? '], ['Korea', 'Japan ', 'Taiwan', 'Hong Kong'], ['Japan ']],
            'M22': [['What is Singapore’s National Flower?'], ['Vanda Miss Joaquim', 'Orchid', 'Peony', 'Sunflower'],
                    ['Vanda Miss Joaquim']],
            'M23': [['What is Singapore’s Land Area?'], ['725', '800', '600', '500'], ['725']],
            'M24': [['Which cannot be considered Singapore’s National Dish?'],
                    ['Singapore Chilli Crab', 'Hainanese Chicken Rice', 'Singapore Laksa', 'Singapore Satay'],
                    ['Hainanese Chicken Rice']],
            'M25': [['Who are the Peranankans?'], ['Straits-Born Chinese', 'Malaysian', 'Indonesians', 'Singaporeans'],
                    ['Straits-Born Chinese']],
            'M26': [['How many islands in Singapore?'], ['60', '62', '64', '1'], ['64']],
            'M27': [['Where is Changi Jewel?'], ['Changi Airport', 'Upper Changi', 'Changi Village', 'Changi Road'],
                    ['Changi Airport']],
            'M28': [['What is Singlish?'],
                    ['Singlish are colloquial catchphrases', 'Singlish is just English', 'Singlish is Chinese',
                     'Singlish is a world language'], ['Singlish are colloquial catchphrases']],
            'M29' : [['How many countries are there in Africa? '], ['53', '54', '45', '43'], ['54']],
            'M30': [['Singapore’s city concept?'], ['City in a garden', 'Garden city', 'Asian city', 'Flower town'],
                    ['City in a garden']],
            'M31': [['Singapore Botanic Gardens is a:'], ['UNESCO World Heritage Site', 'UNCLOS AREA', 'FTZ', 'ASEAN'],
                    ['UNESCO World Heritage Site']],
            'M32' : [['Which country is home to the most volcanos? '], ['Vietnam', 'Indonesia', 'Philipines', 'Italy'], ['Indonesia']],
            'M33': [['Singapore is part of :'], ['ASEAN', 'China', 'Malaysia', 'Malacca Straits'], ['ASEAN']],
            'M34': [['What is not true about Pulau Tekong?'],
                    ['You can have fun and leisure activities here.', 'Military training area', 'Recruits Live here',
                     'Its notorious'], ['You can have fun and leisure activities here.']],
            'M35': [['Singapore Population Figure?'], ['5.6million', '4 million', '10 million', '6.7 million'],
                    ['5.6million']],
            'M36' : [['In which year was John F. Kennedy assassinated?'], ['1961', '1965', '1963', '1964'], ['1963']],
            'M37': [['What is a Hawker Centre?'], ['A place where Hawker sell food', 'A place to cook food for others',
                                                   'A Centre for hawkers to relax', 'An Office Name'],
                    ['A place where Hawker sell food']],
            'M38': [['Which is not a City State?'], ['Singapore', 'Monaco', 'Philippines', 'Vatican'], ['Philippines']],
            'M39' : [['When did Mao Zedong come to power?'], ['1947', '1950', '1949', '1960'], ['1949']],
            'M40': [['What is NEWater?'],
                    ['Highly treated reclaimed wastewater', 'Newly created water', 'Salt water', 'Weird water'],
                    ['Highly treated reclaimed wastewater']],
            'M41' : [['Which war took place between 1950 and 1953?'], ['The Korean War', 'The Vietnam War', 'Cuban Missile Crisis', 'Second World War'], ['The Korean War']],
            'M42' : [['In which year was the Berlin Wall torn down?'], ['1990', '1989', '1986', '1985'], ['1989']],
            'M43': [['Which is the happiest country in South East Asia?'],
                    ['Thailand', 'Singapore', 'Malaysia', 'Brunei'], ['Singapore']],
            'M44': [['How many countries are there in South East Asia?'], ['11', '10', '9', '8'], ['11']],
            'M45' : [['Who led the USSR from 1917-1922?'], ['Vladimir Lenin', 'Joseph Stalin', 'Georgy Malenkov', 'Leonid Brezhnev'], ['Vladimir Lenin']],
            'M46': [['How long does plastic take to decompose?'],
                    ['120 years', '450 years', '1300 years', 'Never decompose'], ['450 years']],
            'M47' : [['In which year did WWI begin?'], ['1945', '1915', '1914', '1943'], ['1914']],
            'M48' : [['Where was Adolf Hitler born?'], ['Zurich', 'Weimar', 'Poland', 'Austria'], ['Austria']],
            'M49': [['How many animals are at risk of becoming extinct because of plastic?'],
                    ['700', '267', '400', '102'], ['700']],
            'M50': [['What is the largest country in the world?'], ['China', 'USA', 'Russia', 'Australia'], ['Russia']],
            'M51' : [['What is the longest war in U.S. history?'], ['Afghan War', 'Civil War', 'Spanish-American War', 'Mexican War'], ['Afghan War']],
            'M52' : [['Which treaty formally established the status of Singapore as a British colony?'], [' Treaty of Singapore ', ' Treaty of Temasek ', 'Anglo-Dutch Treaty', 'Straits Settlements Treaty'], ['Anglo-Dutch Treaty']],
            'M53' : [['In which year did Singapore fall to the Japanese in World War Two?'], ['1945', '1943', '1942', '1944'], ['1942']],
            'M54': [['What is greenwashing?'],
                    ['a marketing scheme where the product advertised is not actually ''green''',
                     'companies changing their products to be more ''green', 'Painting things green', ''],
                    ['a marketing scheme where the product advertised is not actually ''green''']],
            'M55' : [['In which year did the Japanese Occupation of Singapore end?'], ['1947', '1944', '1945', '1946'], ['1945']],
            'M56' : [['Who was the first Chief Minister of Singapore?'], ['David Marshall', 'Lee Kuan Yew', 'Goh Chok Tong', 'Yusof Ishak'], ['David Marshall']],
            'M57': [['What is the smallest country in the world?'],
                    ['Luxemborg', 'Vatican City', 'Singapore', 'Monaco'], ['Vatican City']],
            'M58' : [['Along with Hiroshima, Japan, which Japanese city was hit by an atomic bomb in 1945?'], ['Roppongi', 'Nagano', 'Nagasaki', 'Fukushima'], ['Nagasaki']],
            'M59' : [['Which geographical instrument measures air pressure?'], ['Psychrometer', 'Barometer', 'Hygrometer', 'Wind vane'], ['Barometer']],
            'M60' : [['Which of the following are not carbon sinks?'], ['Ocean', 'Forest', 'Soil', 'Us, humans'], ['Us, humans']],
            'M61' : [['In which European City would you find the Orly Aiport?'], ['Paris', 'London', 'Lisbon', 'Brussels'], ['Paris']],
            'M62' : [['What is the main reason for sea/land breeze?'], ['Change in seasons', 'difference in temperature of the land and sea', 'difference in air pressure', 'Change in light'], ['difference in temperature of the land and sea']],
            'M63' : [['How to measure compass bearings?'], ['From North, following the clockwise direction', 'From South, following the clockwise direction', 'From East, following the clockwise direction', 'From West, following the clockwise direction'], ['From North, following the clockwise direction']],
            'M64' : [['What does a wind vane do?'], ['Wind pressure', 'Amount of wind', 'Wind direction', 'Wind speed'], ['Wind direction']],
            'M65' : [['How many layers does the Earth have?'], ['5', '4', '3', '2'], ['3']],
            'M66': [['Who was the first woman to win a Nobel Prize (1903)?'],
                    ['Marie Curie', 'Bertha Von Suttner', 'Grazia Deledda', 'Jane Addams'], ['Marie Curie']],
            'M67' : [['Where is the deepest part of the ocean?'], ['Java Trench', 'Mariana Trench', 'South Sandwich Trench', 'Molloy Deep'], ['Mariana Trench']],
            'M68' : [['What is NOT a characteristic of a shield volcano?'], ['Basaltic magma', 'low on silica', 'low gas content', 'Steep sides'], ['Steep sides']],
            'M69' : [['What is dew point?'], ['The temperature at which dew begins to evaporate', 'The temperature at which dew forms', 'The point when dew is visible to the eye', 'A dew pointing'], ['The temperature at which dew begins to evaporate']],
            'M70' : [['How are composite volcanoes formed?'], ['Produced at divergent plate boundaries', 'Produced at convergent plate boundaries', 'Produced by the core being too hot', 'Explosive content in the Earth needed a way to escape'], ['Produced at convergent plate boundaries']],
            'M71' : [['How many types of volcanoes are there?'], ['1', '2', '3', '4'], ['4']],
            'M72' : [['Which book was written by Hitler while in prison in the 1920s?'], ['Mein Kampf', 'Therigatha', 'Persepolis', 'Sualat Al-Salatin'], ['Mein Kampf']],
            'M73' : [['What does POW stands for?'], ['People of the West', 'Prisoners of War', 'People of Workers Party', 'Prisoners of Western World'], ['Prisoners of War']],
            'M74' : [['In which year did the Emancipation Proclamation become law?'], ['1863', '1975', '1865', '1971'], ['1863']],
            'M75' : [['How is an oceanic trench formed?'], ['Continental-continental Converge', 'Continental-Oceanic Converge', 'Continental-Oceanic Diverge', 'Oceanic-oceanic diverge'], ['Continental-Oceanic Converge']],
            'M76' : [['Which Treaty forced Britain to recognize The United States as an independent nation?'], ['Treaty of versailles', 'Treaty of westphalia', 'Treaty of Brest-Litovsk', 'The Treaty of Paris '], ['The Treaty of Paris of 1783']],
            'M77' : [['what happens when continental plates split apart?'], ['An oceanice ridge is formed', 'A Valley-like rift is formed', 'An underwater volcano is formed', 'A mountain is formed'], ['A Valley-like rift is formed']],
            'M78' : [['How are clouds formed?'], ['Water Vapour rises from the ground and condenses into visible water droplets', 'Water Vapour rises and join together to form a cloud', 'Water vapour from the atmosphere condense to form a cloud', 'Cloud Factory'], ['Water Vapour rises and condenses into visible water droplets']],
            'M79' : [['How many tectonic plates are there in the lithosphere now?'], ['10~15', '15~20', '20~25', '25~30'], ['15~20']],
            'M80' : [['When was the Declaration of Independence signed?'], ['August 14, 1871', 'August 2, 1776', 'October 24, 1775', 'July 4, 1876'], ['August 2, 1776']],
            'M81' : [['What is population density?'], ['number of individuals living in a specific location', 'number of individuals in a specific country', 'weight of everyone divided by area of floor', 'total number of people in a specific city'], ['number of individuals living in a specific location']],
            'M82' : [['What year were American women granted the right to vote? '], ['1920', '1921', '1889', '1934'], ['1920']],
            'M83' : [['When did the Japanese attack Pearl Harbor?'], ['1946', '1945', '1941', '1943'], ['1941']],
            'M84' : [['What affects the impact of a natural disaster the most?'], ['Reactivity of people', 'Time for reaction', 'Population', 'Location'], ['Population']],
            'M85' : [['Who was the first woman to hold federal executive office in the United States?'], ['Kamala Harris', 'Queen Elizabeth', 'Mother Theresa', 'Hilary Clinton'], ['Kamala Harris']],
            'M86' : [['Who was the first president of the United States to live in the White House?'], ['President Barack Obama', 'President Franklin D. Roosevelt', 'President John Adams', 'President John F. Kennedy'], ['President John Adams']],
            'M87' : [['What is singapore response to climate change?'], ['reducing its greenhouse gas emissions intensity by 36% compared to 2005 levels by 2030', 'reducing its greenhouse gas emissions intensity by 25% compared to 2005 levels by 2025', 'reducing its greenhouse gas emissions intensity by 30% compared to 2005 levels by 2030', 'reducing its greenhouse gas emissions intensity by 20% compared to 2005 levels by 2025'], ['reducing its greenhouse gas emissions intensity by 36% compared to 2005 levels by 2030']],
            'M88' : [['Which is not one of the pressures that threaten the coral reef ecosystem?'], ['Over-collection of corals', 'Fishing methods', 'Recreational use of the coast', 'Level of salinity and oxygen content'], ['Level of salinity and oxygen content']],
            'M89' : [['When did the Cold War officially end?'], ['1920', '1989', '1943', '1975'], ['1989']],
            'M90' : [['What is NOT part of the structure of the Volcano?'], ['Caldera', 'Vent', 'Crate', 'Slope'], ['Slope']],
            'M91' : [['Which is not a form of tourism?'], ['Honeypot tourism', 'Dark tourism', 'Family tourism', 'Pilgrimage tourism'], ['Family tourism']],
            'M92' : [['Which is a destination factor of global tourism?'], ['Investment in infrastructure and services ', 'Disposable income ', 'Leisure time', 'Changing lifestyle'], ['Family tourism']],
            'M93' : [['What is a wind rose?'], ['rose that is pollinated through the wind', 'measures wind speed and direction are typically distributed', 'measures wind speed', 'measures wind direction'], ['measures wind speed and direction are typically distributed']],
            'M94' : [['1959 was significant in Singapores political history because Singapore ...'], ['became part of Malaysia', 'gained independence', 'was given limited self-independence', 'achieved full government'], ['achieved full government']],
            'M95' : [['What is the dry side of a mountain called?'], ['Dry side', 'Leeward side', 'Back side', 'Windward side'], ['Leeward side']],
            'M96' : [["1959 was significant in Singapore's political history because Singapore ..."], ['became part of Malaysia', 'gained independence', 'was given limited self-independence', 'achieved full government'], ['achieved full government']],
            'M97' : [['What is altitude?'], ['distance from the equator', 'distance from the ground', 'distance above sea level', 'distance from origin'], ['distance above sea level']],
            'M98' : [['When was the Wall Street crash happened?'], ['1929', '1991', '1920', '1957'], ['1929']],
            'M99' : [['Name the pandemic which almost killed 1 percent of world population in 1918?'], ['Spanish Flu.', 'The Black Plague.', 'Small Pox.', 'The Russian Plague.'], ['Spanish Flu.']],
            'M100' : [['In which century the Black Death was held?'], ['15th century.', '14th century.', '18th century.', '19th century.'], ['14th century.']],
        }


        self.randomkey = "M" + str(random.randint(1, 100))  # this gives the random starting question

    def returnkeyset(self):
        qns = self.data_set[self.key]
        return qns

    ### Extracting MCQ options
    def extractmcq(self):
        self.randomkey = "M" + str(random.randint(1, 100))  # this randomly selects the next question
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
    def __init__(self, rootmaster):
        self.rootmaster = rootmaster
        self.queryobject = Questiondatabase()  ##calling a class from another class (1st class)
        self.userboolean = False  # True is for Player 1, False is for Player 2
        self.player1index, self.player2index = 1, 1  # This indicates player position on the board and is passed into the playing board to display
        # positions
        self.player1score, self.player2score = 0, 0  # This indicates overall questions answered correctly.
        self.endgameboolean = False  # Will always be false until the end turn check returns true.
        # Upon being True, the game will show the endgame frame and the next move if any, is to reset the Round.
        self.questionstring, self.mcq1, self.mcq2, self.mcq3, self.mcq4, self.correctans = self.queryobject.extractmcq()  # first question
        self.useranscorrect = False  # This is for the display on the answer screen.
        # above are all the variables required to run questionframemcq and to serve to the answer screen
        self.excludedlistofqns = []  # All elements in this list can not be called again.
        self.potentialindex = 0  # potential step if answer correct or wrong
        self.questiontype = None
        self.nextframe = None
        self.count = 1  # count 1 for intro frame
        self.startframe = Introframe(rootmaster, self)
        self.setnextframe(rootmaster)
        rootmaster.mainloop()

    def setnextframe(self, rootmaster):
        print("count is at : ", self.count)
        if self.count == 1:
            self.startframe = Introframe(rootmaster, self)
        if self.count == 2:
            self.nextframe = Explanationframe(rootmaster, self)
        elif self.count == 3:
            self.nextframe = Playingboard(rootmaster, self)
            # roundstart = Round()
        elif self.count == 3.5:
            self.nextframe = Playingboard(rootmaster, self)
            self.count = 3
        elif self.count == 4:  # at playing board
            self.nextframe = QuestionframeMCQ(rootmaster, self)
        elif self.count == 5:  # at question screen
            self.nextframe = Answerframe(rootmaster, self)
        elif self.count == 7:
            self.nextframe = Endgameframe(rootmaster, self)

    def reset(self):
        self.userboolean = False
        self.player1index, self.player2index = 1, 1
        self.player1score, self.player2score = 0, 0
        self.endgameboolean = False
        self.questionstring = ""
        self.mcq1, self.mcq2, self.mcq3, self.mcq4 = "", "", "", ""
        self.correctans = ""
        self.useranscorrect = None
        self.excludedlistofqns = []
        self.count = 1

    def checkendgame(self):
        if self.player1index >= 100 or self.player2index >= 100:
            self.endgameboolean = True
        else:
            return False


class SNLFrame():
    def __init__(self, master, attributes):
        self.master = Frame(master, width=1280, height=720, background="#8B5A00")
        self.attributes = attributes

    def changeframe(self):
        self.attributes.setnextframe(self.attributes.rootmaster)
        self.attributes.nextframe.master.grid(row=0, column=0)
        self.master.grid_forget()
        self.attributes.nextframe.master.tkraise()


class Introframe(SNLFrame):
    def __init__(self, master, attributes):  # this is to run the explanation frame solely)
        super().__init__(master, attributes)
        self.attributes = attributes
        master.title("Snakes and Ladders Know it All")

        self.label = Label(self.master, text="Snakes and Ladders, KNOW IT ALL!!! ", font=("Corbel", 42),
                           foreground="#110b11", background="#fee1c7", padx=10, pady=20)
        self.label.place(x=200, y=200)

        self.greet_nextframe = attributes.nextframe
        self.greet_button = Button(self.master, text="Let's Begin!", font=("Roboto", 24), padx=10, pady=10,
                                   command=self.greet_button_pressed)
        self.greet_button.place(x=500, y=320)

        self.close_button = Button(self.master, text="Quit Game", command=master.quit, font=("Roboto", 24),
                                   background="#fee1c7", foreground="#110b11")
        self.close_button.place(x=1000, y=600)
        self.master.grid(row=0, column=0)

    def greet_button_pressed(self):
        self.attributes.count = 2
        self.changeframe()


class Endgameframe(SNLFrame):
    def __init__(self, master, attributes):  # resetframe to restart game
        super().__init__(master, attributes)
        self.resetframe = attributes.nextframe
        master.title("Thanks for playing!")

        self.label = Label(self.master, text="Rate us on Playstore 5/5, Hope you enjoyed the game!​",
                           font=("Corbel", 24), foreground="#110b11", background="#fee1c7", padx=10, pady=20)
        self.label.place(x=250, y=200)

        self.restart_button = Button(self.master, text="Restart?", command=self.restartthegame, height=4, width=20,
                                     padx=10, pady=10, font=("roboto", 24), background="#f991cc", foreground="#110b11")
        self.restart_button.place(x=400, y=320)

        self.close_button = Button(master, text="Quit Game", command=master.quit, font=("Roboto", 24),
                                   background="#fee1c7", foreground="#110b11")
        self.close_button.place(x=1000, y=700)

    def restartthegame(self):  # problem with accessing the object
        self.attributes.reset()  # clean all variables and attributes
        self.attributes.count = 1
        self.changeframe()


class QuestionframeMCQ(SNLFrame):
    def __init__(self, master, attributes) -> None:
        super().__init__(master, attributes)
        self.attributes = attributes
        self.attributes.questionstring, self.attributes.mcq1, self.attributes.mcq2, self.attributes.mcq3, self.attributes.mcq4, self.attributes.correctans = self.attributes.queryobject.extractmcq()
        self.attributes.useranscorrect = False  # Reset correct or wrong each turn
        master.title("Question Time!")
        self.questionlabel, self.mcq1, self.mcq2, self.mcq3, self.mcq4 = self.attributes.questionstring, self.attributes.mcq1, self.attributes.mcq2, self.attributes.mcq3, self.attributes.mcq4

        # Declaration of all necessary labels
        self.qlabel = Label(self.master, text=self.questionlabel, font=("Corbel", 16), foreground="#110b11",
                            background="#fee1c7", padx=10, pady=20, wraplength=500)
        self.mcqbutton1 = Button(self.master, text=self.mcq1, command=lambda: self.setuserans(self.mcq1), height=4,
                                 width=40, padx=10, pady=10, font=("roboto", 12), background="#f991cc",
                                 foreground="#110b11")
        self.mcqbutton2 = Button(self.master, text=self.mcq2, command=lambda: self.setuserans(self.mcq2), height=4,
                                 width=40, padx=10, pady=10, font=("roboto", 12), background="#f991cc",
                                 foreground="#110b11")
        self.mcqbutton3 = Button(self.master, text=self.mcq3, command=lambda: self.setuserans(self.mcq3), height=4,
                                 width=40, padx=10, pady=10, font=("roboto", 12), background="#f991cc",
                                 foreground="#110b11")
        self.mcqbutton4 = Button(self.master, text=self.mcq4, command=lambda: self.setuserans(self.mcq4), height=4,
                                 width=40, padx=10, pady=10, font=("roboto", 12), background="#f991cc",
                                 foreground="#110b11")
        # self.nextbutton = Button(self.master, text="Continue", command=self.next_button , font=("Roboto" , 24) , background="#fee1c7" , foreground="#110b11")

        # placements
        self.qlabel.place(x=200, y=100)
        self.mcqbutton1.place(x=300, y=300)
        self.mcqbutton2.place(x=800, y=300)
        self.mcqbutton3.place(x=300, y=500)
        self.mcqbutton4.place(x=800, y=500)
        # self.nextbutton.place(x=1000,y=650)

    def setuserans(self, buttonstring):
        self.userchoice = buttonstring
        self.check_answer()
        self.attributes.count = 5
        self.changeframe()
        print("The answer is : ", self.attributes.useranscorrect)

    def next_button(self):
        self.changeframe()

    def check_answer(self):
        if str(self.userchoice) == str(self.attributes.correctans):
            self.attributes.useranscorrect = True
        else:
            self.attributes.useranscorrect = False


# Class below optional
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


class Answerframe(SNLFrame):
    def __init__(self, master, attributes) -> None:
        super().__init__(master, attributes)
        self.attributes = attributes
        if self.attributes.useranscorrect == True:
            self.displaytext = "Congratulations! You just earned a point!"
        elif self.attributes.useranscorrect == False:
            self.displaytext = "Aw, Try again!"
        else:
            self.displaytext = "Amazing you managed to find a loophole."
        # declaration
        self.answerlabel = Label(self.master, text=self.attributes.correctans, font=("Corbel", 36),
                                 foreground="#110b11", background="#fee1c7", padx=10, pady=20)
        self.nextbutton = Button(self.master, text="Continue", command=self.next_button, font=("Roboto", 24),
                                 background="#fee1c7", foreground="#110b11")
        self.congratulations = Label(self.master, text=self.displaytext, font=("Corbel", 36), foreground="#110b11",
                                     background="#fee1c7", padx=10, pady=20)
        # placements
        self.answerlabel.place(x=200, y=100)
        self.congratulations.place(x=200, y=300)
        self.nextbutton.place(x=1000, y=650)

    def next_button(self):
        self.addpoints()
        self.attributes.count = 3
        self.changeframe()

    def addpoints(self):
        # ladder action if answer right
        if self.attributes.userboolean == True and self.attributes.useranscorrect == True and self.attributes.questiontype == "ladder":
            self.attributes.player1index = self.attributes.potentialindex
            self.attributes.player1score += 1
        elif self.attributes.userboolean == False and self.attributes.useranscorrect == True and self.attributes.questiontype == "ladder":
            self.attributes.player2index = self.attributes.potentialindex
            self.attributes.player2score += 1
        # snake actions if right
        if self.attributes.userboolean == True and self.attributes.useranscorrect == True and self.attributes.questiontype == "snake":
            self.attributes.player1score += 1
            pass
        elif self.attributes.userboolean == False and self.attributes.useranscorrect == True and self.attributes.questiontype == "snake":
            self.attributes.player2score += 1
            pass
        # snake actions if wrong
        if self.attributes.userboolean == True and self.attributes.useranscorrect == False and self.attributes.questiontype == "snake":
            self.attributes.player1index = self.attributes.potentialindex
        elif self.attributes.userboolean == False and self.attributes.useranscorrect == False and self.attributes.questiontype == "snake":
            self.attributes.player2index = self.attributes.potentialindex
        # surprise if right
        if self.attributes.userboolean == True and self.attributes.useranscorrect == True and self.attributes.questiontype == "surprise":
            self.attributes.player1score += 1
            pass
        elif self.attributes.userboolean == False and self.attributes.useranscorrect == True and self.attributes.questiontype == "surprise":
            self.attributes.player2score += 1
        # surprise if wrong
        if self.attributes.userboolean == True and self.attributes.useranscorrect == False and self.attributes.questiontype == "surprise":
            self.attributes.player1index = self.attributes.potentialindex
        elif self.attributes.userboolean == False and self.attributes.useranscorrect == False and self.attributes.questiontype == "surprise":
            self.attributes.player2index = self.attributes.potentialindex
        self.attributes.useranscorrect = False
        self.attributes.userboolean = not self.attributes.userboolean


class Explanationframe(SNLFrame):
    def __init__(self, master, attributes) -> None:
        self.master = Frame(master, width=1280, height=720, background="#E6E6FA")
        super().__init__(master, attributes)
        self.attributes = attributes
        self.explanation = """
        You roll a dice. Then you move that many steps​
        \n
        The questions are history and geography focused.​
        \n
        If you land upon a square with a question, you must answer it, else you will regress 1 step.​
        \n
        If you land at the bottom of the ladder, you must answer the question to proceed upwards, 
        \n
        if you land on the mouth of a snake, you must answer the question correctly to not proceed downwards.​
        \n
        First to reach square 100 wins.
        \n
        """
        self.explanationheader = Label(self.master, text="Rules As Below...", font=("Corbel", 32), foreground="#110b11",
                                       background="#fee1c7", padx=10, pady=20)
        self.explanationtext = Label(self.master, text=self.explanation, font=("Roboto", 12), foreground="#110b11",
                                     background="#fee1c7", padx=10, pady=20)
        self.continuebutton = Button(self.master, text="Continue", command=lambda: self.changeframe(),
                                     font=("Roboto", 24), background="#fee1c7", foreground="#110b11")
        self.continuebutton.place(x=1000, y=650)
        self.explanationtext.place(x=100, y=200)
        self.explanationheader.place(x=100, y=50, anchor="w")
        self.attributes.count = 3


class Playingboard(SNLFrame):
    def __init__(self, master, attributes):
        super().__init__(master, attributes)
        self.attributes = attributes
        self.userboolean = self.attributes.userboolean  # This is the player turn indicator

        # canvas grid system
        self.canvas = Canvas(self.master, width=600, height=600, background="#698B22")

        self.snake_ls = [
            (26, 13), (41, 22), (68, 51), (78, 15), (98, 61)
        ]

        self.ladder_ls = [
            (2, 24), (12, 71), (32, 46), (43, 84), (66, 88)
        ]
        self.surprise_ls = [
            (7, 6), (9, 8), (11, 10), (16, 15), (21, 20), (26, 25),
            (29, 28), (35, 34), (38, 37), (50, 49), (45, 44),
            (54, 53), (56, 55), (59, 58), (63, 62), (72, 71),
            (76, 75), (78, 77), (82, 81), (86, 85), (90, 89), (93, 92)
        ]

        def create_grid(event=None):
            w = self.canvas.winfo_width()  # Get current width of canvas
            h = self.canvas.winfo_height()  # Get current height of canvas
            self.canvas.delete('grid_line')  # Will only remove the grid_line

            # Creates all vertical lines at intevals of 100
            for i in range(0, w, 60):
                self.canvas.create_line([(i, 0), (i, h)], tag='grid_line', fill='white')

            # Creates all horizontal lines at intevals of 100
            for i in range(0, h, 60):
                self.canvas.create_line([(0, i), (w, i)], tag='grid_line', fill='white')

        self.canvas.bind('<Configure>', create_grid)
        self.create_graphics()
        self.canvascreateindexes()

        # player demarcation below
        self.player1initial = self.canvas.create_rectangle(self.indextoboardlocation(self.attributes.player1index),
                                                           fill="white")
        self.x1, self.y1, self.x2, self.y2 = self.indextoboardlocation(self.attributes.player2index)
        print(self.attributes.player1index, self.attributes.player2index)
        self.player2initial = self.canvas.create_rectangle(self.x1 + 30, self.y1 - 30, self.x2 + 30, self.y2 - 30,
                                                           fill="black")

        # label declarations
        self.labeltitle = Label(self.master, text=" THE SHOWDOWN BOARD ", font=("Corbel", 36), foreground="#110b11",
                                padx=10, pady=10)
        self.player1label = Label(self.master, text="Player 1 ", font=("Corbel", 24), background="#8B5A00")
        self.player2label = Label(self.master, text="Player 2", font=("Corbel", 24), background="#8B5A00")
        self.dice1 = Label(self.master, text=0, background="#fee1c7", font=("Roboto", 36), height=2, width=4)
        self.dice2 = Label(self.master, text=0, background="#fee1c7", height=2, width=4, font=("Roboto", 36))
        self.player1point = Label(self.master, text="Player 1 Points", font=("Corbel", 24), background="#8B5A00")
        self.player2point = Label(self.master, text="Player 2 Points", font=("Corbel", 24), background="#8B5A00")
        self.player1counter = Label(self.master, text=self.attributes.player1score, font=("Corbel", 24),
                                    background="#8B5A00")
        self.player2counter = Label(self.master, text=self.attributes.player2score, font=("Corbel", 24),
                                    background="#8B5A00")
        self.close_button = Button(self.master, text="Quit Game", command=master.quit, font=("Roboto", 24),
                                   background="#fee1c7", foreground="#110b11")
        self.rolldicebutton = Button(self.master, text="Roll Dice", command=lambda: self.rollinganimation(),
                                     font=("Roboto", 24), background="#fee1c7", foreground="#110b11")
        # Popup system with waiting here
        self.popupsnake = Label(self.master)
        self.popupladder = Label(self.master)
        self.popupnextplayer = Label(self.master)
        self.popuprandomhit = Label(self.master)

        # Below Are positional placements
        self.canvas.place(x=340, y=100)
        self.labeltitle.place(x=350, y=10)
        self.player1label.place(x=50, y=150)
        self.dice1.place(x=100, y=200)
        self.player2label.place(x=50, y=350)
        self.dice2.place(x=100, y=400)
        self.close_button.place(x=1000, y=600)
        self.player1point.place(x=1000, y=100)
        self.player2point.place(x=1000, y=300)
        self.player1counter.place(x=1000, y=150)
        self.player2counter.place(x=1000, y=350)
        self.rolldicebutton.place(x=100, y=600)

    def create_graphics(self):
        for i in self.ladder_ls:
            x01, y01, x04, y04 = self.indextoboardlocation(i[0])
            x11, y11, x14, y14 = self.indextoboardlocation(i[1])
            self.canvas.create_line(x01 + 15, y01 - 30, x11 + 15, y14, width=5)  # left-slide-ladder
            self.canvas.create_line(x04 + 15, y01 - 30, x14 + 15, y14, width=5)  # right-slide-ladder
            ydif = (y14 - y01 + 30) / 5
            xdif = (x11 - x01) / 5
            for j in range(1, 5):
                self.canvas.create_line(x01 + 15 + xdif * j, y01 - 30 + ydif * j, x04 + 15 + xdif * j,
                                        y01 - 30 + ydif * j, width=5)  # left-slide-ladder

        for i in self.snake_ls:
            x01, y01, x04, y04 = self.indextoboardlocation(i[0])
            x11, y11, x14, y14 = self.indextoboardlocation(i[1])
            if x01 < x11:
                self.canvas.create_line(
                    x01 + 35, y01 - 15, x11 + 10, y11 - 35,  # leftside
                    x11 + 25, y11 - 50, x01 + 50, y01 - 30,  # rightside
                    x01 + 35, y01 - 15, width=5, fill="dark green")
            else:
                self.canvas.create_line(
                    x01 + 10, y01 - 30, x11 + 35, y11 - 50,  # leftside
                    x11 + 50, y11 - 35, x01 + 25, y01 - 15,  # rightside
                    x01 + 10, y01 - 30, width=5, fill="dark green")

    def rollinganimation(self):
        """self.variable  = random.randint(1,6)
        self.dice1 = Label(self.master , text= self.variable , background="#fee1c7" , font = ("Roboto" , 36 ),height=2 , width= 4 )
        self.dice1.place(x=100,y=200)"""
        time.sleep(0.2)
        outcomenumber = random.randint(1, 6)
        # Reminder that true is player1, player2 is false
        if self.attributes.userboolean == True:
            self.dice1 = Label(self.master, text=outcomenumber, background="#fee1c7", font=("Roboto", 36), height=2,
                               width=4)
            self.dice1.place(x=100, y=200)
            self.attributes.player1index += outcomenumber
            print("Player 1 Index: ", self.attributes.player1index)
        elif self.attributes.userboolean == False:
            self.dice2 = Label(self.master, text=outcomenumber, background="#fee1c7", height=2, width=4,
                               font=("Roboto", 36))
            self.dice2.place(x=100, y=400)
            self.attributes.player2index += outcomenumber
            print("Player 2 Index: ", self.attributes.player2index)

        self.attributes.checkendgame()  # incase someone wins immediate
        if self.attributes.endgameboolean == True:  # str8 forward to end game screen
            if self.attributes.userboolean == True:
                messagebox.showerror("CONGRATS", "Player 1 Won!")
                print("Player 1 Won")
            elif self.attributes.userboolean == False:
                messagebox.showerror("CONGRATS", "Player 2 Won!")
                print("Player 2 Won")
            self.attributes.count = 7
            self.changeframe()
            return
        else:
            pass
        # Now displace the movement. Player 1 is by default white, Player 2 is by default black
        if self.attributes.userboolean == True:
            x1, y1, x2, y2 = self.indextoboardlocation(self.attributes.player1index)
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            self.gotquestion = self.check_prompt(self.attributes.player1index)
            self.canvas.delete(self.player1initial)  # this works
            self.attributes.count = 3.5
        elif self.attributes.userboolean == False:
            x1, y1, x2, y2 = self.indextoboardlocation(self.attributes.player2index)
            self.canvas.create_rectangle(x1 + 30, y1 - 30, x2 + 30, y2 - 30, fill="black")
            self.canvas.delete(self.player2initial)  # this works
            self.gotquestion = self.check_prompt(self.attributes.player2index)
        if self.gotquestion:
            self.attributes.count = 4
        elif self.gotquestion == False:
            self.attributes.count = 3.5
        self.changeframe()
        # Below is to check if hit question, and if yes, what type of prompt to show
        # self.showprompt()

    def check_prompt(self, index):
        for i in range(len(self.snake_ls)):
            if index == self.snake_ls[i][0]:
                i1 = self.snake_ls[i][1]
                b = self.snake(i1)
                self.attributes.potentialindex = i1
                self.attributes.questiontype = "snake"
                return True
            else:
                pass
        for i in range(len(self.ladder_ls)):
            if index == self.ladder_ls[i][0]:
                i1 = self.ladder_ls[i][1]
                b = self.ladder(i1)
                self.attributes.potentialindex = i1
                self.attributes.questiontype = "ladder"
                return True
                return True
            else:
                pass
        for i in range(len(self.surprise_ls)):
            if index == self.surprise_ls[i][0]:
                i1 = self.surprise_ls[i][1]
                b = self.surprise(i1)
                self.attributes.potentialindex = i1
                self.attributes.questiontype = "surprise"
                return True
            else:
                pass
        if self.attributes.userboolean == True:
            messagebox.showerror("Next Player", "Player 1, Now it's your turn")
            self.attributes.userboolean = False
        else:
            messagebox.showerror("Next Player", "Player 2, Now it's your turn")
            self.attributes.userboolean = True
        return False

    def snake(self, i1):
        messagebox.showerror("Snake",
                             "You stepped on snake! Answer this qn correctly or else you will have to fall back to tile {}".format(
                                 i1))

    def ladder(self, i1):
        messagebox.showerror("Ladder", "You stepped on ladder! Answer this qn correctly to move to tile {}".format(i1))

    def surprise(self, i1):
        messagebox.showerror("Surprise",
                             "You stepped on surprise! Answer this qn correctly or else you will have to fall back to tile {}".format(
                                 i1))

    def canvascreateindexes(self):
        for x in range(1, 101):
            coord = self.indextoboardlocation(x)
            self.canvas.create_text(coord[0] + 28, coord[1] - 28, text=str(x), fill="white", font=('Corbel 12 bold'))

    def indextoboardlocation(self, index):
        j = index % 20
        if j > 0 and j < 11:
            x = 60 * (j - 1)
        elif j == 0:
            x = 0
        else:
            x = 540 - 60 * (j - 11)
        m = x + 30
        k = int((index - 1) / 10)
        y = 600 - 60 * k
        n = y - 30
        return x, y, m, n  # x,y bottom coords, m,n topright coords


rootmaster = Tk()
rootmaster.geometry("1280x720")
rootmaster.configure(background="#8B5A00")
roundstart = Round(rootmaster)  # roundstart is the object for holding all information
rootmaster.mainloop()
# Above all tkinter initiation
