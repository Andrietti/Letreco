import random

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[1;33m"
WINNER = "\033[0;42m"

words_list = open("dicio.txt" , "r", encoding="utf-8").readlines()


def randomword():
    global word
    word = random.choice(words_list).strip("\n")
    print(word)

dic = {}
def game():
    for i in range(5):

        player_word = input("Type here your guess: ")

        while len(player_word) < 5:
            print("Please, just words than have 5 leterrs")
            player_word = input("Tente novamente:  ")

        for letra in player_word:
            dic[letra] = 0

        for i in range(5):

            

            if word[i] == player_word [i] and dic[player_word[i]] <= word.count(word[i]):
                print(GREEN + player_word[i] + RESET, end="")
                dic[player_word[i]] += 1

            elif player_word[i] in word and dic[player_word[i]] <= word.count(word[i]):
                print(YELLOW + player_word[i] + RESET , end="")
                dic [player_word[i]] += 1
            else:
                print(RED + player_word[i] + RESET , end="" )
            
        if player_word == word:
            print("")
            print(WINNER + "WINNER" + RESET)
            break

    

randomword()

game()