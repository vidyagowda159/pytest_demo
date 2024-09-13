# import pytest
#
# @pytest.fixture(autouse=True, scope="class")
# def display():
# 	print("start....")      # set up -> before tc
# 	yield 10
# 	print("end....")        # teardown -> after tc
#
#
# class TestCalculator:
#
# 	def test_add(self, display):
# 		print(display)          # 10
# 		print("in test add")
#
# 	def test_sub(self):
# 		print(display)          # address
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

###########################################################
import pytest

@pytest.fixture(scope="class")
def display():
	print("start....")      # set up -> before tc
	yield 10
	print("end....")        # teardown -> after tc


class TestCalculator:

	def test_add(self, greet):
		print("in test add")

	def test_sub(self):
		print("in test sub")

	def test_multiply(self):
		print("in multiply")


@pytest.mark.usefixtures("display")
class TestNumber:

	def test_even(self):
		print("in even")

	def test_odd(self):
		print("in odd")