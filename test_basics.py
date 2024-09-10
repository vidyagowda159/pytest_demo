"""
pip install pytest

naming conventions
--------------------
module/file - test_*.py or *_test.py

class -
		class TestClassName:        # pascal

function/method -
		def test_function_name():
			pass

commands
--------
1. pytest test_file.py -vs
2. pytest test_file.py::TestClass::test_function -vs

"""
class TestSample:
	# no init method

	def test_display(self):     # test cases
		print("in test display")
		raise ValueError


def test_spam():
	print("in test spam")















