# 🎮 Rock Paper Scissors Game

A simple and interactive **Rock Paper Scissors Game** built using **Python**.

The player competes against the computer by choosing Rock, Paper, or Scissors. The computer randomly selects its choice, and the winner is decided based on the standard Rock Paper Scissors rules.

## 🎯 Features

* 🪨 Rock
* 📄 Paper
* ✂️ Scissors
* 🤖 Computer makes a random choice
* 🏆 Automatically determines the winner
* 🤝 Detects a tie
* 🔄 Option to play multiple rounds
* ❌ Invalid choice handling
* 👋 Exit the game whenever you want

## 🛠️ Technologies Used

* **Python**
* `random` module
* `random.choice()`
* `while` loop
* `if-elif-else`
* User input
* f-strings
* String `.lower()` method

## 📂 Project Structure

```text
Rock-Paper-Scissors/
│
├── rock_paper_scissors.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### 2. Open the Project Folder

```bash
cd Rock-Paper-Scissors
```

### 3. Run the Python Program

```bash
python rock_paper_scissors.py
```

## 🎮 How to Play

When the game starts, you will see:

```text
========== Rock Paper Scissor Game ==========

1. Rock
2. Paper
3. Scissor
```

Enter your choice:

```text
Enter your Choice : 1
```

The computer will randomly choose Rock, Paper, or Scissors.

The game will then display:

```text
You chose : rock
Computer chose : scissor
You Wins !
```

After each round, you can choose whether to play again:

```text
Do you want to play again ? (yes/no) -->
```

Enter `yes` to continue or `no` to exit.

## 🏆 Game Rules

| Player Choice | Computer Choice | Result        |
| ------------- | --------------- | ------------- |
| Rock 🪨       | Scissors ✂️     | Player Wins   |
| Rock 🪨       | Paper 📄        | Computer Wins |
| Paper 📄      | Rock 🪨         | Player Wins   |
| Paper 📄      | Scissors ✂️     | Computer Wins |
| Scissors ✂️   | Paper 📄        | Player Wins   |
| Scissors ✂️   | Rock 🪨         | Computer Wins |
| Same Choice   | Same Choice     | Tie           |

## 🖥️ Example Output

```text
========== Rock Paper Scissor Game ==========

1. Rock
2. Paper
3. Scissor

Enter your Choice : 2

You chose : paper
Computer chose : rock
You Wins !

Do you want to play again ? (yes/no) --> yes

1. Rock
2. Paper
3. Scissor

Enter your Choice : 3

You chose : scissor
Computer chose : scissor
Match Tie

Do you want to play again ? (yes/no) --> no

Thanks for playing !!
```

## 📚 Python Concepts Practiced

This project helped practice:

* Variables
* `input()`
* `print()`
* Type conversion using `int()`
* `if-elif-else`
* `while` loops
* `break`
* Random number/choice generation
* `random.choice()`
* Strings
* f-strings
* `.lower()` method
* User interaction
* Basic game logic

## 🔮 Future Improvements

Possible improvements for the project:

* 🏆 Add a score system
* 📊 Display player vs computer score
* 🔢 Add a fixed number of rounds
* 🥇 Show the final winner
* 📈 Add win/loss statistics
* 🎨 Create a GUI using Tkinter
* 🔊 Add sound effects
* 🌐 Create a web version
* 💾 Save game history

## 👨‍💻 Author

**Virendra Singh Rathore**

B.Tech CSE | AI & Data Science

---

⭐ If you like this project, consider giving the repository a star!
