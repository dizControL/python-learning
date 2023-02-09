word = "snake"
guess = ""
guess_amount = 0
guess_limit = 3
limit = False

while guess != word and not (limit):
    if guess_amount < guess_limit:
        guess = input("Enter word: ")
        guess_amount += 1
    else:
        limit = True

if limit:
    print("You are out of guesses.")
else:
    print("You got the word! Good Job.")
