from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Ubuntu", 16, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0         
        
        
    def score_board(self):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 270)
        self.write(f"Score: {self.player_score}", move=True, align= ALIGNMENT, font= FONT)
               

    def change_score(self):
        self.player_score += 1
    

    def game_over(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 0)
        self.write("Game Over", move=False, align='center', font=FONT)
        
        
        
        