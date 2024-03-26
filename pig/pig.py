import random
import sys

# roll the dice
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(1, 6)

    return roll

while True:
    players = input("Enter the number of players (1 - 4) (0 to quit): ")
    if players == '0':
        sys.exit() # exit the whole game
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print("Invalid: try again.")
        
max_score = 25
player_scores = [0 for _ in range(players)] # initialize all the players to 0

while max(player_scores) < max_score:
    
    for player_idx in range(players):
        current_score = 0
        print("\nPlayer", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != 'y':
                break

            value = roll()

            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            
            else: 
                current_score += value
                print("You rolled a", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("player", winning_idx + 1, "is the winner with the score of:", max_score)