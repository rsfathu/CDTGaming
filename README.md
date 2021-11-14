Class: Question System 

Module:  

Questionbank() - dictionary with question index classified to difficulty and a formated string inside 

getquestionfromindex() - retrieve a string from the dictionary from a set index 

Questiondeconstructor() - returns a set sequence of string to getqns() 

 

Class: GUI 

Class: 

Introframe()- welcome screen 

Questionframe() pop up question string 

Answerframe() answer correct or wrong screen 

Playingframe() the board screen 

Endgameframe() win game screen w/ play again? 

Class: Turn_Based_System 

Module: 

Setplayerturn() - set player turn 

Setplayerposition() - set original position 

Winconditionchecker() 

Endplayerturn() 

Updateplayerposition() 

Endgame() 

Loop() - loops the above 4 modules to continue till 1 player meets the win condition 

Class: Dice 

Module 

Initialization() - set original dice face – used once 

Rolldice() - roll the dice to get a randomise number 

Updatediceonscreen() - triggers the GUI to update the dice to the new number 

Class: QuestionPopup 

Module 

getqns() - get qns from the return string from dictionary 

setqns() set qns string at GUI to be the question 

serveqns() Trigger pop up at GUI to show question 

Class: Boardinitialization 

Module 

Createindex() - create the 100 squares needed to define position in the game 

Createdice() - create a dice object 

Setquestionindexintoboard() initialize position to be at square 1 

Setplayeroriginalposition() Triggers GUI to show player position at square 1 

 

 

Class Main 
Module 
Initialisation 
Colour Scheme: 

 

f991cc-53599a-fee1c7-52d1dc-110b11 
