#!/usr/bin/env python3
"""tests for gashlycrumb.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput
import phonebook
import argparse
from unittest.mock import mock_open, patch


prg = './phonebook.py'


# --------------------------------------------------
def file_flag():
    """Either -f or --file"""

    return '-f' if random.randint(0, 1) else '--file'


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
def test_bad_file():
    """Test for bad --file"""

    bad = random_string()
    letter = random.choice(string.ascii_lowercase)
    rv, out = getstatusoutput(f'{prg} {letter} -f {bad}')
    assert rv != 0
    expected = f"No such file or directory: '{bad}'"
    assert re.search(expected, out)


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


#---------------------------------------------------
# Test check for name = None, replace with "None
import pytest
from unittest.mock import patch, mock_open
import phonebook

def test_name_is_null():
    mock_data_dict = {
        "John": "john@emailexample.com",
        "Jane": "jane@emaildud.com",
        None: "unknown@dudemail.com"
    }
    mock_data = "\n".join([f"{name}:{contact}" if name else f":{contact}" for name, contact in mock_data_dict.items()])

    with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(file=iter(mock_data.split('\n')))):
        with patch('builtins.print') as mock_print:
            phonebook.main()
            mock_print.assert_any_call('None: unknown@dudemail.com')


#---------------------------------------------------
# Test check for contact = None, replace with "None
import pytest
from unittest.mock import patch, mock_open
import phonebook

def test_contact_is_null():
    mock_data_dict = {
        "John": "john@emailexample.com",
        "Jane": "jane@emaildud.com",
        "Jerry": None
    }
    mock_data = "\n".join([f"{name}:{contact}" if name else f":{contact}" for name, contact in mock_data_dict.items()])

    with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(file=iter(mock_data.split('\n')))):
        with patch('builtins.print') as mock_print:
            phonebook.main()
            mock_print.assert_any_call('Jerry: None')


#---------------------------------------------------
# Test check for contact = "", replace with "None
import pytest
from unittest.mock import patch, mock_open
import phonebook

def test_contact_is_empty_string():
    mock_data_dict = {
        "John": "john@emailexample.com",
        "Jane": "jane@emaildud.com",
        "Jerry": ""
    }
    mock_data = "\n".join([f"{name}:{contact}" if name else f":{contact}" for name, contact in mock_data_dict.items()])

    with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(file=iter(mock_data.split('\n')))):
        with patch('builtins.print') as mock_print:
            phonebook.main()
            mock_print.assert_any_call('Jerry: None')