from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import InventoryPage, CartPage


def test_clear_cart(authorized_driver):
    """Тест: Добавление товара и очистка корзины."""
    driver = authorized_driver

    # Добавляем товар
    driver.find_element(*InventoryPage.ADD_BACKPACK_BTN).click()
    driver.find_element(*InventoryPage.CART_LINK).click()

    # Удаляем товар
    wait = WebDriverWait(driver, 5)
    wait.until(EC.element_to_be_clickable(CartPage.REMOVE_BACKPACK_BTN)).click()

    # Проверяем, что корзина пуста (элементов нет)
    items = driver.find_elements(*CartPage.CART_ITEM)
    assert len(items) == 0, "Корзина не пуста!"

    # Проверяем возврат на страницу товаров
    driver.find_element(*CartPage.CONTINUE_SHOPPING_BTN).click()
    assert "inventory.html" in driver.current_url, "Не произошел возврат на страницу товаров"