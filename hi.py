UP_ARROW = 'Up'
LEFT_ARROW = 'Left'
DOWN_ARROW = 'Down'
RIGHT_ARROW = 'Right'
SPACEBAR = 'space'

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
direction = UP

def up():
    global direction
    direction = UP
    print('You pressed UP')

def down():
    global direction
    direction = DOWN
    print ('You pressed DOWN')

def left():
    global direction
    direction = LEFT
    print ('You pressed LEFT')

def right():
    global direction
    direction = RIGHT
    print ('You pressed RIGHT')
    


    

