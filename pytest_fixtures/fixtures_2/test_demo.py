# import pytest
#
# pytestmark = pytest.mark.usefixtures("greet")

def test_palindrome():
	string = "hello"
	assert string == string[::-1], "not a palindrome"

