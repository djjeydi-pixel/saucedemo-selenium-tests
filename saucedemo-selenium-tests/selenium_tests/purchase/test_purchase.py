import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import InventoryPage, CartPage, CheckoutPage


@allure.suite("Покупка")
@allure.label("layer", "E2E")
class TestPurchase:

    @allure.title("Успешное оформление заказа")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_successful_purchase(self, authorized_driver):
        driver = authorized_driver
        wait = WebDriverWait(driver, 5)

        with allure.step("Добавление товара в корзину"):
            wait.until(EC.element_to_be_clickable(InventoryPage.ADD_BACKPACK_BTN)).click()
            driver.find_element(*InventoryPage.CART_LINK).click()

        with allure.step("Переход к оформлению заказа"):
            wait.until(EC.element_to_be_clickable(CartPage.CHECKOUT_BTN)).click()

        with allure.step("Заполнение формы доставки"):
            driver.find_element(*CheckoutPage.FIRST_NAME_INPUT).send_keys("Ivan")
            driver.find_element(*CheckoutPage.LAST_NAME_INPUT).send_keys("Ivanov")
            driver.find_element(*CheckoutPage.ZIP_CODE_INPUT).send_keys("123456")
            driver.find_element(*CheckoutPage.CONTINUE_BTN).click()

        with allure.step("Завершение покупки"):
            wait.until(EC.element_to_be_clickable(CheckoutPage.FINISH_BTN)).click()

        with allure.step("Проверка успешного завершения заказа"):
            complete_header = wait.until(EC.visibility_of_element_located(CheckoutPage.COMPLETE_HEADER))
            assert complete_header.text == "Thank you for your order!", "Покупка не была завершена успешно"