#!/usr/bin/env python3
"""
Author : Jeff Smathers <roadbike2000@duck.com>
Date   : 2024-05-25
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "text",
        metavar="str",
        help="Input phone number as text",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    number = args.text
    # new_number = ''
    jumper = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5"
    }
    for char in number:
        print(jumper.get(char, char), end="")


# --------------------------------------------------
if __name__ == "__main__":
    main()
