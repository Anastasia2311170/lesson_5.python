from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    # Найдите поле ввода с названием custname
    name_field = driver.find_element(By.ID, "custname")
    name_field.send_keys("Анастасия")

    driver.find_element(By.CSS_SELECTOR, ("[type='submit']")).click()

    assert driver.current_url == (
        "https://httpbin.qa-territory.online/forms/post/submitted"
    )

    driver.quit()
