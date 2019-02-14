#Ex36.py: Designing and Debugging
# Homework problem
# Maze : Player have to escape the maze using left right and forward only
    
def dead():
    print('You activated some trap, sounds like exit is closed. Good job!')
    exit(0)

def ask_choice():
    print("Which way you want to go")
    ch = input(">")
    return ch

def ask_left():
    print("There is a way to the left")
    ch = ask_choice()
    return ch

def ask_right():
    print("There is a way to the right.")
    ch = ask_choice()
    return ch

def loop_left():
    count =0
    while count != 3:
        choice =ask_left()
        if 'left' in choice:
            count += 1
            continue
        else:
            dead()


def loop_right():
    count =0
    while count != 3:
        choice =ask_right()
        if 'right' in choice:
            count += 1
            continue
        else:
            dead()

def loop(choice):
    while 'forward' not in choice:
        if 'right' in choice:
            loop_right()
            print("It looks you reached where you are started.")
            choice = ask_choice()
        
        if 'left' in choice:
            loop_left()
            print("It looks you reached where you are started.")
            choice = ask_choice()

        else:
            dead()
            
def start():
    print("""You are trapped in a maze.To make matters worse, it's dark everywhere. 
Someone shouted 'Dont walk backward!'
So, which way do you want to go? forward, left or right """)
    choice = input(">")

    loop(choice)

    choice =ask_right()
    if 'right' in choice:
        choice =ask_left()
        if 'left' in choice:
            print("There is way to left and right")
            choice = ask_choice()
            if 'right' in choice:
                print("Congratulations. You have escaped")
            elif 'left' in choice:
                print("You fall into death")
                exit(0)
            else:
                dead()
        else:
            dead()
    else:
        dead()


if __name__ == "__main__":
    start()
            
                
