#!/usr/bin/env python3
"""
Author : Jeff Smathers <roadbike2000@duck.com>
Date   : 2024-05-10
Purpose: Get command-line arguments
filename: crowsnest.py

"""

import argparse


# --------------------------------------------------
def get_args(args=None):
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args(args)


# --------------------------------------------------
def check_arg(arg):
    """Check if the argument is a string of letters only"""
    return isinstance(arg, str) and arg.isalpha()


# --------------------------------------------------
def main():
    """Make a report from the crows nest"""

    args = get_args()
    word = args.word
    if check_arg(word):
        print(f"Ahoy, Captain, {'an' if word[0].lower() in 'aeiou' else 'a'} {word} off the larboard bow!")
    else:
        print(f"{word} is not a word. Please try again.")

# --------------------------------------------------
if __name__ == '__main__':
    main()
