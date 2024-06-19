#!/usr/bin/env python3
"""
Author : Jeff Smathers <roadbike2000@duck.com>
Date   : 2024-06-19
Purpose: Heap Abuse by random insults
"""

import argparse
import random


# --------------------------------------------------
def positive_integer(value):
    try:
        ivalue = int(value)
        if ivalue <= 0:
            raise ValueError
        return ivalue
    except ValueError:
        raise argparse.ArgumentTypeError("Please enter a number > 0")


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Heap Abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adjectives',
                        type=positive_integer,
                        default=2)

    parser.add_argument('-i',
                        '--insults',
                        help='Number of insults',
                        metavar='insults',
                        type=positive_integer,
                        default=3)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=positive_integer,
                        default=None)

    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.insults < 1:
        parser.error(f'--insults "{args.insults}" must be > 0')
    
    return args


# --------------------------------------------------
def main():
    """Heap Abuse with random insults"""

    args = get_args()
    random.seed(args.seed)

    adjectives = """
    bankrupt base caterwauling corrupt cullionly detestable dishonest false
    filthsome filthy foolish foul gross heedless indistinguishable infected
    insatiate irksome lascivious lecherous loathsome lubbery old peevish
    rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
    thin-faced toad-spotted unmannered vile wall-eyed
    """.strip().split()

    nouns = """
    Judas Satan ape ass barbermonger beggar block boy braggart butt
    carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
    gull harpy jack jolthead knave liar lunatic maw milksop minion
    ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    """.strip().split()
    
    for _ in range(args.insults):
        abusive_adjectives = ', '.join(random.sample(adjectives, k=args.adjectives))
        print(f'You {abusive_adjectives} {random.choice(nouns)}!')    

# --------------------------------------------------
if __name__ == '__main__':
    main()
