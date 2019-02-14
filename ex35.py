#Ex35: Branches and Functions

from sys import exit

def gold_room():
    print('This room is full of gold. How much do you take?')

    choice = input('> ')

    if choice.isnumeric():
        how_much = int(choice)
    else:
        dead('Man, learn to type a number.')

    if how_much < 99:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead('You greedy bastard!')


def bear_room():
    print('There is a bear here.')
    print('The bear has a bunch of honey.')
    print('The fat bear is in front of another door.')
    print('How are you going to move the bear?')
    bear_moved = False

    while True:
        choice = input('> ')

        if 'honey' in choice:
            dead('The bear looks at you then slaps your face off.')
        elif 'taunt' in choice and not bear_moved:
            print('The bear has moved from the door.')
            print('You can go through it now.')
            bear_moved = True
        elif 'taunt' in choice and bear_moved:
            dead('The bear gets pissed off and chews your legs off.')
        elif 'door' in choice and bear_moved:
            gold_room()
        elif 'door' in choice and not bear_moved:
            print('The bear is in front of the door.')
        else:
            print('I got no idea what that means.')


def dead(why):
    print(why, 'Good job!')
    exit(0)


def start():
    print('You are in a dark room.')
    print('There is a door to your right and left.')
    print('Which one do you take?')

    choice = input('> ')

    if 'left' in choice:
        bear_room()
    elif 'right' in choice:
        dead('The room was dead trap.')
    else:
        dead('You stumble around the room until you starve.')


start()
