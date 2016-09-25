"""
I am not entirely sure if you know what hangman means but it is game where i give a word and then you guess the word
based on the set of the characters available in the word originally.
hope this is gonna really be fun.

first of all I get random word out of a set of words and then i replace most of the values with a blank
leaving behind some of the original characters.

if the word is more than ten provide 3 else 2
"""
import random
import re


def randoms(word):
    rands = []
    if len(word) < 5:
        r = random.randint(0, len(word) - 1)
        rands.append(word[r])
    elif len(word) < 10:
        k = 0
        for i in range(2):
            r = random.randint(0, len(word) - 1)

            if k == 1:
                while rands[0][0] == r:
                    r = random.randint(0, len(word) - 1)

            rands.append(word[r])
            k += 1
    else:
        k = 0
        for i in range(3):
            r = random.randint(0, len(word) - 1)

            if k == 1:
                while rands[0][0] == r:
                    r = random.randint(0, len(word) - 1)

            if k == 2:
                while rands[0][0] == r or rands[1][0] == r:
                    r = random.randint(0, len(word) - 1)

            rands.append(word[r])
            k += 1

    return rands


def execute(word):
    l = list("_" * len(word))
    rand = randoms(word)
    for f in rand:
        find = re.finditer(f, word)
        for u in find:
            l[u.start()] = u.group()

    return l


def inputs(word):
    sl = execute(word)
    print('A SIMPLE HANGMAN GAME', end="\n\n")
    print(" ".join(sl))

    for i in range(sl.count("_")):
        ni = input('please guess a letter:  ')
        find = re.finditer(ni, word)
        for u in find:
            sl[u.start()] = u.group()
        if "_" not in sl:
            print("\nCONGRATULATIONS. WELL DONE")
            print(" ".join(sl))
            break

        print(" ".join(sl), end="\n\n")

    if "_" in sl:
        print("SORRY BUT KEEP TRYING YOUR LUCK")
    return sl


if __name__ == '__main__':
    Word = 'floss folly Janice Eulogy Grave'
    for i in Word.split():
        inputs(i)
