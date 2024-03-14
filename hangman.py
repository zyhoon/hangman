import random

def hangman(word):
    wrong = 0
    stages = ["",
              "____________            ",
              "|          |            ",
              "|          |            ",
              "|          0            ",
              "|         /|\           ",
              "|         / \           "
              ]
    letters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")
    while wrong < (len(stages) - 1):
        print(" ".join(board) + "\n")
        char = input("Guess a letter: ")
        if char not in letters:
            wrong += 1
            print("\nWrong guess\n")
            print(" ".join(board))
            e = wrong + 1
            print("\n".join(stages[0:e]) + "\n")
        while char in letters:
            location = letters.index(char)
            board[location] = char
            letters[location] = "$"
            e = wrong + 1
            print("\n".join(stages[0:e]) + "\n")
        if "_" not in board:
            print("You win! " + "The word is {}.".format(word))
            win = True
            break
    if not win:
        print("\n".join(stages[0:(wrong +1)]))
        print("\nYou lose! " + "The word is {}.".format(word))

wlist = ["gracious",
         "metaphor",
         "watermelon",
         "tiger",
         "vehicle",
         "statistic",
         "paradox"
         ]
number = random.randint(0,6)
word = wlist[number]
hangman(word)



        
