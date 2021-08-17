
# square is need to make the head of the snake and food
# vector is needed to manipulate the speed
# randrage is need to randomly generation
# “Turtle” is a python feature like a drawing board

from turtle import *
from random import randrange
from base import square, vector


#variables
food = vector(0, 0)			#center position
snake = [vector(10, 0)]		#snake basic position to matain the list for different size
aim = vector(0, -10)		#position | movement of snake

def change(x, y):
    "Change snake direction."
	# new direction basically changed the snake direction
    aim.x = x
    aim.y = y

def inside(head):			# to check that whether head is within boundary or not
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():					# movement for snake to check that within boundary or not
    "Move snake forward one segment."
    head = snake[-1].copy()			# snake[-1] means head and snake[0] means tail
    head.move(aim)

    if not inside(head) or head in snake:     # if snake strikes itself or boundary
        square(head.x, head.y, 9, 'red')      #make snake die
        update()
        return

    snake.append(head)		    #append the snake in the list as snake died

    if head == food:			# snake eaten food or head strike to the food
        print('Snake:', len(snake))		# print the length of the snake
										# create food at random position
        food.x = randrange(-15, 15) * 10	# x= after eaten food, now food is generated random position
        food.y = randrange(-15, 15) * 10	# y= after eaten food, now food is generated random position
    else:		# if snake does not eat food
        snake.pop(0)		# length should be poped
							# remove the nearest position from the list
    clear()				# clear the console

    for body in snake:	# randomly created variable have the list of all positions of the snake basically the body
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')		# food position
    update()
    ontimer(move, 100)		# ontimer to call the move function to every 100 mili seconds	

setup(420, 420, 370, 0)			#console size
hideturtle()
tracer(False)		# delay should be false there isn't any be delay
listen()

# define keys to play the game
onkey(lambda: change(10, 0), 'Right')		#change function is called defined at top
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()			# move our snake one segment
done()
