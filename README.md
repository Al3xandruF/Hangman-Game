# **Hangman Game**

The **Hangman Game** is a Python based terminal game, which runs in Code Institute mock terminal on Heroku.

In this version, the computer auto-generates a word from the library in which the user will have to guess before waisting all available tries which will result in losing the game.

[Hangman Game - Live Version](https://hangman-game-p3-python.herokuapp.com/)

![responsive](/assets/screenshots/responsive.png)

## **Contents**

- How to play
- Features:
  - Existing Features
  - Future Features
- Modules/ Functions/ Methods
- Testing
- Validator Testing
- Deployment
- Credits

### **How to play**
---

This Python terminal version of **Hangman** is based on the classic pen-and-paper game ([Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game))).  

In this instance, **Hangman Game** is a guessing game between the computer and the user.  

The computer will generate a word in which the user will have to guess by suggesting letters within 6 guesses.  

### **Features**
---

**Existing Features**

- Welcoming message.
- Hidden word which the user will have to guess.
- The 'incorrect letters' variable which will display all wrong letters chosen by the user throughout the game.
- The number of tries.
- The input where the user types the letters and triggers the game. 

![main_screen](/assets/screenshots/main_screen.png) 

- Accepts user input.
- Displays the incorrect letters.
- Shows the number of tries. 

![maine_screen1](/assets/screenshots/main_screen1.png)


- Input validation and error-checking:
  - Tells the user an incorrect letter has been chosen if numbers, words or other symbols are used to guess the hidden word.
  - You must enter only lower case letters.

![main_screen2](/assets/screenshots/main_screen2.png)

- When no tries are left, the user loses and the computer will show there are no tries left while displaying the hidden word.

![main_screen3](/assets/screenshots/main_screen3.png)

- If the player wins, the hidden word is displayed and the computer congratulates the user.

![main_screen4](/assets/screenshots/main_screen4.png)

### **Future Features**
---

- Will allow the user to choose the complexity of the game by:
  - Having options in how to play the game by guessing:
    - Single words
    - Short sentences
    - Names

### **Modules/ Functions/ Methods**
---

- Choice function from random module has been used to generate a word from the 'words' variable under the choose_word function.
- isalpha() method was used for the input to accept only alphabet letters (a-z).
- len() function was used for the chosen letter to be only one character.

### **Testing**
---

Manual Testing:

- Passed the code through PEP8 linter for no errors confirmation.
- Local terminal testing.
- Tested in the Code Institute Heroku terminal.
- Given W605 invalid escape sequence '\ '.

### **Deployment**
---
The project was deployed using Code Institute's mock terminal for Heroku.
- Steps for deployment:
  - Clone or Fork the repository.
  - Create a new heroku app.
  - Set the buildpacks to Python first and then NodeJS.
  - Link the Heroku app to the github repository.
  - Click on deploy.

### **Credits**
---

- Code Institute for the deployment terminal.
- Wikipedia for the Hangman Game details.
- [Chris Horton](https://gist.github.com/chrishorton) for the Hangman word bank.

