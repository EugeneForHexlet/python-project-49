#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0
    while i < 3:
        randNumber = random.randint(0, 20)
        print('Question: ' + str(randNumber))
        answer = prompt.string('Your answer: ')
        if randNumber % 2 == 0 and answer == 'yes' or randNumber % 2 != 0 and answer == 'no':
            print('Correct!')
            if i == 2:
                print('Congratulations, ' + name + '!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{'yes' if randNumber % 2 == 0 else 'no'}'.\nLet's try again, '{name}'!")
            break

        i = i + 1


if __name__ == '__main__':
    main()
