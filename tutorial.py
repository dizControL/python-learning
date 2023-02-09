word = "snake"
guess = ""
guess_amount = 0
guess_limit = 3
limit = False

while guess != word and limit = False:
    if guess_amount <= guess_limit:
        guess = input("Enter word: ")
        guess_limit += 1
    else:
        limit = True

print("You got the word! Good Job.")
