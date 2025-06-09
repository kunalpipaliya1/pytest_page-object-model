# Program: 1
# Grouping Tests

import pytest

@pytest.mark.sanity
def test_case1():
    assert True

@pytest.mark.regression
def test_case2():
    assert True

@pytest.mark.sanity
@pytest.mark.regression
def test_case3():
    assert True

# Run in Terminal below - 
# pytest -m sanity
# pytest -m "sanity and regression"

# Program: 2
# Priority of Tests
#  pip install pytest-order # to priority to execute code

import pytest

@pytest.mark.order(2)
def test_b():
    print("B")
    assert True

@pytest.mark.order(13)
def test_a():
    print("A")
    assert True

# terminal command - pytest test_Practics.py -v -s

# Program: 3
# Invocation count(how many time repeat the code)
# pip install pytest-repeat   # Invocation Count (Repeat Test)

import pytest

@pytest.mark.repeat(2)
def test_b():
    print("B")
    assert True

@pytest.mark.repeat(5)
def test_a():
    print("A")
    assert True

