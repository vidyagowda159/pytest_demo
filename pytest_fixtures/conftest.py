import pytest


@pytest.fixture()
def greet():
	print("in conftest greet......")
	yield
	print("ended greet function.....")
