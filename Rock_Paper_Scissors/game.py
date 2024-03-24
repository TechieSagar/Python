import random

"""
    Game class representing a simple game of Rock, Paper, Scissors.
    This class has three attributes:
        - computer_pick: The choice made by the computer.
        - user_pick: The choice made by the user.
        - get_result: A method to determine the winner of the game.
"""
class Game:
    def __init__(self): 
        # Initializes the game with the computer's and user's choices unset, and the result method unbound.

        self.computer_pick = self.computer_pick()
        self.user_pick = self.user_pick()
        self.get_result = self.get_result()

    def user_pick(self):
        """
        Prompts the user to input their choice (rock, paper, or scissors) until a valid input is given.

        Returns:
            str: The user's choice, either 'rock', 'paper', or 'scissors'.
        """
        while True:
                inputValue =  input("Enter rock/paper/scissors : ")
                inputValue = inputValue.lower()
                if inputValue in ["rock", "paper","scissors"]:
                    break
                else:
                    print("Invalid Input! Try again")

        return inputValue


    def computer_pick(self):
        random_value = random.randint(1, 3) 
        if random_value == 1:
            return "Rock"
        elif random_value == 2:
            return "Paper" 
        else: 
            return "Scissors"

    def get_result(self):
        if  (self.user_pick == self.computer_pick):
            result ="Game Draw"

        elif (self.user_pick == "rock" and self.computer_pick=="scissors") or (self.user_pick == "scissors" and self.computer_pick == "paper") or (self.user_pick == "paper" and self.computer_pick=='rock'):
            result = "You Win"

        else:
            result = "You Lose"

        return result

    def print_result(self):
        print(f"Computer's Pick - {self.computer_pick}")
        print(f"Your Pick - {self.user_pick}")
        print(self.get_result)


# created game object of Game class to access methods
game = Game()
game.print_result()  # called the method to ptint the results

