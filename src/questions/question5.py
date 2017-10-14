#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
question5.py

Created on 2017-10-12
by Mike Zawitkowski
mike@acornanalytics.io
"""
from __future__ import division, print_function
import logging as log
from random import random, randint


def roll():
    return randint(1,6)


def play_a_game(ladder_threshold=0, player2_start_position=1,
                first_snake_immunity=False):

    # positions = {'player1': 1,
    #              'player2': 1}
    positions = {'player1': 1}
    # added for question 4
    positions['player2'] = player2_start_position

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
    roll_count = 0  # a double-check
    snake_count = 0  # new for question 2
    last_square = 36
    first_snake_p2 = True
    while max(positions.values()) < last_square:
        for player in sorted(positions.keys()):
            turns[player] += 1
            log.debug("%s plays turn %s" % (player, turns[player]))
            new_position = positions[player] + roll()
            roll_count += 1
            if new_position in ladders.keys():
                ladder_prob = random() # new for q 3
                if ladder_prob >= ladder_threshold: # 50% chance to take ladder
                    new_position = ladders[new_position]

            if new_position in snakes.keys():
                snake_count += 1  # New for question 2
                # add this conditional for question 5
                if (first_snake_p2 and first_snake_immunity and
                    player == 'player2'):
                    first_snake_p2 = False # skips the snake penalty first time
                else:
                    new_position = snakes[new_position]
            positions[player] = new_position
            if new_position >= last_square:
                positions[player] = new_position
                winner = player
                break
    game_stats = {'positions': positions,
                    'turns': turns,
                    'snake_count': snake_count,
                    'roll_count': roll_count,
                    'winner': winner}
    return game_stats


def play_10k_games(ladder_threshold=0, player2_start_position=1, first_snake_immunity=False):
    # change winners to results so it can be re-used
    results = []
    for i in range(10000):
        game_stats = play_a_game(ladder_threshold=ladder_threshold,
                            player2_start_position=player2_start_position,
                            first_snake_immunity=first_snake_immunity)
        results.append(game_stats)
    # changed results to be a list of dictionaries for more flexibility
    # changed function to be more true to its name, not just a snake_counter
    return results


def question5():
    results = play_10k_games(ladder_threshold=0.0, first_snake_immunity=True)

    winners = []
    for result in results:
        winners.append(result['winner'])
    msg = "{:,} games played, player1 won {:,} times, player2 won {:,} times"
    print(msg.format(len(winners), winners.count('player1'),
            winners.count('player2')))

    player1_prob = winners.count('player1') / len(winners)
    print("player1 probability: {:.2f}".format(player1_prob))

    player2_prob = winners.count('player2') / len(winners)
    print("player2 probability: {:.2f}".format(player2_prob))


def main():
    question5()

if __name__ == "__main__":
    log.basicConfig(level=log.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt="%b %d %H:%M:%S %Z")
    main()
