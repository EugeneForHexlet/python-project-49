import brain_games.logic


def main():
    name = brain_games.logic.user_welcome()
    brain_games.logic.brain_prime_func(name)


if __name__ == '__main__':
    main()
