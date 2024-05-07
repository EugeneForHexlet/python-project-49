#!/usr/bin/env python3
import prompt


def user_welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    return name


def user_win(name):
    print('Congratulations, ' + name + '!')


def user_error(answer, result, name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
