# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. You will practice string manipulation, loops, conditionals, and random selection to create an interactive Hangman game.

## 📝 Tasks

### 🛠️	Set Up the Game

#### Description
Create the foundation for the Hangman game by defining a list of words and randomly selecting one for the player to guess. Initialize the game state including the hidden word display and attempt counter.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of words
- Display the hidden word as underscores (e.g., `_ _ _`) at the start of the game
- Set a maximum number of incorrect guesses allowed

### 🛠️	Implement the Game Loop

#### Description
Build the main game loop that accepts letter guesses from the player, updates the game state, and determines when the game ends.

#### Requirements
Completed program should:

- Accept single-letter guesses from the user as input
- Reveal correctly guessed letters in the hidden word display
- Track and display the number of incorrect guesses remaining
- End the game when the word is fully guessed or attempts are exhausted
- Display a win or lose message when the game ends
