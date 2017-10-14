#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
question4.py

Created on 2017-10-12
by Mike Zawitkowski
mike@acornanalytics.io

"""
from __future__ import division, print_function
import logging as log
from random import random, randint


def roll():
    return randint(1,6)


def play_a_game(ladder_threshold=0, player2_start_position=1):

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
                new_position = snakes[new_position]
                snake_count += 1  # New for question 2
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


def play_10k_games(ladder_threshold=0, player2_start_position=1):
    # change winners to results so it can be re-used
    results = []
    for i in range(10000):
        game_stats = play_a_game(ladder_threshold=ladder_threshold,
                            player2_start_position=player2_start_position)
        results.append(game_stats)
    # changed results to be a list of dictionaries for more flexibility
    # changed function to be more true to its name, not just a snake_counter
    return results


def question3():
    results = play_10k_games(ladder_threshold=0.5)
    rolls = sum([sum(result['turns'].values()) for result in results])
    sanity_check = sum([result['roll_count'] for result in results])

    # oops! After using the sum of the result of turns I realized my error.
    # I initialized player positions at 1 and that messed up the counting.
    # Also my use of the `break` statement came too early!

    if log.getLogger().getEffectiveLevel() <= 10: # DEBUG
        import pdb; pdb.set_trace()

    if log.getLogger().getEffectiveLevel() <= 20: # INFO or DEBUG
        assert (rolls == sanity_check)
        log.debug("assertion passed!")

    total_games = len(results)
    answer = rolls / total_games

    msg = ("\nQ3. If each time a player landed on a ladder and there was " +
            "only a 50% chance they could take it, what is the average " +
            "number of rolls needed to complete a game?\n")
    print(msg)

    msg = ("\nA. Under these conditions an average of {:.2f} rolls are " +
            "needed to complete the game.\n")
    print(msg.format(answer))

    msg = "\n{:,} games played, {:,} rolls of the dice.\n"
    log.info(msg.format(total_games, rolls))


def question4():
    # all the possible starting squares for player2
    start_options = range(1,36)

    player2_chances = {}
    for start in start_options:
        results = play_10k_games(ladder_threshold=0.0,
                                    player2_start_position=start)
        log.debug("start: %s" % start)
        winners = []
        for result in results:
            winners.append(result['winner'])
        msg = "{:,} games played, player1 won {:,} times, player2 won {:,} times"
        log.debug(msg.format(len(winners), winners.count('player1'),
                winners.count('player2')))

        player2_prob = winners.count('player2') / len(winners)
        log.debug("player2 probability: {:.2f}".format(player2_prob))
        player2_chances[start] = player2_prob

    half = min(player2_chances.values(), key=lambda v: abs(v-0.5))
    answer = player2_chances.keys()[player2_chances.values().index(half)]
    # print(answer)

    msg = ("\nQ4. Starting with the base game, you decide you want the game " +
            "to have approximately fair odds. You do this by changing the " +
            "square that Player 2 starts on. Which square for Player 2's " +
            "start position give the closest to equal odds for both players?\n")
    print(msg)

    msg = ("\nA. Under these conditions the best square for player2 to start " +
            "is square %s.\n")
    print(msg % answer)


def main():
    question4()


if __name__ == "__main__":
    log.basicConfig(level=log.WARN,
                    format='%(asctime)s %(message)s',
                    datefmt="%b %d %H:%M:%S %Z")
    main()
