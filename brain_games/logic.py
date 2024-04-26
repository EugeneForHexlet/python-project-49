import prompt


def user_welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    return name


def user__win(name):
    print('Congratulations, ' + name + '!')


def user__error(answer, result, name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
