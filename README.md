# Al-Komi Card Game

## Overview
Al-Komi is a digital Python-based implementation of a traditional Egyptian card game, redesigned for one human player versus a computer. Players take turns placing cards on the table, attempting to match card values and capture cards. The game ends when the deck is finishes and the first player to reach 70 points wins.

## Files in Repository

- 

##  How to Run the Program 
From your terminal, navigate to the project folder and run:

_python3 Al_Komi.py_

**Note:**  __No command-line arguments are required.__

**How to Play**
* You will see your hand 
* You’ll be prompted to choose a card from your hand (has to match the numbers on your hand; case sensitive)
* The computer will take its turn automatically.
* The game continues until the deck is empty and a winner is declared.
* Table cards, current scores, and your hand are displayed clearly every round.
* If your hand becomes empty and the deck still has cards, you will be re-dealt automatically.

## Anotated Biblography 
EgyBasra – https://www.egybasra.com/

This website was used to understand the official rules, structure, and gameplay of the traditional Egyptian card game Basra (also known as Al-Komi). It helped us accurately implement the core mechanics, special card rules (like the 7 of Diamonds as a wildcard), scoring system, and general flow of the game in our Python version. 

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
