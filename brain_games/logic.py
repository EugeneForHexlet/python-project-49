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


def user_error(reply, result, name):
    rpl_tmpl = 'is wrong answer ;(. Correct answer was'
    print(f"'{reply}' '{rpl_tmpl}' '{result}'.\nLet's try again, {name}!")


# Движок игры brain_calc.py
def brain_calc_func(name, symbols):
    print('What is the result of the expression?')

    for _ in range(3):
        one_rnd_int = random.randint(1, 10)
        two_rnd_int = random.randint(1, 10)
        rand_symbol = random.choice(symbols)

        expression = f'{one_rnd_int} {rand_symbol} {two_rnd_int}'

        if rand_symbol == '+':
            result = one_rnd_int + two_rnd_int
        elif rand_symbol == '-':
            result = one_rnd_int - two_rnd_int
        elif rand_symbol == '*':
            result = one_rnd_int * two_rnd_int

        print('Question: ' + expression)
        reply = prompt.string('Your answer: ')

        if str(result) == reply:
            print('Correct!')
        else:
            user_error(reply, result, name)
            return

    user_win(name)


# Движок игры brain_even.py
def brain_even_func(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0
    while i < 3:
        rnd_int = random.randint(1, 10)
        print('Question: ' + str(rnd_int))
        rpl = prompt.string('Your answer: ')
        result = 'yes' if rnd_int % 2 == 0 else 'no'

        if (rnd_int % 2 == 0) == (rpl == 'yes'):
            print('Correct!')
            if i == 2:
                user_win(name)
        else:
            user_error(rpl, result, name)
            break

        i = i + 1


# Движок игры brain_gcd.py
def brain_gcd_dev(a, b):
    while b:
        a, b = b, a % b
    return a


def brain_gcd_question():
    one_rand_number = random.randint(1, 20)
    two_rand_number = random.randint(1, 20)
    print(f"Question: {one_rand_number} {two_rand_number}")
    answer = prompt.string('Your answer: ')
    return one_rand_number, two_rand_number, answer


def brain_gcd_func(name):
    print('Find the greatest common divisor of given numbers.')

    i = 0
    while i < 3:

        one_rand_number, two_rand_number, answer = brain_gcd_question()
        result = brain_gcd_dev(one_rand_number, two_rand_number)

        if int(answer) == result:
            print('Correct!')
            if i == 2:
                user_win(name)
        else:
            user_error(answer, result, name)
            break

        i = i + 1


# Движок игры brain_prime.py
def brain_prime_just_number(number):
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


def brain_prime_func(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    i = 0
    while i < 3:
        rnd_int = random.randint(1, 10)
        print('Question: ' + str(rnd_int))
        reply = prompt.string('Your answer: ')

        result = brain_prime_just_number(rnd_int)

        if result == reply:
            print('Correct!')
            if i == 2:
                user_win(name)
        else:
            user_error(reply, result, name)
            break

        i = i + 1


# Движок игры brain_progression.py
def brain_progression_generate(a, b, length=10):
    progression = [a + i * b for i in range(length)]
    return progression


def brain_progression_string(progression, hidden):
    hidden_el = progression[:]
    hidden_el[hidden] = '..'
    return ' '.join(map(str, hidden_el))


def brain_progression_question():
    rand_start = random.randint(1, 20)
    rand_step = random.randint(2, 7)
    rand_hidden = random.randint(1, 9)

    progression = brain_progression_generate(rand_start, rand_step)
    result = progression[rand_hidden]
    prog_str = brain_progression_string(progression, rand_hidden)

    print('Question: ' + prog_str)
    reply = prompt.string('Your answer: ')

    return result, reply


def brain_progression_func(name):
    print('What number is missing in the progression?')

    i = 0
    while i < 3:
        reply, result = brain_progression_question()

        if str(result) == reply:
            print('Correct!')
            if i == 2:
                user_win(name)
        else:
            user_error(reply, result, name)
            break

        i = i + 1
