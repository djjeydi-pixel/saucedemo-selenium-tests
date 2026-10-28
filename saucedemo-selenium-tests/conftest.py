import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators.locators import LoginPage


@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации и закрытия браузера."""
    # Отключаем обнаружение автоматизации (защита от ботов)
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Инициализация драйвера
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver

    driver.quit()


@pytest.fixture
def authorized_driver(driver):
    """Фикстура для авторизации на сайте."""
    driver.find_element(*LoginPage.USERNAME_INPUT).send_keys("standard_user")
    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys("secret_sauce")
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()
    return driver