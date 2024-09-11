import pytest


def test_even():
	assert 2 % 2 == 0


@pytest.mark.regression
@pytest.mark.smoke_test
def test_palindrome():
	a = "mom"
	assert a == a[::-1]

