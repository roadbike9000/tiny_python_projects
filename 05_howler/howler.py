#!/usr/bin/env python3
"""
Author : Jeff Smathers <roadbike2000@duck.com>
Date   : 2024-05-27
Purpose: Transmogrify text
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (Transmogrify text to upper case)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Name of the output file',
                        metavar='str',
                        type=str,
                        default='')
    
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper() + '\n')
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
