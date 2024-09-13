import pytest


# @pytest.fixture(scope="class", autouse=True)
# def greet():
# 	print("Hai....")
# 	yield
# 	print("end....")


# @pytest.fixture(scope="module")
# def greet():
# 	print("Hai....")
# 	yield
# 	print("end....")

@pytest.fixture(scope="session", autouse=True)
def greet():
	print("Hai....")
	yield
	print("end....")

