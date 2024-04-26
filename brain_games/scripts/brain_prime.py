#!/usr/bin/env python3
import prompt
import random
import brain_games.logic


def main():
    name = brain_games.logic.user_welcome()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    i = 0
    while i < 3:
        randNumber = random.randint(1, 10)
        print('Question: ' + str(randNumber))
        answer = prompt.string('Your answer: ')

        def justNumber(number):
            if number <= 1:
                return 'no'
            if number <= 3:
                return 'yes'
            if number % 2 == 0 or number % 3 == 0:
                return 'no'
            i = 5
            while i * i <= number:
                if number % i == 0 or number % (i + 2) == 0:
                    return 'no'
                i += 6
            return 'yes'

        result = justNumber(randNumber)

        if result == answer:
            print('Correct!')
            if i == 2:
                brain_games.logic.user__win(name)
        else:
            brain_games.logic.user__error(answer, result, name)
            break

        i = i + 1


if __name__ == '__main__':
    main()
