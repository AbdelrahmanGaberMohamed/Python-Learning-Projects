import random

def roll_dice(dice_number):
    result = ()
    for i in range (0,dice_number):
        dice = random.randint(1,6)
        result = result + (dice,)
        print(dice)
    return 0

#Total number of dice rolls
roll_count = 0
#Number of invaild dice_count input errors
input_tries = 0
#Program choices y:accept, n:quit, d:input number of dice
choice = 'd'

while True:
    while choice == 'd' and input_tries< 3:
        try:
         dice_count = int(input('Enter The Number of Dice: '))
         intput_tries = 0
         break
        except:
            print("Invalid input!, Please use whole non-negative numbers")
            input_tries +=1
    if input_tries == 3:
        print("Too Many Invalid Inputs")
        break

    choice = input("Roll the dice? (y accept/n quit/d input number of dice): ").lower()
    if choice == "y":
        roll_dice(dice_count)
        roll_count += 1
        continue
    elif choice == "n":
        print("Thanks For Playing!")
        break
    elif choice == "d":
        continue
    else:
        print("Invalid Input!")
    