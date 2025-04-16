# Flashy - French Word Learning Flashcard App

## Description

Flashy is a simple desktop application built with Python and Tkinter designed to help users learn French vocabulary. It presents flashcards with French words, allowing users to test their knowledge and track their progress. Words the user indicates they know are removed from the learning pool, focusing study efforts on words that still need practice.

![Flashy Screenshot]("Language-Learning-Flashcard-App/images/Screenshot-flashcard.png")

## Features

*   Displays French words on the front of a flashcard.
*   Reveals the English translation on the back after a 3-second delay.
*   Users can mark words as "known" (green checkmark button) or "unknown" (red X button).
*   Known words are removed from the current session's learning list.
*   Progress is saved: words marked as known are stored in `data/words_to_learn.csv`, so the app remembers which words you still need to learn across sessions.
*   If `data/words_to_learn.csv` doesn't exist (e.g., on the first run or after learning all words), it starts fresh with the full list from `data/french_words.csv`.
*   Displays a completion message when all words in the list have been marked as known.

## Requirements

*   Python 3.x
*   Pandas library
*   Tkinter library (usually included with standard Python installations)

## Setup and Installation

1.  **Clone or download the project:** Get the project files onto your local machine.
2.  **Navigate to the project directory:** Open your terminal or command prompt and change into the `flash-card-project-start` directory.
    ```bash
    cd path/to/flash-card-project-start
    ```
3.  **Install dependencies:** The project requires the Pandas library. You can install it using pip:
    ```bash
    pip install pandas
    ```
    *(Note: Tkinter is typically included with Python. If you encounter issues, you might need to install it separately depending on your OS and Python distribution, e.g., `sudo apt-get install python3-tk` on Debian/Ubuntu).*

## Usage

1.  Make sure you are in the project's root directory (`flash-card-project-start`) in your terminal.
2.  Run the main application script:
    ```bash
    python main.py
    ```
3.  The application window will appear:
    *   A French word is displayed.
    *   After 3 seconds, the card flips to show the English translation.
    *   Click the **red X button** if you didn't know the word. A new word will be shown.
    *   Click the **green checkmark button** if you knew the word. The word will be removed from your list of words to learn for future sessions, and a new word will be shown.
4.  The application saves your progress by updating the `data/words_to_learn.csv` file each time you mark a word as known.
5.  When you have learned all the words, a completion message will be displayed. To restart with the full list, you can delete the `data/words_to_learn.csv` file.



