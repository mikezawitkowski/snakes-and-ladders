#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
question3_wrong.py

Created on 2017-10-12
by Mike Zawitkowski
mike@acornanalytics.io

"""
from __future__ import division, print_function
import logging as log
from random import randint
from util import roll


def play_a_game():
    positions = {'player1': 1,
                 'player2': 1}
    turns = {'player1': 1,  # note this is wrong
                'player2': 1}  # note this is wrong
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
    while max(positions.values()) < last_square:
        for player in sorted(positions.keys()):
            log.debug("%s plays turn %s" % (player, turns[player]))
            new_position = positions[player] + roll()
            roll_count += 1
            if new_position in ladders.keys():
                ladder_prob = randint(1,2) # new for q 3
                if ladder_prob == 1: # 50% chance you can take the ladder
                    new_position = ladders[new_position]
            if new_position in snakes.keys():
                new_position = snakes[new_position]
                snake_count += 1  # New for question 2
            positions[player] = new_position
            if new_position >= last_square:
                positions[player] = new_position
                break
            turns[player] += 1  # note this is wrong!
    game_stats = {'positions': positions,
                    'turns': turns,
                    'snake_count': snake_count,
                    'roll_count': roll_count}
    return game_stats


def play_10k_games():
    # change winners to results so it can be re-used
    results = []
    for i in range(10000):
        game_stats = play_a_game()
        results.append(game_stats)
    # changed results to be a list of dictionaries for more flexibility
    # changed function to be more true to its name, not just a snake_counter
    return results


def question3():
    results = play_10k_games()
    rolls = sum([sum(result['turns'].values()) for result in results])
    sanity_check = sum([result['roll_count'] for result in results])
    # oops! After using the sum of the result of turns I realized my error.
    # I initialized player positions at 1 and that messed up the counting.
    # Also my use of the `break` statement came too early!
    if log.getLogger().getEffectiveLevel() <= 20: # INFO or DEBUG
        # import pdb; pdb.set_trace()
        assert (rolls == sanity_check)
    total_games = len(results)
    answer = rolls / total_games


    msg = ("\nQ3. If each time a player landed on a ladder and there was " +
            "only a 50% chance they could take it, what is the average " +
            "number of rolls needed to complete a game?\n")
    print(msg)

    msg = ("A. OOPS! I made a mistake here, because I summed the turns, " +
        "but the turns are miscounted. Thankfully I wrote a little sanity " +
        "checker and found my error. The sum of player turns gives you {:,} " +
        "but adding an explicit counter for the triggering of the roll()" +
        " function gives a result of {:,}. I'm leaving this file here with " +
        "errors for a record to 'show my work' but the corrected version " +
        "is in the `question3.py` script. Note that retroactively I also" +
        "changed code in questions 1 and 2 so that turns is incremented" +
        "as the first step instead of the last one after the break." +
        " Also the start value for each player turn changed from 1 to 0.")

    # msg = "\nA. On average, a snake was landed on {:.2f} times per game.\n"
    print(msg.format(rolls, sanity_check))
    #
    # msg = "\n{:,} games played, {:,} rolls of the dice.\n"
    # log.info(msg.format(total_games, rolls))


def main():
    question3()


if __name__ == "__main__":
    log.basicConfig(level=log.WARN,
                    format='%(asctime)s %(message)s',
                    datefmt="%b %d %H:%M:%S %Z")
    main()
