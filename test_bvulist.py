from bvulist import bvulist
import pytest

def test_prepend():
    L = bvulist()
    L.prepend(2)
    L.prepend(1)
    assert L[0] == 1 and L[1] == 2 and len(L) == 2

def test_pop_back():
    L = bvulist()
    L.append(1)
    L.append(2)
    L.append(3)
    assert L.pop_back() == 3 and L[:] == [1, 2]

def test_pop_back_empty():
    L = bvulist()
    with pytest.raises(IndexError):
        L.pop_back()

def test_pop_front():
    L = bvulist()
    L.append(1)
    L.append(2)
    L.append(3)
    assert L.pop_front() == 1 and L[:] == [2, 3]

def test_pop_front_empty():
    L = bvulist()
    with pytest.raises(IndexError):
        L.pop_front()
