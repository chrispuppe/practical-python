from random import randrange


print("Hi, what's your name?")

username = input('Type your name: ')

print(username.capitalize(), "I'm thinking of a number between 1 and 100.")

computers_number = randrange(1, 100)
keep_playing = True
atempts = 0

while keep_playing:
    guess = int(input('Your guess: '))
    atempts += 1

    if guess > computers_number:
        print('Your guess is too high, try again.')
    elif guess < computers_number:
        print('Your guess is too low, try again.')
    elif guess == computers_number:
        print(f'Well done, {username}. ' +
            f'You guessed my number in {atempts} tries!')
        keep_playing = False
 