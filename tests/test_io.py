import pytest
import os
from pathlib import Path
from spinas.io import replace_in_file, replace_in_lines

def test_replace_in_lines():
    lines = ['some [[text]] that', 'needs <<replacing>>']
    sub = {'[[text]]': 'nice text', '<<replacing>>': 'printing'}
    lines_out = replace_in_lines(lines, sub)
    assert len(lines_out) == 2
    assert lines_out[0] == 'some nice text that'
    assert lines_out[1] == 'needs printing'

def test_replace_does_not_add_lines(tmp_path):
    path = Path(os.path.dirname(__file__))
    sub = {'[[n_lines]]': '4', '[[values]]': 'values'}
    replace_in_file(path/'data/replace_in.txt', tmp_path/'replace_out.txt', sub)
    
    with open(path/'data/replace_in.txt') as f:
        before = f.readlines()

    with open(tmp_path/'replace_out.txt') as f:
        after = f.readlines()


    assert len(after) == len(before)