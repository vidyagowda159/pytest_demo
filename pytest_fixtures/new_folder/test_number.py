
def test_even(display):
	num = display
	assert num % 2 == 0, f"{num} is not even"


def test_palindrome(display):
	num = display
	assert str(num) == str(num)[::-1], f"{num} is not a palindrome"

