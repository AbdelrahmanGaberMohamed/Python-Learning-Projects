import random


guess_count = 0

while True:
    computer_number = random.randint(1,100)
    user_guess = 0
    while computer_number != user_guess:
        try:
            user_guess = int(input('Guess a number between 1 and 100: '))
            if computer_number > user_guess:
                print('Too Low!')
            elif computer_number < user_guess:
                print('Too High!')
            guess_count +=1
        except:
            print('Invalid input!, Please use whole non-negative numbers')

    print(f'Congratulations you guess {user_guess} is correct')
    
    while True:
        play_again = input("Play Again (y/n)").lower()
        if play_again != 'n' and play_again != 'y':
            print('Invalid Input!')
        else:
            break
    if play_again == 'n':
        print('Thanks For Playing!')
        break



