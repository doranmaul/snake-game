from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.coords = 0
        self.snakes = []
        self.create_snakes()
        self.head = self.snakes[0]

    def create_snakes(self):
        for turtle_index in range(0, 3):
            self.add_snake(turtle_index)

    def add_snake(self, turtle_index):
        tim = Turtle()
        tim.penup()
        tim.color("white")
        tim.shape("square")
        tim.goto(self.coords, 0)
        self.coords -= 20
        self.snakes.append(tim)

    def extend(self):
        # adds new snakes to the end of snake
        self.add_snake(self.snakes[-1].position())
    def move(self):
        for objects in range(len(self.snakes) - 1, 0, -1):  # This takes turtles starting from the end of the list and sends them to the turtle position in front of it
            new_x = self.snakes[objects - 1].xcor()  # So over time each turtle (square) is following itself
            new_y = self.snakes[objects - 1].ycor()  # So when the front (first) turtle turns or makes a move, each turtle (square) behind it follows suit
            self.snakes[objects].goto(new_x, new_y)  # It's an interesting (and sort of mind-bending) way to create the infinite "snake" animation
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)



