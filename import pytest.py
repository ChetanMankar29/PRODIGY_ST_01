import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://the-internet.herokuapp.com/login"

VALID_USERNAME = "tomsmith"
VALID_PASSWORD = "SuperSecretPassword!"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()


# ---------------- POSITIVE TEST CASE ----------------
def test_login_valid_credentials(driver):
    driver.find_element(By.ID, "username").send_keys(VALID_USERNAME)
    driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in message


# ---------------- NEGATIVE TEST CASES ----------------
def test_login_invalid_credentials(driver):
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in message or "Your password is invalid!" in message


def test_login_empty_username(driver):
    driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in message


def test_login_empty_password(driver):
    driver.find_element(By.ID, "username").send_keys(VALID_USERNAME)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    message = driver.find_element(By.ID, "flash").text
    assert "Your password is invalid!" in message


def test_login_empty_fields(driver):
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in message
