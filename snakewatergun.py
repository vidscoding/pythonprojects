#snake water gun game
# a player choose snake or water or gun
# snake-water; snakes wins
#gun-water ; gun drowns in water
#snake-gun ;gun kills the snake

import random

swg = ['s', 'w', 'g']

attempts = 10
num_of_attempts = 0
comps_score = 0
user_score = 0

print("s for snake \nw for water \ng for gun \n")

while num_of_attempts < attempts:
    user_input = input("Snake, Water, Gun: ")
    rand = random.choice(swg)

    if user_input == rand:
        print("Both get a 0 point")

    elif user_input == 's' and rand == 'g':
        comps_score = comps_score + 1
        print(f"Your guess {user_input} and computer guess is {rand} \n")
        print("Computer gets 1 point\n")
        print(f"Computer point is {comps_score} and your point is {user_score}\n")

    elif user_input == 'g' and rand == 's':
        user_score = user_score +1
        print(f"Your guess {user_input} and computer guess is {rand} \n")
        print("You get 1 point\n")
        print(f"Computer point is {comps_score} and your point is {user_score}\n")

    elif user_input == 'g' and rand == 'w':
        comps_score = comps_score +1
        print(f"Your guess {user_input} and computer guess is {rand} \n")
        print("Computer gets 1 point\n")
        print(f"Computer point is {comps_score} and your point is {user_score}\n")

    elif user_input == 'w' and rand == 'g':
        user_score = user_score +1
        print(f"Your guess {user_input} and computer guess is {rand} \n")
        print("You get 1 point\n")
        print(f"Computer point is {comps_score} and your point is {user_score}\n")

    elif user_input == 's' and rand == 'g':
        comps_score = comps_score +1
        print(f"Your guess {user_input} and computer guess is {rand} \n")
        print("Computer gets 1 point\n")
        print(f"Computer point is {comps_score} and your point is {user_score}\n")

    elif user_input == 'g' and rand == 's':
        user_score = user_score + 1
        print(f"Your guess {user_input} and computer guess is {rand} \n")
        print("You get 1 point\n")
        print(f"Computer point is {comps_score} and your point is {user_score}\n")

    else:
        print("You have input wrong \n")

    num_of_attempts = num_of_attempts + 1
    print(f"{attempts - num_of_attempts} is left out of {attempts}\n")

    print("Game Over")

    if comps_score == user_score:
        print("Tie")
    elif comps_score > user_score:
        print("Computer wins and you loose")
    else:
        print("You win and computer looses")

    print(f"Your point is {user_score} and computer point is {comps_score}")
