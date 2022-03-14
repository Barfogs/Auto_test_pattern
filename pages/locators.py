from selenium.webdriver.common.by import By
from selenium import webdriver

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_INPUT = (By.ID, "id_registration-email")
    PASSWORD_INPUT1 = (By.ID, "id_registration-password1")
    PASSWORD_INPUT2 = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUMM_CART = (By.CSS_SELECTOR, ".icon-shopping-cart")
    SUMM_PRODUCT = (By.CLASS_NAME, "price_color")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    NAME_PRODUCT_TO_CART = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CLASS_NAME, "btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    CONTENT_INNER = (By.ID, "content_inner")
    BASKET_ITEMS = (By.ID, "basket-items")