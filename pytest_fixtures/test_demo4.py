# import pytest
#
# @pytest.fixture(scope="module", autouse=True)
# def display():
# 	print("start....")      # set up -> before tc
# 	yield 10
# 	print("end....")        # teardown -> after tc
#
#
# def test_palindrome():
# 	string = "hello"
# 	assert string == string[::-1], "not a palindrome"
#
#
# class TestCalculator:
#
# 	def test_add(self):
# 		print("in test add")
#
# 	def test_sub(self):
# 		print("in test sub")
#
# 	def test_multiply(self):
# 		print("in multiply")
#
#
# class TestNumber:
#
# 	def test_even(self):
# 		print("in even")
#
# 	def test_odd(self):
# 		print("in odd")

#############################################################
import pytest

@pytest.fixture(scope="module")
def display():
	print("start....")      # set up -> before tc
	yield 10
	print("end....")        # teardown -> after tc

pytestmark = pytest.mark.usefixtures("display")

def test_palindrome():
	string = "hello"
	assert string == string[::-1], "not a palindrome"


class TestCalculator:

	def test_add(self):
		print("in test add")

	def test_sub(self):
		print("in test sub")

	def test_multiply(self):
		print("in multiply")


class TestNumber:

	def test_even(self):
		print("in even")

	def test_odd(self):
		print("in odd")
