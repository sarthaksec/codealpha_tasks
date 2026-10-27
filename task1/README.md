# Task 1: Hangman Game (CodeAlpha Internship)

## 📌 Project Overview
A text-based console implementation of the classic **Hangman** word guessing game in Python. The computer selects a random secret word from a predefined list, and the player tries to guess the word by proposing letters one by one within a maximum of 6 incorrect attempts.

---

## 🎯 Task Requirements & Features
- **Predefined Word List:** 5 curated programming-related words (`PYTHON`, `DEVELOPER`, `HANGMAN`, `CODEALPHA`, `PROGRAMMING`).
- **Attempt Limit:** Strict 6 incorrect guess limit with real-time ASCII hangman progression.
- **Input Validation:**
  - Enforces single character input.
  - Rejects non-alphabetic characters.
  - Warns about duplicate guesses without penalizing attempts.
- **Real-Time Visuals:**
  - Masked word display (e.g., `_ _ T _ _ _`).
  - History of incorrect guesses.
  - Detailed ASCII gallows art updated dynamically at each stage.
- **Game Replay:** Prompt to replay upon winning or losing.

---

## 🛠️ Concepts Used
- **`random` module:** `random.choice()` for secret word selection.
- **Data Structures:** Lists for incorrect guesses and ASCII gallows, Sets for efficient duplicate check and win-condition verification.
- **Loops & Control Flow:** `while` loop for game execution, `if-elif-else` branches for game rules and input handling.
- **String Manipulation:** Uppercasing, joining, string splitting, and masked display generation.

---

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to this directory:
   ```bash
   cd Task1_Hangman_Game
   ```
3. Run the script:
   ```bash
   python hangman.py
   ```

---

## 📸 Sample Gameplay Preview

```text
=============================================
      WELCOME TO CODEALPHA HANGMAN GAME      
=============================================
I have picked a secret word with 6 letters.
You have 6 incorrect attempts before game over.


       +---+
       |   |
           |
           |
           |
           |
    =========
    
Incorrect guesses (0/6): None

Word: _ _ _ _ _ _
----------------------------------------
Enter a letter: p

[+] Good guess! 'P' is in the word.

       +---+
       |   |
           |
           |
           |
           |
    =========
    
Incorrect guesses (0/6): None

Word: P _ _ _ _ _
----------------------------------------
Enter a letter: z

[-] Sorry, 'Z' is NOT in the word. (Remaining attempts: 5)

       +---+
       |   |
       O   |
           |
           |
           |
    =========
    
Incorrect guesses (1/6): Z

Word: P _ _ _ _ _
----------------------------------------
```
