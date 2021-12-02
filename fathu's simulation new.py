class p1_turn():
    def __init__(self,index):
        self.index = index

    def snake(self,i1):
        # messagebox.showerror("Snake","You stepped on snake! Answer this qn correctly or else you will have to fall back to tile {}".format(i1))
        print("Snake",
              "You stepped on snake! Answer this qn correctly or else you will have to fall back to tile {}".format(i1))

    def ladder(self,i1):
        # messagebox.showerror("Ladder","You stepped on ladder! Answer this qn correctly or else you will have to fall back to tile {}".format(i1))
        print("Ladder", "You stepped on ladder! Answer this qn correctly to move to tile {}".format(i1))

    def surprise(self,i1):
        # messagebox.showerror("Surprise","You stepped on surprise! Answer this qn correctly or else you will have to fall back to tile {}".format(i1))
        print("Surprise",
              "You stepped on surprise! Answer this qn correctly or else you will have to fall back to tile {}".format(
                  i1))
        
while end == 0:
    p1.roll_dice()
    for i in range(len(snake_ls)):
        if p1.index == snake_ls[i][0]:
            b = p1.snake(snake_ls[i][1])
        else:
            pass
    for i in range(len(ladder_ls)):
        if p1.index == ladder_ls[i][0]:
            b = p1.ladder(ladder_ls[i][1])
        else:
            pass
    for i in range(len(surprise_ls)):
        if p1.index == surprise_ls[i][0]:
            b = p1.surprise(surprise_ls[i][1])
        else:
            pass
    print(p1.bot_left())
    print("p1 turn done")
