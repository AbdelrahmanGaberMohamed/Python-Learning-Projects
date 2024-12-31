import random 

rock = "🪨"
paper = "📄"
scissors = "✂️"
computer_win = 'Computer Wins 😔'
player_win = 'Player Wins 👑'
rock_paper = f'Paper {paper} Covers Rock  {rock}'
rock_scissors = f'Rock {rock}  Crushes scissors {scissors}'
paper_scissors = f'Scissors {scissors}  Cuts Paper {paper}'
player_score = computer_score = 0
choices = ('r', 'p', 's')
def rock_paper_scissros(input_char):
    match input_char:
        case 'r':
            input_char = rock
        case 'p':
            input_char = paper
        case 's':
            input_char = scissors
    #print(input_char)
    return input_char

while True:
    print(' ' *6 + f'ScoreBoard\n   Player  |   Computer \n     {player_score}           {computer_score}\n')
    print(f'Welcome To Rock {rock}  Paper {paper} Scissors {scissors}')
    #Start New Game or Exit
    while True:
        start_game = input(' '*10 + 'Start (y/n)').lower()
        if start_game != 'y' and start_game != 'n':
            print('Invalid Input! 😟')
            continue
        else:
            break
    if start_game == 'n':
        print('Thanks For Playing!')
        break
    computer_win_streak = 0
    player_win_streak = 0 

    while computer_win_streak < 2 and player_win_streak < 2:
        computer_choice = random.choice(choices)
        computer_hand = rock_paper_scissros(computer_choice)

        player_choice = input('Rock, Paper, Scissors (r,p,s): ').lower()
        if player_choice not in choices:
            print('Invalid Input! 😟')
            continue
        else:
            player_hand = rock_paper_scissros(player_choice)
            score_board = f'    Player  |   Computer \n     {player_hand}           {computer_hand}\n'
            # Game Score logic:
            #   Rock beats scissors.
            #   Scissors beats paper.
            #   Paper beats rock
            if player_hand == computer_hand:
                print(f'Draw')
                continue
            if player_hand == rock and computer_hand == paper:
                print(score_board + rock_paper)
                print(computer_win)
                computer_win_streak +=1
            elif player_hand == rock and computer_hand == scissors:
                print(score_board + rock_scissors)
                print(player_win)
                player_win_streak +=1
            elif player_hand == paper and computer_hand == rock:
                print(score_board + rock_paper)
                print(player_win)
                player_win_streak +=1
            elif player_hand == paper and computer_hand == scissors:
                print(score_board + paper_scissors)
                print(computer_win)
                computer_win_streak +=1
            elif player_hand == scissors and computer_hand == rock: 
                print(score_board + rock_scissors)
                print(computer_win)
                computer_win_streak +=1
            elif player_hand == scissors and computer_hand == paper:
                print(score_board + paper_scissors)
                print(player_win)
                player_win_streak +=1
            else:
                print('Undefiend Error 😟!')
                break

    if player_win_streak == 2:
        print('Player Victory! 👑')
        player_score +=1
    else:
        print('Player Defeat! 😔')
        computer_score +=1

