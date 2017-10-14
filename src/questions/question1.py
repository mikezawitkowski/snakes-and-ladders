#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
question1.py

Created on 2017-10-12
by Mike Zawitkowski
mike@acornanalytics.io

"""
from __future__ import division, print_function
import logging as log
from random import randint


def roll():
    return randint(1,6)


def play_a_game():
    positions = {'player1': 1,
                 'player2': 1}
    turns = {'player1': 0,
                'player2': 0}
    ladders = {
        3: 16,
        5: 7,
        15: 25,
        18: 20,
        21: 32
               }
    snakes = {
        12: 2,
        14: 11,
        17: 4,
        31: 19,
        35: 22
    }
    last_square = 36
    while max(positions.values()) < last_square:
        for player in sorted(positions.keys()):
            turns[player] += 1
            log.debug("%s plays turn %s" % (player, turns[player]))
            new_position = positions[player] + roll()
            if new_position in ladders.keys():
                new_position = ladders[new_position]
            if new_position in snakes.keys():
                new_position = snakes[new_position]
            positions[player] = new_position
            if new_position >= last_square:
                positions[player] = new_position
                break
    return positions, turns


def play_10k_games():
    winners = []

    for i in range(10000):
        positions, turns = play_a_game()
        log.debug(positions)
        log.debug(turns)
        player1 = positions['player1']
        player2 = positions['player2']
        if player1 > player2:
            winners.append('player1')
        else:
            winners.append('player2')

    return winners


def question1():
    winners = play_10k_games()
    assert len(winners) == 10000
    print("""\nQ1. In a two person game, what is the probability that the player who starts the game wins?\n""")
    msg = """A. Player1 won {:,} out of {:,} games, for a probability of {:.2f}. \n
    """
    player1_wins = winners.count('player1')
    total_games = len(winners)
    prob = player1_wins / total_games
    print(msg.format(player1_wins, total_games, prob))


def main():
    question1()


if __name__ == "__main__":
    log.basicConfig(level=log.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt="%b %d %H:%M:%S %Z")
    main()
