snake_ls = [
    (26,13),(41,22),(68,51),(78,15),(98,61)
]

ladder_ls = [
    (2,24),(12,71),(32,46),(43,84),(66,88)
]
surprise_ls = [
    (7, 6), (9, 8), (11, 10), (16, 15), (21, 20), (26, 25),
    (29, 28), (35, 34), (38, 37), (50, 49), (45, 44),
    (54, 53), (56, 55), (59, 58), (63, 62), (72, 71),
    (76, 75), (78, 77), (82, 81), (86, 85), (90, 89), (93, 92)
]

class p1_turn():
    def __init__(self,index):
        self.index = index

    def snake(self,i1):
        # messagebox.showerror("Snake","You stepped on snake! Answer this qn correctly or else you will have to fall back to tile {}".format(i1))
        print("Snake","You stepped on snake! Answer this qn correctly or else you will have to fall back to tile {}".format(i1))

    def ladder(self,i1):
        # messagebox.showerror("Ladder","You stepped on ladder! Answer this qn correctly to move to tile {}".format(i1))
        print("Ladder", "You stepped on ladder! Answer this qn correctly to move to tile {}".format(i1))

    def surprise(self,i1):
        # messagebox.showerror("Surprise","You stepped on surprise! Answer this qn correctly or else you will have to fall back to tile {}".format(i1))
        print("Surprise","You stepped on surprise! Answer this qn correctly or else you will have to fall back to tile {}".format(i1))
        
def check_prompt(p1.index):
    for i in range(len(snake_ls)):
        if p1.index == snake_ls[i][0]:
            i1 = snake_ls[i][1]
            b = p1.snake(i1)
        else:
            pass
    for i in range(len(ladder_ls)):
        if p1.index == ladder_ls[i][0]:
            i1 = ladder_ls[i][1]
            b = p1.ladder(i1)
        else:
            pass
    for i in range(len(surprise_ls)):
        if p1.index == surprise_ls[i][0]:
            i1 = surprise_ls[i][1]
            b = p1.surprise(i1)
        else:
            pass
