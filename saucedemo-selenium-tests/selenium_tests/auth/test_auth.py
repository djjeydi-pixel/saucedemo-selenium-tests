import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import LoginPage


@allure.suite("Авторизация")
@allure.label("layer", "UI")
class TestAuth:

    @allure.title("Проверка ошибки при вводе неверных данных")
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_login(self, driver):
        with allure.step("Ввод некорректного логина и пароля"):
            driver.find_element(*LoginPage.USERNAME_INPUT).send_keys("invalid_user")
            driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys("wrong_password")

        with allure.step("Нажатие на кнопку 'Login'"):
            driver.find_element(*LoginPage.LOGIN_BUTTON).click()

        with allure.step("Проверка появления сообщения об ошибке"):
            error_element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(LoginPage.ERROR_MESSAGE)
            )
            expected_text = "Epic sadface: Username and password do not match any user in this service"
            assert error_element.text == expected_text, "Текст ошибки не совпадает"