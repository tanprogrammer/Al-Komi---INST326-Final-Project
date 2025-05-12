# Al-Komi Card Game

## Overview
Al-Komi is a digital Python-based implementation of a traditional Egyptian card game, redesigned for one human player versus a computer. Players take turns placing cards on the table, attempting to match card values and capture cards. The game ends when the deck is finishes or when the first player to reach 70 points wins.

## Files in Repository

- **README.md**: This file explains what the project is about, how to set it up, and how to run it. It gives background on the program and is meant to help anyone who wants to use or contribute to the code. It also has our sources and attributions
- **AlKomi-Final-Script.py**: This is the main Python file where all the actual code lives. It has everything needed for the program to work—like the game logic, how the players behave, how the deck is handled, and how everything runs together.

##  How to Run this Program 
This program takes one command line argument, your name (single player only). Open the terminal and run the follwing: 

_python3 AlKomi-Final-Script.py {insert name}_

## How to use this program
**How to Play**
* You will see your hand 
* You’ll be prompted to choose a card from your hand (has to match the numbers on your hand; **case sensitive**)
* The computer will take its turn automatically.
* The game continues until the deck is empty and a winner is declared.
* Table cards, current scores, and your hand are displayed clearly every round.
* If your hand becomes empty and the deck still has cards, you will be re-dealt automatically.

## How to interpret the terminal output 
Background work in the script: When you play a turn, your card is first added to the table, then the computer takes a turn and their play is evaulated. After that the table is updated again for you to play again and those are the cards you see on the table after the computer's turn. If we had more time we wanted to work on printing this process to the terminal so the palyers have a clear idea of whats going on. 

## Anotated Biblography 
EgyBasra – https://www.egybasra.com/

__This website was used to understand the official rules, structure, and gameplay of the traditional Egyptian card game Basra (also known as Al-Komi). It helped us accurately implement the core mechanics, special card rules (like the 7 of Diamonds as a wildcard), scoring system, and general flow of the game in our Python version.__ 

## Attributions 
| **Method/Function**           | **Primary Author**    | **Techniques Demonstrated**              |
|---------------------------|-------------------|--------------------------------------|
| Deck.shuffle_deck()             | Colette Rouiller       | Use of standard library(random.shuffle)                       |
| deal_cards()           | Colette Rouiller    | Sequence unpacking |
| match()            | Jeffrey Tan  |  Set operations     |
|refill          |    Leighwith   | Comprehensions or generator Expressions (list comprenshion)       |
| evaluate_play()             | Micheas       | f-strings contianing expressions                       |
| Gamestate.__str__         | Micheas   | magic method |
| parse_args            | Leighwith  |  ArgumentParser class    |
|          |       |     |
|          |       |     |
|          |       |     |
|          |       |     |
|          |       |     |
|          |       |     |
|          |       |     |
|          |       |     |
