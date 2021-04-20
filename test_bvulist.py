import pytest
from bvulist import bvulist

def test_prepend():
    L = bvulist()
    L.prepend(2)
    L.prepend(1)
    assert len(L) == 2
    assert L[0] == 1 and L[1] == 2
    assert L == bvulist([1, 2])

def test_pop_front():
    L = bvulist([1, 2])
    assert L.pop_front() == 1
    assert L.pop_front() == 2
    with pytest.raises(IndexError):
        L.pop_front()

def test_pop_back():
    L = bvulist([1, 2])
    assert L.pop_back() == 2
    assert L.pop_back() == 1
    with pytest.raises(IndexError):
        L.pop_back()

def test_legacy_list_methods():
    L = bvulist([1, 2])
    L.append(3)
    assert L[-1] == 3

