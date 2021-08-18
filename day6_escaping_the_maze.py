#hurdle 4: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# def jump():
#     turn_left()
#     i = 0
#     while wall_on_right():
#         move()
#         i += 1
#     turn_right()
#     move()
#     turn_right()
#     move()
#     while i > 1:
#         move()
#         i-= 1
#     turn_left()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# MAZE ON REEBORG'S WORLD

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if front_is_clear() and right_is_clear():
        move()
    elif not front_is_clear() and right_is_clear():
        turn_right()
    elif front_is_clear() and not right_is_clear():
        move()
        turn_right()
    else:
        turn_left()