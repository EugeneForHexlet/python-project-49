#!/usr/bin/env python3
import prompt
import random
import brain_games.logic


def main():
    name = brain_games.logic.user_welcome()
    print('What number is missing in the progression?')

    i = 0
    while i < 3:

        rand_start = random.randint(1, 20)
        rand_step = random.randint(2, 7)
        rand_hidden = random.randint(1, 9)
        arr_progresion = [rand_start]

        def progression_arr(step):
            i = 1
            while i < 10:
                acc = arr_progresion[len(arr_progresion) - 1] + step
                arr_progresion.extend([acc])
                i = i + 1

            return arr_progresion

        progression_arr(rand_step)
        result = arr_progresion[rand_hidden]
        arr_progresion.pop(rand_hidden)
        arr_progresion.insert(rand_hidden, '...')

        def progression_str(arr):
            resultStr = ''
            for el in arr:
                resultStr = resultStr + str(el) + ' '
            return resultStr

        progression_res = progression_str(arr_progresion)
        print('Question: ' + progression_res)
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
