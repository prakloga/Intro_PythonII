#!/usr/bin/env python3
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass

    def win_round(self):
        self.score += 1

    def beats(one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        move = random.choice(moves)
        return move


class HumanPlayer(Player):
    def move(self):
        move = input("rock, paper, or scissors? > ").lower()
        while move not in moves:
            print("Sorry, try again.")
            move = input("rock, paper, or scissors? > ").lower()
        return move


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_move = None

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            if self.my_move == 'rock':
                return 'paper'
            elif self.my_move == 'paper':
                return 'scissors'
            else:
                return 'rock'


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.current_round = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.decide_round(move1, move2)
        self.current_round += 1

    def decide_round(self, move1, move2):
        if Player.beats(move1, move2):
            print("Player 1 wins this round!")
            self.p1.win_round()
        elif Player.beats(move2, move1):
            print("Player 2 wins this round!")
            self.p2.win_round()
        else:
            print("It's a tie!")

    def play_game(self):
        print("Rock Paper Scissors, Go!")
        for round in range(3):
            print(f"\nRound: {round + 1}:-")
            self.play_round()
            print(f"Score: Human: {self.p1.score} Vs Comp: {self.p2.score}")
        print(f"Final score: {self.p1.score} to {self.p2.score}")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
