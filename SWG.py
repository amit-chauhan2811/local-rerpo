# Snake Water Gun or Rock paper scissors
import random

def gameWin(comp, you):
    # If two values are equal , declare a tie!
    if comp == you : 
        return None
   
    elif comp == 's':
        return you == 'g'
    
    elif comp == 'w':
        return you == 's'
    
    elif comp == 'g':
        return you == 'w'

print(("Comp Turn: Snake(s) water(w) or gun(g) ? \n"))
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) water(w) or gun(g) ? \n").lower()

if you not in ['s', 'w','g']:
    print("Invalid input. Please enter correct word.")
else:
    result = gameWin(comp, you)

    print(f"Computer Choose {comp}")
    print(f"You Choose {you}")

if result == None:
   print("The game is a tie!")
elif result:
    print("You win!")
else:
   print("You loss!")
   


    