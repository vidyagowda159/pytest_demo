# custom markers - grouping the testcases
import pytest


@pytest.mark.smoke_test
def test_add():
	print("in test add")


@pytest.mark.regression
def test_spam():
	print("in test spam")


@pytest.mark.smoke_test
def test_sample():
	print("in test sample")

"""
pytest command -m "smoke_test"
pytest command -m "smoke_test or regression"
pytest command -m "smoke_test and regression"
pytest command -m "not smoke_test"
"""

