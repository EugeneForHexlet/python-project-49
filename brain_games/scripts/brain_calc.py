#!/usr/bin/env python3
import brain_games.logic

symbols = ['+', '-', '*']


def main():
    brain_games.logic.start_game(brain_games.logic.brain_calc_func, symbols)


if __name__ == '__main__':
    main()
