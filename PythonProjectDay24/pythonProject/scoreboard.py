from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")




class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write_high_score(new_score=self.score)
        self.write(f"Score: {self.score}  High Score: {self.read_high_score()}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def read_high_score(self):
        with open("my_file.txt") as file:
            high_score = file.read()
            return high_score

    def write_high_score(self, new_score):
        with open("my_file.txt","w") as file:
            file.write(str(new_score))


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.read_high_score()):
            self.write_high_score(self.score)
        self.score = 0