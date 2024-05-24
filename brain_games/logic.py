#!/usr/bin/env python3
import prompt
import random


def user_welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    return name


def user_win(name):
    print('Congratulations, ' + name + '!')


def user_error(answer, result, name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")


# Движок игры brain_calc.py
def brain_calc_func(name, symbols):
    print('What is the result of the expression?')

    for _ in range(3):
        one_rand_number = random.randint(1, 10)
        two_rand_number = random.randint(1, 10)
        rand_symbol = random.choice(symbols)

        expression = f'{one_rand_number} {rand_symbol} {two_rand_number}'

        if rand_symbol == '+':
            result = one_rand_number + two_rand_number
        elif rand_symbol == '-':
            result = one_rand_number - two_rand_number
        elif rand_symbol == '*':
            result = one_rand_number * two_rand_number

        print('Question: ' + expression)
        answer = prompt.string('Your answer: ')

        if str(result) == answer:
            print('Correct!')
        else:
            user_error(answer, result, name)
            return

    user_win(name)


# Движок игры brain_even.py
def brain_even_func(name):
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
                user_win(name)
        else:
            user_error(answer, result, name)
            break

        i = i + 1


# Движок игры brain_gcd.py
def brain_gcd_func(name):
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
                user_win(name)
        else:
            user_error(answer, result, name)
            break

        i = i + 1


# Движок игры brain_prime.py
def brain_prime_func(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    i = 0
    while i < 3:
        rand_number = random.randint(1, 10)
        print('Question: ' + str(rand_number))
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

        result = justNumber(rand_number)

        if result == answer:
            print('Correct!')
            if i == 2:
                user_win(name)
        else:
            user_error(answer, result, name)
            break

        i = i + 1


# Движок игры brain_progression.py
def brain_progression_func(name):
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
        arr_progresion.insert(rand_hidden, '..')

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
                user_win(name)
        else:
            user_error(answer, result, name)
            break

        i = i + 1
