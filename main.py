#!/usr/bin/env python3

import sys

import card


def main():
    for c in card.DECK:
        for o in card.DECK:
            c.record_outcome(o)
        print(c.get_display())


if __name__ == '__main__':
    main()
    sys.exit()
