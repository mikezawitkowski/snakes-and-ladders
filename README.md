snakes_and_ladders
==============================

A short description of the project.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

TODO: walk them through the acuna matata case study. Call them Acme, or better yet. Orange You Gonna By Our Product Inc.

"Orange You Gonna By Our Product Inc." is a special platform geared toward sales teams. They had a proprietary way of presenting information to sales teams "using data science." In fact, OYGBOP Inc. just received $100 M in funding to build out a data science team, and go get customers.

A friend of OYGBOP Inc. who was also a friend of my company, Acorn Analytics, said, "Stop everything!" Before you waste time and money finding, recruiting, training and retaining an entire data science team, which by the way was going to cost a lot of money and may be impossible given the current demand for data scientists, let's explore. My friend, who we'll call Zed, was an experienced data scientist himself, and decided we would team up and consult for this client together.

This was  difficult setup, politically. Zed had a relationship with J, the CEO, and was technically an advisor.

From a technical point of view, the stack looked like this:
- salesforce to google cloud, pulled rarely, like once every six months at most
- google cloud namely google SQL


The end result:
- The client didn't spend most of its millions of dollars on data scientists. It was clear that they needed more data.
- Despite the lack of data, they got more value than they anticipated


Where we would go from here:
- the clients were deleting the data

Lessons Learned:
- too much shielding between J the CEO, when we should have had contact with the client immediately
- next time we look at the implementation instead
- they were not agile, and we should have forced them to be more, to incorporate developments earlier instead of sitting on accumulated technical debt
- it would be nice to see this in production to see how well it is performing and predicting events

***

Second case study is an IOT company that lost the ability to do any analysis. So we got called in and for the cost of a single hire, we provided a team of people.




# The Background

Outstanding, lets confirm Tuesday 10/17 from 10am till about 5pm,

Additional details below,

Dress: Business Casual

The Formal Interview is usually a day long onsite visit where you have approx. 6 one-on-one conversations with senior and junior people in the firm, to help you get a sense of “an average day in our life”.

The interviewer is looking to see how you model a problem at this stage. The interviewer may walk you through a simplified consulting problem from a previous client and see you how set up the initial solution and address the clients pressing issues.

Alternatively, they may like to talk about a previous engagement or project from your resume that is similar to our work and push the boundaries of the problem. None of the material in the interview will be foreign to you, but will come from your relevant experience or one of our recent projects that we will walk you through. ​ A significant component of the interview is to learn about you and your background and tell you about our firm's setup. ​

In addition to this, the entire firm sits in a 1-hour Case presentation. You can go over the details of one major or two smaller projects that you worked on during this presentation. The typical length of this presentation is 45 minutes + time for questions. Most presenters will use powerpoint.

For the case presentation, a balanced approach is key – you should communicate your technical solution with sufficient depth while at the same time explaining the high-level impact and insights from your work. The audience is skewed to the technical side and will appreciate strong modeling capabilities, but the presentation shouldn’t only be math formulation. If needed, make up sanitized/simulated data from what you can remember from your project: the key point is to demonstrate your thinking and communicate the trends, insights and important outputs of the analysis.

Part of our interview process also includes a take home simulation exercise.

The purpose is to understand your coding/technical background. To help with that, we are attaching a simple simulation exercise.

You may use any programming language or tools you want to complete the exercise, but make sure to show all of your work. Please send it to me one day prior to your onsite interview.
Please feel free to reach out to me if you have any questions or constraints with completing the exercise.

One of the interviewers will review your exercise with you during your on-site interview.

# The Challenge

You and your friend are playing your old Snakes and Ladders board game. Each player begins on square 1 and takes turns rolling a fair 6-sided die. The player moves the number of spaces indicated on the die. If you land at the bottom of a ladder, you automatically move to the square at the top of the ladder. Conversely, if you land on a snake head, then you fall to the square at the snake's tail. The winner is the first person to make it onto or past the last square.

Being interested in analytics, you decide to run simulations of 10,000 games to understand your odds of winning under different scenarios. Consider each scenario independent of the other scenarios.

Please answer the following questions using any means available. We would like you to keep a record of your work and walk us through your solution. We are primarily interested in your approach and code, rather than the final answers.

Ladders 3 --> 16 5 --> 7 15 --> 25 18 --> 20 21 --> 32
Snakes 12 --> 2 14 --> 11 17 --> 4 31 --> 19 35 --> 22


## Question 1

In a two person game, what is the probability that the player who starts the game wins?

## Question 2
On average, how many snakes are landed on in each game?

## Question 3
If each time a player landed on a ladder and there was only a 50% chance they could take it, what is the average number of rolls needed to complete a game?

## Question 4
Starting with the base game, you decide you want the game to have approximately fair odds. You do this by changing the square that Player 2 starts on. Which square for Player 2’s start position gives the closest to equal odds for both players?

## Question 5
In a different attempt to change the odds of the game, instead of starting Player 2 on a different square, you decide to give Player 2 immunity to the first snake that they land on. What is the approximate probability that Player 1 wins now?



<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
