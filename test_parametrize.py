# parametrize(arg_names, arg_list) - give arguments to a test case
import pytest


# @pytest.mark.parametrize("num", [1, 2, 3, 4])
# def test_even(num):
# 	assert num % 2 == 0, f"{num} is not even"

##########################################################
data = [("admin", "pwd123"), ("user1", "pwd")]

@pytest.mark.parametrize("username, password", data)
def test_validate(username, password):
	assert username == "admin", "invalid username"
	assert password == "pwd123", "invalid password"

"""
pip install pytest-html

pytest command -vs --html="report.html"
pytest command -vs --html="absolute_path/report.html"

# batch execution
pytest -vs

# parallel execution
pip install pytest-xdist

pytest -vs -n 3
pytest -vs -n=3

"""
