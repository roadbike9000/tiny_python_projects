#!/usr/bin/env python3
"""tests for telephone.py"""

from subprocess import getstatusoutput, getoutput
import os
import random
import re
import string

prg = "./telephone.py"
fox = '../inputs/fox.txt'
now = '../inputs/now.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)
    assert os.path.isfile(fox)
    assert os.path.isfile(now)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'{prg} {flag}')
        assert re.match('usage', out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_seed_str():
    """bad seed str value"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -s {bad} {fox}')
    assert rv > 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_mutation_str():
    """Test case for bad mutation str value.

    This function tests the behavior of the program when a bad mutation string value is provided.
    It generates a random string using the `random_string` function and passes it as an argument to the program.
    The function then checks that the return value is greater than 0 and that the output contains the expected error message.

    Raises:
        AssertionError: If the return value is not greater than 0 or if the expected error message is not found in the output.
    """
    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -m {bad} {fox}')
    assert rv > 0
    assert re.search(f"invalid float value: '{bad}'", out)


# --------------------------------------------------
def test_bad_mutation():
    """
    Test function for bad mutation values.

    This function tests the behavior of the program when provided with invalid mutation values.
    It iterates over a list of invalid mutation values and asserts that the return value (rv) is greater than 0,
    indicating an error, and that the output (out) contains the expected error message.

    Args:
        None

    Returns:
        None
    """
    for val in ['-1.0', '10.0']:
        rv, out = getstatusoutput(f'{prg} -m {val} {fox}')
        assert rv > 0
        assert re.search(f'--mutations "{val}" must be between 0 and 1', out)


# --------------------------------------------------
def test_for_echo():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(f'{prg} -m 0 "{txt}"')
    assert rv == 0
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{txt}"'


# --------------------------------------------------
def test_now_cmd_s1():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(f'{prg} -s 1 "{txt}"')
    assert rv == 0
    expected = """
    Now is Ege time [dr all good me- to come to the jid of the party.
    """.strip()
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def test_now_cmd_s2_m4():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(f'{prg} -s 2 -m .4 "{txt}"')
    assert rv == 0
    expected = """
    No$ i% khefMiIe sor@all$glo<BmenYts cAAeltaTtheSaid[HYnthe Aalty.
    """.strip()
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def test_fox_file_s1():
    """test"""

    rv, out = getstatusoutput(f'{prg} --seed 1 {fox}')
    assert rv == 0
    txt = open(fox).read().rstrip()
    expected = "The duic: brown hox jumps over the lkzy dog."
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def test_fox_file_s2_m6():
    """test"""

    rv, out = getstatusoutput(f'{prg} --seed 2 --mutations .6 {fox}')
    assert rv == 0
    txt = open(fox).read().rstrip()
    expected = "ZoA@qric` HwdTB Alx$jumIslolXs th^Yl?dy<YoA."
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
