# Hangman Game in Python

## Features
- Random word selection from predefined categories:
  - European countries
  - European capitals
  - American countries
  - American capitals
  - Animal names
  - Common names
  - League of Legends champions
  - Electronics-related terms
- ASCII-based hangman visuals that change based on incorrect guesses.
- Input validation to prevent special characters, numbers, and repeated letters.
- Dynamic display of guessed letters and remaining attempts.
- Option to restart or exit the game after completion.

## How to Play
1. Run the Python script.
2. Select a category.
3. Try to guess the word by entering one letter at a time.
4. If the guessed letter is correct, it will be revealed in the word.
5. If the guessed letter is incorrect, the number of attempts decreases, and a part of the hangman drawing is added.
6. The game ends when:
   - The player correctly guesses the word.
   - The player runs out of attempts, revealing the correct word.
7. The player can choose to play again or exit the game.

## Example Gameplay

Welcome to Hangman!  
Choose a category:  
▶ European countries  
▶ American capitals  
▶ Animal names  
...  
  
You have 6 attempts remaining.  
Word: _ _ _ _ _  
Enter a letter: ➜ a  
✔ Correct!   
Word: A _ _ _ A  
  
Enter a letter: ➜ z  
✖ Incorrect!   
Attempts remaining: 5  

## Future Improvements

1. Add more word categories.
2. Implement a graphical user interface (GUI).
3. Allow multiplayer mode.
