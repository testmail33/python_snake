from turtle import Turtle


class Scoreboard (Turtle):
    def __init__(self):
        super ().__init__ ()
        self.hideturtle()
        self.color ("white")
        self.penup ()
        self.goto (0, 270)
        self.score = 0
        with open ("data.txt") as file:
            self.high_score = int(file.read())
        self.update_score()


    def update_score(self):
        self.clear ()
        self.write (arg=f"Score : {self.score}, High_score : {self.high_score}", move=False, align="center",font=("Arial", 12, "normal"))

    def increase_score(self):
        self.clear ()
        self.score += 1
        self.update_score()


    def reset(self):
        if self.score > self.high_score:
            with open ("data.txt", "w") as file:
                file.write(str(self.score))
            with open ("data.txt") as file:
                self.high_score = int(file.read ())
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.home ()
    #     self.write (arg="Game Over", move=False, align="center", font=("Arial", 12, "normal"))
