import pytest


# pytest addoption

def pytest_addoption(parser):
	parser.addoption("--number", action="store")

# number = 10


@pytest.fixture()
def greet(request):
	number = request.config.getoption("--number")
	print("in conftest greet......")
	yield number
	print("ended greet function.....")

"""
pytest -vs 
"""