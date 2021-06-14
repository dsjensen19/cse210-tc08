# Batter
What's your batting average? Find out with this terminal version of the arcade 
classic. The goal is simple. Just bat the ball at the blricks until there are 
none left. If you miss the ball the game is over.

## Overview
Batter is a game in which the player seeks to bat the ball back towards the top of the screen to break the bricks. Miss the ball and its game over!

## Rules
Batter is played according to the following rules.

1. The bricks are arranged in 4 rows and 70 columns at the top of the screen.
2. The bat (or paddle) is positioned near the bottom of the screen.
3. The player can move the bat left or right within the boundaries of the screen.
4. The ball moves of its own accord, bouncing off the bat, bricks and walls.
If the bat misses the ball the game is over.

## Requirements
Your program must also meet the following requirements.

The program must use the Batter template.
The program must have a README file with assignment and author names.
The program must have at least ten classes.
Each module, class and method must have a corresponding comment using the style demonstrated in the solo checkpoint.

    -
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """
    -

The game must remain generally true to the order of play described in the rules.
## Suggestions
Make the game your own by enhancing it any way you like. A few ideas are as follows.

Enhanced feedback (score, etc).
Enhanced game play (more bats, balls or bricks).
Enhanced screens (splash, game over, etc).
Enhanced appearance (longer bat, bigger bricks, etc)

## Getting Started
---
Make sure you have Python 3.8.0 or newer and asciimatics 1.12.0 or new installed 
and running on your machine. You can install Asciimatics by opening a terminal 
and running the following command.
```
python3 -m pip install asciimatics
```
After you've installed the required libraries, open a terminal and browse to the 
project's root folder. Start the program by running the following command.
```
python3 batter 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the hunter folder and 
click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- batter              (source code for game)
  +-- game              (specific game classes)
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Asciimatics 1.12.0

## Authors
---
* # TODO: Add your names and emails here
