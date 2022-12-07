from tkinter import *
import random
# class variables 
GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 100 # milliseconds
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#16123f"
FOOD_COLOR = "#ffe26a"
BACKGROUND_COLOR = "#75c9b7"
# create Snake class
 #TODO: is being able to go left and up at the same time 
 #TODO: not spawning apple/food on snake body 
 #TODO: Winners screen if game is completed
 #TODO: change font and display zs

class Snake:
    # initialize the snake
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
       # create a list of coordinates for the snake
        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])
       # create squares for the snake
        for x, y in self.coordinates:
           square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
           self.squares.append(square)
            
    
class Food:
    # initialize the food
    def __init__(self):
        # get random coordinates 0-14 
        x = random.randint(0, (GAME_WIDTH - SPACE_SIZE) / SPACE_SIZE) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT - SPACE_SIZE) / SPACE_SIZE) * SPACE_SIZE
        
        self.coordinates = [x, y]
        # create food
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
# define all methods
def next_turn(snake, food):
    #unpack the coordinates of the snake's head
    x, y = snake.coordinates[0]
    if direction == "Up":
        y -= SPACE_SIZE
    elif direction == "Down":
        y += SPACE_SIZE
    elif direction == "Left":
        x -= SPACE_SIZE
    elif direction == "Right":
        x += SPACE_SIZE
# update the coordinates of the snake's head
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
    snake.squares.insert(0, square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        # increase score
        global score
        score += 1
        # change label
        Label.config(text="Score: {}".format(score))
        # if the snake has eaten the food, replace the food
        canvas.delete("food")
        food = Food()
    else:
        # delete the snake's tail
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    # if else for collision
    if check_collisions(snake):
        game_over()
    else:
     window.after(SPEED, next_turn, snake, food)
def change_direction(event):
    # change the direction of the snake
    global direction
    
    if event == "Up" and direction != "Down":
        direction = event
    elif event == "Down" and direction != "Up":
        direction = event
    elif event == "Left" and direction != "Right":
        direction = event
    elif event == "Right" and direction != "Left":
        direction = event
    elif event == "Up" and direction != "Down":
        direction = event
        
def check_collisions(snake):
    # check if the snake has collided with itself or the wall
     x, y = snake.coordinates[0]
     if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
         print("Ohh no!... You hit the wall")
         return True
     # now in case the new head is in the same position as any other part of the body
     for body_part in snake.coordinates[1:]:
         if x == body_part[0] and y == body_part[1]:
             print("Ohh no!... You hit yourself")
             return True
     return False 
def game_over():
   canvas.delete(ALL)
   canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, text="Game Over! ", 
                      fill="white", font=("Great Vibes", 44), tag="gameover")
 # TODO: add a restart button  
# def restart():
#     canvas.delete(ALL)
#     main()
window = Tk()
window.title("Cora.Cell")

score = 0
direction = "Right"

# create label for the score
Label = Label(window, text="Score: " + str(score), font=("Helvetica", 20))
Label.pack()

canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

# center the canvas when it pops up
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width/2) - (window_width/2)
y = (screen_height/2) - (window_height/2)

window.geometry("+%d+%d" % (x, y))
# create controls/bindings
window.bind("<Up>", lambda event:change_direction("Up"))
window.bind("<Down>", lambda event:change_direction("Down"))
window.bind("<Left>", lambda event:change_direction("Left"))
window.bind("<Right>", lambda event:change_direction("Right"))
window.bind("<W>", lambda event:change_direction("Up"))
window.bind("<S>", lambda event:change_direction("Down"))
window.bind("<A>", lambda event:change_direction("Left"))
window.bind("<D>", lambda event:change_direction("Right"))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
