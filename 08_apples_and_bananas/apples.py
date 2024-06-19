#!/usr/bin/env python3
"""
Author : Jeff Smathers <roadbike2000@duck.com>
Date   : 2024-06-14
Purpose: Find and replace vowels
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))
    
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Find and replace vowels"""

    args = get_args()
    text = args.text
    vowel = args.vowel
    new_text = []

    for char in text:
        if char in 'aeiou':
            new_text.append(vowel)
        elif char in 'aeiou'.upper():
            new_text.append(vowel.upper())
        else:
            new_text.append(char)

    print(''.join(new_text))


# --------------------------------------------------
if __name__ == '__main__':
    main()
