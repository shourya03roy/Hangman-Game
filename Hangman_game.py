import random
s1 = "---------"
s2 = "|     O"
s3 = "|    /|\\"
s4 = "|    / \\" 
s5 = "----"
def printhangman(guessno):
    if guessno == 1:
        print(s1,s2,s3[:-3],s4[:-3],s5,sep="\n")
    if guessno == 2:
        print(s1,s2,s3[:-2],s4[:-3],s5,sep="\n")
    if guessno == 3:
        print(s1,s2,s3[:-1],s4[:-3],s5,sep="\n")
    if guessno == 4:
        print(s1,s2,s3,s4[:-3],s5,sep="\n")
    if guessno == 5:
        print(s1,s2,s3,s4[:-2],s5,sep="\n")
    if guessno == 6:
        print(s1,s2,s3,s4,s5,sep="\n")
def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon']
    return random.choice(words)
word = choose_word()
guessed = ["_"]*len(word)
guessno = 0
print("Welcome to Hangman Game")
while guessno != 6 :
    print(" ".join(guessed))
    guess = input("Enter guess letter: ")
    if guess in word:
        if guess in guessed:
            print("Already guessed")
            continue
        print("Your guess is right")
        for j in range(0,len(word)):
            if word[j] == guess:
                guessed[j] = guess
    else:
        print("Your guess is wrong")
        guessno += 1
        printhangman(guessno)
    if "".join(guessed) == word:
        print("You won")
        break
    print("\n")
if guessno == 6:
    print("You lost. Correct word was: ",word)
    
