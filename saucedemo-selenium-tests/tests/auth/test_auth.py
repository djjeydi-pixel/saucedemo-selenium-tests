import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import LoginPage


def test_invalid_login(driver):
    """Тест: Проверка появления ошибки при вводе неверных данных."""
    driver.find_element(*LoginPage.USERNAME_INPUT).send_keys("invalid_user")
    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys("wrong_password")
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()

    # Ожидаем появления сообщения об ошибке
    error_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LoginPage.ERROR_MESSAGE)
    )

    expected_text = "Epic sadface: Username and password do not match any user in this service"
    assert error_element.text == expected_text, "Текст ошибки не совпадает"