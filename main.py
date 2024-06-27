import random
from art import logo
from word_list import word_list

print(logo)
lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_game = False
print(f'Pssst, the solution is {chosen_word}.')
display=[]
for n in range(word_length):
    display.append("_")
print(display)
while not end_game :

    guess = input("guess a letter").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    for p in range(word_length):
        letter = chosen_word[p]
        if letter == guess:
            display[p] = letter
    if guess not in chosen_word:
        print("you guessed it wrong, YOU LOSE A LIFE!")
        lives-=1
        if lives==0:
            end_game=True
            print("you have run out of lives. YOU LOSE!")

    if  "_" not in display:
        end_game=True
        print("YOU WON THE GAME!")

    from art import stages
    print(stages[lives])
