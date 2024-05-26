#!/usr/bin/env python3
"""tests for jump.py"""

import os
from subprocess import getstatusoutput

prg = './jump.py'


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
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_only_numbers():
    """numbers and nothing else"""

    rv, out = getstatusoutput(f'{prg} 123-456-7890')
    assert rv == 0
    assert out == '987-604-3215'


# --------------------------------------------------
def test_text_with_numbers():
    """Text with numbers xxx-xxx-xxxx"""

    rv, out = getstatusoutput(f'{prg} "That number to call is 098-765-4321."')
    assert rv == 0
    assert out.rstrip() == 'That number to call is 512-340-6789.'

# --------------------------------------------------
def test_text_with_numbers_2():
    """Text with numbers (xxx) xxx xxxx """

    rv, out = getstatusoutput(f'{prg} "Call (706) 890 3075."')
    assert rv == 0
    assert out.rstrip() == "Call (354) 215 7530."