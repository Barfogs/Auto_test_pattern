from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.url, 'url имеет подстроку "login"'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Имеется форма авторизации'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Имеется форма регистрации'

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.EMAIL_INPUT), 'Имеется инпут регистрации  Email'
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT1), 'Имеется инпут регистрации Password'
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT1).send_keys(password)
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT2), 'Имеется инпут регистрации Password2'
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT2).send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), 'Имеется кнопка регистрации'
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

