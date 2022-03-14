from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def empty_cart_null(self):
        assert self.is_element_present(*BasketPageLocators.CONTENT_INNER), "Имеется уведомление о пустой корзине"
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Козина не имеет товаров"

    def empty_cart_full(self):
        assert self.is_not_element_present(*BasketPageLocators.CONTENT_INNER), "Уведомление о пустой корзине отсутствует"
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Козина имеет товары"
