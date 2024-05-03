#from turtle import Turtle, Screen
#from random import random


#danny = Turtle()
#print(danny)
#danny.shape("turtle")
#danny.color("#ab99f1")
#danny.forward(100)

#for i in range(10):
#   steps = int(random() * 100)
#    angle = int(random() * 360)
#    danny.right(angle)
#    danny.fd(steps)


#my_screen = Screen()

#print(my_screen.canvheight)
#my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align  = ("l")
print()
print(table)