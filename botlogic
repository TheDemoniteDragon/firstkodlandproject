import random

def pass_gen(pass_length):
    character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for char in range(pass_length) :
        password += random.choice(character)

    return password

def rng(number) :
    result = random.randint(1, number)

    return result

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"
