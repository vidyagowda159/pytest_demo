"""
2 types
-------
@pytest.mark.marker_name

1. inbuilt - skip, skipif, xfail, parametrize, dependency, usefixtures
2. custom

assert
------
assert condition[, message]
true - control is given to the next statement
false - raise AssertionError
"""
import pytest

num = 11
num2 = 0

@pytest.mark.skip(reason="test even passes everytime")
def test_even():
	assert num % 2 == 0, f"{num} is not even"
	print("number is even")

@pytest.mark.skipif(num2 == 0, reason="denominator is zero")
def test_division():
	assert num / num2 != 0

@pytest.mark.xfail(num == 10, reason="number is 11")
def test_odd():
	assert num % 2 != 0, f"{num} is not odd"
	print("number is odd")


"""
pip install pytest-dependency
"""

@pytest.mark.dependency(name="add")
def test_add():
	assert num + 10 == 20, f"sum is not 20"


@pytest.mark.dependency(name="palindrome", depends=["add"])
def test_palindrome():
	string = "hello"
	assert string == string[::-1], "not a palindrome"

###########################################################

# @pytest.mark.xfail(2 == 2)
# def test_login():
# 	driver.find_element("id", "abc").send_keys("admin")


