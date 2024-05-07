#!/usr/bin/env python3
import prompt
import random
import brain_games.logic


def main():
    name = brain_games.logic.user_welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0
    while i < 3:
        rand_number = random.randint(1, 10)
        print('Question: ' + str(rand_number))
        answer = prompt.string('Your answer: ')
        result = 'yes' if rand_number % 2 == 0 else 'no'

        if rand_number % 2 == 0 and answer == 'yes' or rand_number % 2 != 0 and answer == 'no':
            print('Correct!')
            if i == 2:
                brain_games.logic.user_win(name)
        else:
            brain_games.logic.user_error(answer, result, name)
            break

        i = i + 1


if __name__ == '__main__':
    main()
