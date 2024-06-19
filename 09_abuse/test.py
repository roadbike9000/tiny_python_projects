#!/usr/bin/env python3
"""tests for abuse.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput

prg = './abuse.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_adjective_str():
    """bad_adjectives"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -a {bad}')
    assert rv != 0
    assert re.search(f"Please enter a number > 0", out)


# --------------------------------------------------
def test_bad_adjective_num():
    """bad_adjectives"""

    n = random.choice(range(-10, 0))
    rv, out = getstatusoutput(f'{prg} -a {n}')
    print(out)
    assert rv != 0
    assert re.search(f"Please enter a number > 0", out)


# --------------------------------------------------
def test_bad_insults_str():
    """bad_insults_number"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -i {bad}')
    assert rv != 0
    assert re.search(f"Please enter a number > 0", out)


# --------------------------------------------------
def test_bad_insults_int():
    """bad_insults_number"""

    n = random.choice(range(-10, 0))
    rv, out = getstatusoutput(f'{prg} -i {n}')
    assert rv != 0
    assert re.search(f"Please enter a number > 0", out)


# --------------------------------------------------
def test_bad_seed():
    """bad seed"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -s {bad}')
    assert rv != 0
    assert re.search(f"Please enter a number > 0", out)


# --------------------------------------------------
def test_one_noun_seed_1():
    """test one noun with seed 1"""

    out = getoutput(f'{prg} -s 1 -i 1')
    assert out.strip() == 'You filthsome, cullionly fiend!'


# --------------------------------------------------
def test_seed_2():
    """test seed 2"""

    out = getoutput(f'{prg} --seed 2')
    expected = """
You corrupt, detestable beggar!
You peevish, foolish gull!
You insatiate, heedless worm!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_seed_3_five_insults_one_adjective():
    """test seed 3 with five insults and one adjective"""

    out = getoutput(f'{prg} -s 3 -i 5 -a 1')
    expected = """
You infected villain!
You vile braggart!
You peevish worm!
You sodden-witted villain!
You cullionly worm!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_seed_4_two_insults_four_adjectives():
    """test seed 4 with two insults and four adjectives"""

    out = getoutput(f'{prg} --seed 4 --insults 2 --adjectives 4')
    expected = """
You infected, lecherous, dishonest, rotten recreant!
You filthy, detestable, cullionly, base lunatic!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
