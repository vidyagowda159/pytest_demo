import pytest

class TestSample:

	@pytest.mark.dependency()
	def test_demo(self):
		assert False


class TestDemo:

	@pytest.mark.dependency(depends=["TestSample::test_demo"])
	def test_spam(self):
		assert True

