#!/usr/bin/env python3
import prompt
import random
import brain_games.logic


def main():
    name = brain_games.logic.user_welcome()
    print('Find the greatest common divisor of given numbers.')

    i = 0
    while i < 3:
        firstRandNumber = random.randint(1, 20)
        secondRandNumber = random.randint(1, 20)
        print(f"Question: {firstRandNumber} {secondRandNumber}")
        answer = prompt.string('Your answer: ')

        arrayNumbersSort = sorted([firstRandNumber, secondRandNumber])

        if arrayNumbersSort[1] % arrayNumbersSort[0] == 0:
            result = arrayNumbersSort[0]
        else:
            devider = arrayNumbersSort[0] // 2
            while devider > 0:
                if arrayNumbersSort[0] % devider == 0 and arrayNumbersSort[1] % devider == 0:
                    result = devider
                    break
                devider = devider - 1

        if int(answer) == result:
            print('Correct!')
            if i == 2:
                brain_games.logic.user__win(name)
        else:
            brain_games.logic.user__error(answer, result, name)
            break

        i = i + 1


if __name__ == '__main__':
    main()
