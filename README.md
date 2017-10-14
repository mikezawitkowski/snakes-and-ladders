# README

This repo is a little exercise created as a snakes and ladders example, answering some questions.

## Requirements

 - python2.7
 - a command line application (like terminal on linux or OSX)

### Getting Started

  - Run `./snakes.py` from the command line

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
