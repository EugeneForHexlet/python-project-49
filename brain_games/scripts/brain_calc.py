#!/usr/bin/env python3
import prompt
import random
import brain_games.logic


symbols = ['+', '-', '*']


def main():
    name = brain_games.logic.user_welcome()
    print('What is the result of the expression?')

    i = 0
    while i < 3:
        oneRandNumber = random.randint(1, 10)
        twoRandNumber = random.randint(1, 10)
        randSymbol = random.choice(symbols)

        expression = f'{oneRandNumber} {randSymbol} {twoRandNumber}'

        if randSymbol == '+':
            result = oneRandNumber + twoRandNumber
        elif randSymbol == '-':
            result = oneRandNumber - twoRandNumber
        elif randSymbol == '*':
            result = oneRandNumber * twoRandNumber

        print('Question: ' + expression)
        answer = prompt.string('Your answer: ')

        if str(result) == answer:
            print('Correct!')
            if i == 2:
                brain_games.logic.user__win(name)
        else:
            brain_games.logic.user__error(answer, result, name)
            break

        i = i + 1


if __name__ == '__main__':
    main()
