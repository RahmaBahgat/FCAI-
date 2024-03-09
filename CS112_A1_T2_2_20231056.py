# File: CS112_A1_T1_2_20231056.pdf
# Purpose: Number scrabble is played with the list of numbers between 1 and 9. Each player takes
# turns picking a number from the list. Once a number has been picked, it cannot be picked
# again. If a player has picked three numbers that add up to 15, that player wins the game.
# However, if all the numbers are used and no player gets exactly 15, the game is a draw.
# Author: Rahma Bahgat Muhammed Essa
# ID: 20231056

# Importing the random library for generating random choices
import random
# Importing permutations from itertools to generate all possible combinations of numbers
from itertools import permutations
# Function to get player names and choose randomly first player


def inputs():
    first_input = input("Enter the first player's name: ")
    second_input = input("Enter the second player's name: ")
    players = [first_input, second_input]
    player1 = random.choice(players)
    print(f"The first player is: {player1}")
    if player1 == players[0]:
        player2 = players[1]
    else:
        player2 = players[0]
    return player1, player2

# Function to check if a player has won


def check_winner(current_player, numbers):
    # Making all combinations
    combinations = permutations(numbers, 3)
    # Checking if the sum of any combination equals 15
    for p in combinations:
        if sum(p) == 15:
            print(f"The numbers couldn't resist your charm, {current_player}! You've won!")
            return True
    return False

# Main function to run the game


def main():
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers_of_player1 = []
    numbers_of_player2 = []
    # Explaining the game and its rules
    print("Welcome to the Number Scrabble game")
    print("From 1 to 9, each player takes turns picking a number.\n"
          "If a player has picked three numbers that add up to 15, that player wins.\n"
          "Once a number has been picked, it cannot be picked again.\n"
          "Wish you a happy game!")
    # Menu for the user to decide whether they want to play or exit
    while True:
        print("Do you want to play?")
        start_or_exit = input("1)Start\n"
                              "2)Exit\n")

        start_or_exit = start_or_exit.lower()
        if start_or_exit == '2' or start_or_exit == 'exit':
            print(f'Goodbye, players! Remember, the thrill of Number Scrabble awaits your return!')
            break
        elif start_or_exit == '1' or start_or_exit == 'start':
            player1, player2 = inputs()
            current_player = player1
            # Loop to handle players taking turns picking numbers
            for _ in range(len(list_of_numbers)):
                print(f"The available numbers are {list_of_numbers}")
                print(f"Numbers chosen by {player1}: {numbers_of_player1}")
                print(f"Numbers chosen by {player2}: {numbers_of_player2}")
                print(f"{current_player}'s turn")
                player_choice = []
                while not player_choice:
                    choice = input("Enter your choice: ")
                    # Checking input's validity
                    if choice.isdigit():
                        choice = int(choice)
                        if choice not in list_of_numbers:
                            print("Please enter a valid choice from the available numbers.")
                        else:
                            player_choice.append(choice)
                            break
                    else:
                        print("Invalid! Please enter a valid integer choice.")

                if current_player == player1:
                    numbers_of_player1.extend(player_choice)
                    # Checking & announcing the winner
                    if check_winner(current_player, numbers_of_player1):
                        break
                    current_player = player2
                else:
                    numbers_of_player2.extend(player_choice)
                    if check_winner(current_player, numbers_of_player2):
                        break
                    current_player = player1

                list_of_numbers.remove(player_choice[0])

            else:
                print("It's a draw!")
        else:
            print("Invalid!")

# Call the main function to start the game


main()
