#!/usr/bin/env python3
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
from enum import Enum

"""The Player class is the parent class for all of the Players
in this game"""


class Move(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'

    @classmethod
    def moves(cls):
        return [move.value for move in cls]


class Player:
    my_move = random.choice(Move.moves())
    their_move = random.choice(Move.moves())

    def __init__(self):
        self.score = 0

    def move(self):
        return Move.ROCK.value

    def learn(self, my_move, their_move):
        pass

    def win_round(self):
        self.score += 1

    def beats(one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class AllRockPlayer(Player):
    def move(self):
        return Move.ROCK.value


class RandomPlayer(Player):
    def move(self):
        return random.choice(Move.moves())


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("rock, paper, or scissors? > ").lower()
            if move in Move.moves():
                return move
            else:
                print(f"The move {move} is not valid. Try again.")


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(Move.moves())
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(Move.moves())
        else:
            index = Move.moves().index(self.my_move)
            return Move.moves()[(index + 1) % len(Move.moves())]

    def learn(self, my_move, their_move):
        self.my_move = my_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.current_round = 0

    def play_round(self):

        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1} *** Player 2: {move2}")
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
        for round in range(3):
            print(f"\nRound: {round + 1}:-")
            self.play_round()
            print(f"Score: Player1:{self.p1.score} Vs Player2:{self.p2.score}")
        print(f"Final score: {self.p1.score} to {self.p2.score}")
        print("Game over!")


if __name__ == '__main__':
    print("\nRock Paper Scissors, Go!\n")
    opponents = {
        '1': AllRockPlayer(),
        '2': RandomPlayer(),
        '3': ReflectPlayer(),
        '4': CyclePlayer(),
        '5': HumanPlayer()
    }
    print("Players to choose:-")
    for key, value in opponents.items():
        print(f"{key}: {value.__class__.__name__}")
    print("\n")
    p1 = opponents[input("Choose player1 -> ")]
    p2 = opponents[input("Choose player2 -> ")]
    game = Game(p1, p2)
    game.play_game()
