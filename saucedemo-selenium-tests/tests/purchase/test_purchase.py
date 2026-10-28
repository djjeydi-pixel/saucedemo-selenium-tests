from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import InventoryPage, CartPage, CheckoutPage


def test_successful_purchase(authorized_driver):
    """Тест: Сквозной сценарий успешной покупки."""
    driver = authorized_driver
    wait = WebDriverWait(driver, 5)

    # Добавляем товар и идем в корзину
    wait.until(EC.element_to_be_clickable(InventoryPage.ADD_BACKPACK_BTN)).click()
    driver.find_element(*InventoryPage.CART_LINK).click()

    # Оформляем заказ
    wait.until(EC.element_to_be_clickable(CartPage.CHECKOUT_BTN)).click()

    # Заполняем поля
    driver.find_element(*CheckoutPage.FIRST_NAME_INPUT).send_keys("Ivan")
    driver.find_element(*CheckoutPage.LAST_NAME_INPUT).send_keys("Ivanov")
    driver.find_element(*CheckoutPage.ZIP_CODE_INPUT).send_keys("123456")
    driver.find_element(*CheckoutPage.CONTINUE_BTN).click()

    # Завершаем покупку
    wait.until(EC.element_to_be_clickable(CheckoutPage.FINISH_BTN)).click()

    # Проверяем успешное завершение
    complete_header = wait.until(EC.visibility_of_element_located(CheckoutPage.COMPLETE_HEADER))
    assert complete_header.text == "Thank you for your order!", "Покупка не была завершена успешно"