# README

This repo is a little exercise created as a snakes and ladders example, answering some questions.

## Requirements

 - python2.7
 - a command line application (like terminal on linux or OSX)

### Getting Started

  - Download this to your local machine
  - From the root directory Run `./src/snakes.py` from the command line
  - Answers will print to standard output on the command line (For your benefit answers from a recent run are below)


### Sample output

Running `./src/snakes.py` will produce output that resembles the following:

```
Q1. In a two person game, what is the probability that the player who starts the game wins?

A. Player 1 demonstrated a 0.52 probability of winning, having won 5,171 out of 10,000 games.

Q2. On average, how many snakes are landed on in each game?

A. On average, a snake was landed on 3.11 times per game.


Q3. If each time a player landed on a ladder and there was only a 50% chance they could take it, what is the average number of rolls needed to complete a game?

A. Under these conditions an average of 22.40 rolls are needed to complete the game.


Q4. Starting with the base game, you decide you want the game to have approximately fair odds. You do this by changing the square that Player 2 starts on. Which square for Player 2's start position give the closest to equal odds for both players?

A. Under these conditions the best square for player2 to start is square 7.

Q5. In a different attempt to change the odds of the game, instead of staring Player 2 on a different square, you decide to give Player 2 immunity to the first snake that they land on. What is the approximate probability that Player 1 wins now?

A. Under these conditions Player 2 has a 0.61 probability of winning.
```


### About the Files

Below is a breakdown of what the files
```
.
├── README.md : this file here, in markdown for you to understand the project
├── all.py - old method, typing `./all.py` runs correct question.py file
├── question1.py
├── question2.py
├── question3.py
├── question3_wrong.py - record of an error that was fixed (ignored by all.py)
├── question4.py
├── question5.py
└── snakes.py  - FINAL VERSION, refactored. Run `./snakes.py` in a terminal
```


To run these files simply execute `./all.py` on a computer that has python2.7 installed.

Each question has been answered in the file with the right filename.

There was a mistake made partway through question3, and that wrong path is documented in `question3_wrong.py`. Running `./all.py` doesn't run this file.


## Refactored `snakes.py`

The code for this project had a "bad code smell." After writing the code for the questions as functions in individual scripts, we de-duplicated the code.


## Advanced evaluation

Each file will run by itself, for instance `./src/question1.py` runs the original work done to answer question 1. A small amount of that was changed when refactored into `snakes.py` but it still works fine.

You have the option of entering debug mode with any file. Open up the file in any text editor and at the very end you'll notice code that looks like this:

```
log.basicConfig(level=log.WARN,
                format='%(asctime)s %(message)s',
                datefmt="%b %d %H:%M:%S %Z")

```

Change the log level from `log.WARN` to `log.INFO` to get more detailed text printing to stdout. For the most detailed logs to analyze, you can enter debug mode by changing that line to `log.DEBUG`.



## Future Improvements

There's still a little bit of a bad code smell in this project. Even if nothing else was changed regarding its purpose (answering the five questions), here are a few areas worth improving:

- The speed at which these are calculated is sub-optimal. Current speed is 55 seconds. Add a timer decorator to evaluate performance, then try and make this faster.
- Add a graphical interface
- Deploy this project onto a VSP server (e.g. Ubuntu running on a Linux node) and giving it a web interface
- Removing the assertions, which don't really belong in production. At the very least wrapping it in code that detects the log level, and if it's in debug mode, applies them.
- For some questions the debug mode prints a TON of text to stdout that is very expensive. Debug should be a little better at those sort of things.
- The use of string formatting with percent vs `format()` is inconsistent.
- Cleaning up the log levels so it's clear what you are getting, all the way up to WARN or CRITICAL.
- Adding a couple more tests so if the numbers don't check out it raises an Error message.
- There are some aspects of each question method that is duplicated. It could be handled as an additional entry to the results dictionary once, and be done for all questions.


## Questions? Feedback?

Email mike at acornanalytics dot io or call Mike at 925-388-NUTS.
