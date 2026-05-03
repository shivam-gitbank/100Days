def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    if right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
        

while at_goal() != True:
    if wall_in_front() and wall_on_right():
        jump()
    elif right_is_clear():
        turn_right()
        move()
    else:
        move()