#!/usr/bin/env python3
import brain_games.logic

symbols = ['+', '-', '*']


def main():
    name = brain_games.logic.user_welcome()
    brain_games.logic.brain_calc_func(name, symbols)


if __name__ == '__main__':
    main()
