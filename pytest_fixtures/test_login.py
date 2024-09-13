import time
import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"])
def driver_init(request):
	browser = request.param

	if browser == "chrome":
		driver = webdriver.Chrome()

	elif browser == "firefox":
		driver = webdriver.Firefox()

	driver.get("https://demowebshop.tricentis.com/")
	driver.maximize_window()
	driver.implicitly_wait(10)
	yield driver
	print(driver.title)
	driver.close()


def test_login(driver_init):
	driver = driver_init

	driver.find_element("link text", "Log in").click()
	driver.find_element("id", "Email").send_keys("abc@gmail.com")
	driver.find_element("id", "Password").send_keys('abc123')
	driver.find_element("xpath", '//input[@value="Log in"]').click()
	time.sleep(5)
