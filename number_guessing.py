import random

best_score = max_guess = 10

while True:
    guess_count = 0
    print('         Welcome To Guess The Number Game!')
    while True:
        try:
            min_value = int(input('Enter the min number: '))
            max_value = int(input('Enter the max number: '))
            break
        except ValueError:
            print('Invalid input!, Please use whole non-negative numbers')

    computer_number = random.randint(max_value,max_value)
    user_guess = 0
    while computer_number != user_guess:
        # Get user input for range of values to guess from
        try:
            user_guess = int(input(f'Guess a number between {min_value} and {max_value}: '))
            guess_count +=1
            #End Game if user exceeds max tries
            if guess_count >= max_guess:
                print('    GameOver!')
                print(f'The Answer is {computer_number}')
                break
        except ValueError:
            print('Invalid input!, Please use whole non-negative numbers')
        # Compare User Guess to computer number
        if computer_number > user_guess:
                print('Too Low!')
                continue
        elif computer_number < user_guess:
                print('Too High!')
                continue
        print(f'Congratulations you guess {user_guess} is correct')
        # Check if user has new high score
        if guess_count < best_score:
            best_score = guess_count 
            print(f'New High Score: {best_score}')

    # Start New Game or Exit
    while True:
        play_again = input("Play Again (y/n)").lower()
        if play_again != 'n' and play_again != 'y':
            print('Invalid Input!')
        else:
            break
    if play_again == 'n':
        print('Thanks For Playing!')
        break



