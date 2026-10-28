import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import InventoryPage, CartPage


@allure.suite("Корзина")
@allure.label("layer", "UI")
class TestCart:

    @allure.title("Очистка корзины после добавления товара")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_clear_cart(self, authorized_driver):
        driver = authorized_driver
        wait = WebDriverWait(driver, 5)

        with allure.step("Добавление товара в корзину"):
            wait.until(EC.element_to_be_clickable(InventoryPage.ADD_BACKPACK_BTN)).click()

        with allure.step("Переход в корзину"):
            driver.find_element(*InventoryPage.CART_LINK).click()

        with allure.step("Удаление товара из корзины"):
            wait.until(EC.element_to_be_clickable(CartPage.REMOVE_BACKPACK_BTN)).click()

        with allure.step("Проверка, что корзина пуста"):
            items = driver.find_elements(*CartPage.CART_ITEM)
            assert len(items) == 0, "Корзина не пуста!"

        with allure.step("Проверка возврата на страницу товаров"):
            driver.find_element(*CartPage.CONTINUE_SHOPPING_BTN).click()
            assert "inventory.html" in driver.current_url, "Не произошел возврат на страницу товаров"