#!/usr/bin/env python3
"""
Author : Jeff Smathers <roadbike2000@duck.com>
Date   : 2024-06-07
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Read a file and create a dictionary',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='A text file to read',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='phonebook.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Create a phonebook dictionary"""

    args = get_args()

    phonebook = {}
    for line in args.file:
        if line is None:
            name, contact = "None", "None"
        else:
            name, contact = line.strip().split(':') 
            name = name if name else "None"
            contact = contact if contact else "None"
        phonebook[name] = contact
    for name, contact in phonebook.items():
        print(f'{name}: {contact}')
# --------------------------------------------------
if __name__ == '__main__':
    main()
