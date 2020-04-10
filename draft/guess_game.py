#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def guess_game(guess, answer):
    count = 0
    for k, v in enumerate(guess):
        if v == answer[k]:
            count += 1
    return count


if __name__ == '__main__':
    guess = [1, 2, 3]
    answer = [1, 2, 3]
    count = guess_game(guess, answer)
    print(count)
