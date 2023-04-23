
import random
# import hangman_words
from hangman_words import word_list
# from hangman_art import stages
from hangman_art import logo,stages
import os


print(logo)
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(hangman_words.word_list)-et khali import hangman_word korle erokom
chosen_word = random.choice(word_list)


lives=6

print(f'Psst, the solution is {chosen_word}.')



display=[]
word_length=len(chosen_word)
for _ in range(word_length):
    display+="_"
print(display)

end_of_game=False

while not end_of_game:
    guess = input("Guess a letter: ").lower()


    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    clear_console()


    if guess in display:
        print(f"You have already guessed {guess}")


    for position in range(word_length):
        letter=chosen_word[position]
        if letter == guess:
            display[position]=letter
        
    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word therefore you loose a life")
        lives-=1
        if lives ==0:
            end_of_game=True
            print("You lose")

    print(display)

    if "_" not in display:
        end_of_game=True
        print("You Win")

    print(stages[lives])