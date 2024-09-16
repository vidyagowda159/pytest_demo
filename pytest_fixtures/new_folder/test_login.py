
def test_login(driver_init):
	driver = driver_init

	driver.find_element("link text", "Log in").click()
	driver.find_element("id", "Email").send_keys("abc@gmail.com")
	driver.find_element("id", "Password").send_keys('abc123')
	driver.find_element("xpath", '//input[@value="Log in"]').click()