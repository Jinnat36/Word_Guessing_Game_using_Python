# Import the ramdom module here. 
import random
def random_choice():
    """This function choose random word from  below given list """
    words =['apple','banana','mango','orange','tree','red','white','black','pink','programing','programer','elephant','egg','duck','python','java','php','monday','facebook','whatpsapp']
    random_word=random.choice(words)
    return random_word
def guessing(x):
    """In this function ,User guess the random word ,which is already choosed by random module."""
    guesses=""
    chances=10
    while chances>0:
        wrong_g=0
        for char in x:
            if char in guesses:
                print(f"\033[1;31m {char}\033[0m",end=" ")
            else:
                wrong_g+=1 
                print("_",end=" ")
        if wrong_g==0:
            print("You Guesse The Correct Word ,So You Are win .")
            break
        w=input("\nGuess Another word : ")
        guess=w.lower()
        guesses+=guess
        if guess not in x:
            chances-=1
            print(f"Wrong choice.{chances} Chances Are  Left")
            if chances ==0:
                print("Game Over")
                print("you Are Loose.")

abc="\033[1;35m***** WORD GUESSING GAME *****\033[0m"
print(abc.center(172))
player_name=input("ENTER YOUR NAME : ")

print(f"\033[1;33mBest of Luck! \033[0m{player_name.capitalize()}")
print("PLEASE GUESSES CHARACTERS")
# call random_choice function here.
a=random_choice()
# call guessing function here.
guessing(a)

