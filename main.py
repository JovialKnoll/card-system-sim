#!/usr/bin/env python3

import sys

import card


def main():
    print(len(card.DECK))
    for c in card.DECK:
        print(c.get_display())


if __name__ == '__main__':
    main()
    sys.exit()
