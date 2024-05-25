#!/usr/bin/env python3
"""
Author : Jeff Smathers <roadbike2000@duck.com>
Date   : 2024-05-22
Purpose: List items for a picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='List items for a picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='item',
                        nargs='+',
                        help='Item(s) to bring',)

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Bring items to a picnic"""

    args = get_args()
    items = args.item
    number_of_items = len(items)

    if args.sorted:
        items.sort()   

    bringing_items = ''
    if number_of_items == 1:
        bringing_items = items[0]
    elif number_of_items == 2:
        bringing_items = ' and '.join(items)
    else:
        bringing_items = ', '.join(items[:-1]) + ', and ' + items[-1]
    print(f"You are bringing {bringing_items}.")



# --------------------------------------------------
if __name__ == '__main__':
    main()
