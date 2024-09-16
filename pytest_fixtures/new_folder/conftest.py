import pytest

# command line arguments -> strings

# def pytest_addoption(parser):
# 	parser.addoption("--num")
#
#
# @pytest.fixture
# def display(request):
# 	number = int(request.config.getoption("--num"))
# 	yield number

##########################################################
# def pytest_addoption(parser):
# 	parser.addoption("--num", dest="name1")
#
#
# @pytest.fixture
# def display(request):
# 	# number = int(request.config.option.name1)
# 	number = int(request.config.getoption("--num"))
# 	yield number

#############################################################
from selenium import webdriver


def pytest_addoption(parser):
	parser.addoption("--num", dest="number")
	parser.addoption("--browser",
	                dest="browser_name",
	                action="store",
	                help="get browser name for execution",
	                choices=["chrome", "edge", "firefox"]
	                 )


@pytest.fixture
def driver_init(request):
	browser = request.config.option.browser_name

	if browser.lower() == "chrome":
		driver = webdriver.Chrome()

	elif browser.lower() == "firefox":
		driver = webdriver.Firefox()

	elif browser.lower() == "edge":
		driver = webdriver.Edge()

	# else:
	# 	raise ValueError(f"Invalid browser: {browser}")

	driver.get("https://demowebshop.tricentis.com/")
	driver.maximize_window()
	driver.implicitly_wait(10)
	yield driver
	print(driver.title)
	driver.close()











