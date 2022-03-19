from random import randrange


number_of_dice = int(input('How many d6 dice would you like to roll? '))

i = 0
dice_total = 0
while number_of_dice > i:
    dice_total += randrange(1, 6)
    i += 1

print(f'Your dice total is {dice_total}.')