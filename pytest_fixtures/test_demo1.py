# print("start")
# import pytest
#
# @pytest.fixture
# def display():
# 	print("start")      # set up -> before tc
# 	yield
# 	print("end")        # teardown -> after tc
#
#
# def test_even(display):
# 	num = 10
# 	assert num % 2 == 0, f"{num} is not even"
# 	print("in test even")


# print("end")
############################################################
# import pytest
#
# @pytest.fixture(autouse=True)
# def display():
# 	print("start....")      # set up -> before tc
# 	yield
# 	print("end....")        # teardown -> after tc
#
# def test_even():
# 	num = 10
# 	assert num % 2 == 0, f"{num} is not even"
# 	print("in test even")
#
# def test_spam():
# 	print("in test spam")
#
# def test_greet():
# 	print("hellooo")

##########################################################
import pytest

@pytest.fixture(autouse=True)
def display():
	print("start....")      # set up -> before tc
	yield 10
	print("end....")        # teardown -> after tc

def test_even(display):
	print(display)          # 10
	num = display
	assert num % 2 == 0, f"{num} is not even"
	print("in test even")

def test_spam():
	print(display)      # <function display at 0x000002C6DEB10280>
	print("in test spam")

def test_greet():
	print("hellooo")