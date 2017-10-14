#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
snakes.py

Created on 2017-10-14
by Mike Zawitkowski
mike@acornanalytics.io
"""
from __future__ import division, print_function
import logging as log
from random import random, randint
from datetime import datetime
import os
import sys
import multiprocessing as mp


class Snakes(object):
    """
    Refactored the all.py into snakes.py.
    """
    def __init__(self):
        print("")  # give a little space in stdout
        self.ladders = {3: 16, 5: 7, 15: 25, 18: 20, 21: 32}
        self.snakes = {12: 2, 14: 11, 17: 4, 31: 19, 35: 22}
        self.last_square = 36
        self.default_results = self.play_10k_games()

    def roll(self):
        return randint(1,6)

    def play_a_game(self, ladder_threshold=0, player2_start_position=1,
                    first_snake_immunity=False):

        snake_count = 0
        roll_count = 0
        positions = {'player1': 1}
        positions['player2'] = player2_start_position  # added for question 4
        first_snake_p2 = True

        turns = {'player1': 0, 'player2': 0}
        while max(positions.values()) < self.last_square:
            for player in sorted(positions.keys()):
                turns[player] += 1
                log.debug("%s plays turn %s" % (player, turns[player]))
                new_position = positions[player] + self.roll()
                roll_count += 1
                if new_position in self.ladders.keys():
                    ladder_prob = random() # new for q 3
                    if ladder_prob >= ladder_threshold: # 50% chance take ladder
                        new_position = self.ladders[new_position]

                if new_position in self.snakes.keys():
                    snake_count += 1  # New for question 2
                    # added this conditional for question 5
                    if (first_snake_immunity and first_snake_p2 and
                        player == 'player2'):
                            first_snake_p2 = False
                    else:
                        new_position = self.snakes[new_position]
                positions[player] = new_position
                if new_position >= self.last_square:
                    positions[player] = new_position
                    winner = player
                    break
        game_stats = {'positions': positions,
                        'turns': turns,
                        'snake_count': snake_count,
                        'roll_count': roll_count,
                        'winner': winner}
        return game_stats

    def play_10k_games(self, ladder_threshold=0, player2_start_position=1,
                        first_snake_immunity=False):
        # change winners to results so it can be re-used
        results = []
        for i in range(10000):
            game_stats = self.play_a_game(ladder_threshold=ladder_threshold,
                                player2_start_position=player2_start_position,
                                first_snake_immunity=first_snake_immunity)
            results.append(game_stats)
        # changed results to be a list of dictionaries for more flexibility
        # changed function to be more true to its name, not just a snake_counter
        return results

    def question1(self):
        results = self.default_results
        winners = [result['winner'] for result in results]
        assert len(winners) == 10000
        print("""Q1. In a two person game, what is the probability that the player who starts the game wins?\n""")
        player2_wins = winners.count('player2')
        assert player2_wins > 0
        player1_wins = winners.count('player1')
        total_games = len(winners)
        prob = player1_wins / total_games
        msg = """A. Player 1 demonstrated a {:.2f} probability of winning, having won {:,} out of {:,} games.\n"""
        print(msg.format(prob, player1_wins, total_games))

    def question2(self):
        results = self.default_results
        snakes_count = sum([result['snake_count'] for result in results])
        total_games = len(results)
        answer = snakes_count / total_games

        msg = "Q2. On average, how many snakes are landed on in each game?\n"
        print(msg)

        msg = "A. On average, a snake was landed on {:.2f} times per game.\n"
        print(msg.format(answer))

        msg = "{:,} games played, {:,} snakes landed on.\n"
        log.debug(msg.format(total_games, snakes_count))

    def question3(self):
        results = self.play_10k_games(ladder_threshold=0.5)
        rolls = sum([sum(result['turns'].values()) for result in results])
        sanity_check = sum([result['roll_count'] for result in results])
        try:
            assert sanity_check == rolls
        except Exception as ex:
            log.exception(ex)
            import pdb; pdb.set_trace()
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

    def question4(self):
        # all the possible starting squares for player2
        start_options = range(1,36)

        player2_chances = {}
        for start in start_options:
            results = self.play_10k_games(ladder_threshold=0.0,
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

        msg = ("\nQ4. Starting with the base game, you decide you want the game " +
                "to have approximately fair odds. You do this by changing the " +
                "square that Player 2 starts on. Which square for Player 2's " +
                "start position give the closest to equal odds for both players?\n")
        print(msg)

        msg = ("\nA. Under these conditions the best square for player2 to start " +
                "is square %s.\n")
        print(msg % answer)

    def question5(self):
        msg = ("\nQ5. In a different attempot to change the odds of the " +
                "game, instead of staring Player 2 on a different square, " +
                "you decide to give Player 2 immunity to the first snake " +
                "that they land on. What is the approximate probability " +
                "that PLayer 1 wins now?")
        print(msg)

        results = self.play_10k_games(first_snake_immunity=True)
        winners = []
        for result in results:
            winners.append(result['winner'])
        msg = "{:,} games played, player1 won {:,} times, player2 won {:,} times"
        log.debug(msg.format(len(winners), winners.count('player1'),
                winners.count('player2')))

        player1_prob = winners.count('player1') / len(winners)
        log.debug("player1 probability: {:.2f}".format(player1_prob))
        player2_prob = winners.count('player2') / len(winners)
        log.debug("player2 probability: {:.2f}".format(player2_prob))

        msg = ("\nA. Under these conditions Player 2 has a {:.2f} " +
                "probability of winning.\n")
        print(msg.format(player2_prob))


def start_and_end_times(func):
    "Decorator that prints start, end, and total elapsed time values."
    def timer_function(*args, **kwargs):
        time1 = datetime.utcnow()
        msg = "Started timer at %s"
        log.info(msg % time1.replace(microsecond=0).isoformat())
        sys.stdout.flush()

        result = func(*args, **kwargs)

        time2 = datetime.utcnow()
        timed = time2 - time1
        msg = "Script completed at %s; Total time: %s"
        log.info(msg % (time2.replace(microsecond=0).isoformat(), timed))
        return result
    return timer_function


@start_and_end_times
def main():
    s = Snakes()
    s.question1()
    s.question2()
    s.question3()
    s.question4()
    s.question5()

if __name__ == "__main__":
    log.basicConfig(level=log.WARN,
                    format='%(asctime)s %(message)s',
                    datefmt="%b %d %H:%M:%S %Z")

    main()
