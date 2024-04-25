#!/usr/bin/env python3
import prompt
import random
import brain_games.logic


def main():
    name = brain_games.logic.user_welcome()
    print('What is the result of the expression?')

    i = 0
    while i < 3:

        randStart = random.randint(1, 20)
        randStep = random.randint(2, 7)
        randHidden = random.randint(1, 9)
        arrProgresion = [randStart]

        def progressionArr(step):
            i = 1
            while i < 10:
                acc = arrProgresion[len(arrProgresion) - 1] + step
                arrProgresion.extend([acc])
                i = i + 1

            return arrProgresion

        progressionArr(randStep)
        result = arrProgresion[randHidden]
        arrProgresion.pop(randHidden)
        arrProgresion.insert(randHidden, '...')

        def progressionStr(arr):
            resultStr = ''
            for el in arr:
                resultStr = resultStr + str(el) + ' '
            return resultStr

        progressionRes = progressionStr(arrProgresion)
        print('Question: ' + progressionRes)
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
