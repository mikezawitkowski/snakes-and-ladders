#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
question2.py

Created on 2017-10-12
by Mike Zawitkowski
mike@acornanalytics.io
"""
from __future__ import division, print_function
import logging as log
from random import randint


def roll():
    return randint(1,6)


def play_a_game(snake_count=0):
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
                snake_count += 1  # New for question 2
            positions[player] = new_position
            if new_position >= last_square:
                positions[player] = new_position
                break
    return positions, turns, snake_count


def play_10k_games():
    # change winners to results so it can be re-used
    results = []
    for i in range(10000):
        _, _, snake_count = play_a_game()
        results.append(snake_count)

    return results


def question2():
    msg = "\nQ2. On average, how many snakes are landed on in each game?\n"

    results = play_10k_games()
    snakes_count = sum(results)
    total_games = len(results)
    answer = snakes_count / total_games

    print(msg)

    msg = "\nA. On average, a snake was landed on {:.2f} times per game.\n"
    print(msg.format(answer))

    msg = "\n{:,} games played, {:,} snakes landed on.\n"
    log.info(msg.format(total_games, snakes_count))


def main():
    question2()


if __name__ == "__main__":
    log.basicConfig(level=log.WARN,
                    format='%(asctime)s %(message)s',
                    datefmt="%b %d %H:%M:%S %Z")
    main()
