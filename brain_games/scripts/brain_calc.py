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
        one_rand_number = random.randint(1, 10)
        two_rand_number = random.randint(1, 10)
        randSymbol = random.choice(symbols)

        expression = f'{one_rand_number} {randSymbol} {two_rand_number}'

        if randSymbol == '+':
            result = one_rand_number + two_rand_number
        elif randSymbol == '-':
            result = one_rand_number - two_rand_number
        elif randSymbol == '*':
            result = one_rand_number * two_rand_number

        print('Question: ' + expression)
        answer = prompt.string('Your answer: ')

        if str(result) == answer:
            print('Correct!')
            if i == 2:
                brain_games.logic.user_win(name)
        else:
            brain_games.logic.user_error(answer, result, name)
            break

        i = i + 1


if __name__ == '__main__':
    main()
