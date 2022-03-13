from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import time

class ProductPage(BasePage):
    def push_adding_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.CART_BUTTON), 'Имеется кнопка добавления в корзину'
        cart_button = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        cart_button.click()

    def the_amounts(self):
        assert self.is_element_present(*ProductPageLocators.SUMM_CART), "Имеется сумма корзины"
        summ_cart = self.browser.find_element(*ProductPageLocators.SUMM_CART).text
        assert self.is_element_present(*ProductPageLocators.SUMM_PRODUCT), "Имеется стоимость продукта"
        summ_product = self.browser.find_element(*ProductPageLocators.SUMM_PRODUCT).text
        assert summ_cart in summ_product, "Сумма корзины равна стоимости продукта"
        print(summ_product)

    def name_product_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "Имеется наименование продукта"
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT_TO_CART), "Имеется наименование продукта"
        name_product_to_cart = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_TO_CART).text
        assert name_product == name_product_to_cart, 'Наименование товара в корзине соответствует добавленному товару'





