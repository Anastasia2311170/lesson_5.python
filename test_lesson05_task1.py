from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")

    button_HTMLForm = driver.find_element(By.LINK_TEXT, "HTML Form")
    button_HTMLForm.click()

    assert driver.current_url == "https://httpbin.qa-territory.online/forms/post"

    driver.back()

    assert driver.current_url == "https://httpbin.qa-territory.online/"

    driver.quit()


test_navigation()
