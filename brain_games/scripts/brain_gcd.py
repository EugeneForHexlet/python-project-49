#!/usr/bin/env python3
import prompt
import random
import brain_games.logic


def main():
    name = brain_games.logic.user_welcome()
    print('Find the greatest common divisor of given numbers.')

    i = 0
    while i < 3:
        one_rand_number = random.randint(1, 20)
        two_rand_number = random.randint(1, 20)
        print(f"Question: {one_rand_number} {two_rand_number}")
        answer = prompt.string('Your answer: ')

        array_numbers_sort = sorted([one_rand_number, two_rand_number])

        if array_numbers_sort[1] % array_numbers_sort[0] == 0:
            result = array_numbers_sort[0]
        else:
            devider = array_numbers_sort[0] // 2
            while devider > 0:
                if array_numbers_sort[0] % devider == 0 and array_numbers_sort[1] % devider == 0:
                    result = devider
                    break
                devider = devider - 1

        if int(answer) == result:
            print('Correct!')
            if i == 2:
                brain_games.logic.user_win(name)
        else:
            brain_games.logic.user_error(answer, result, name)
            break

        i = i + 1


if __name__ == '__main__':
    main()
