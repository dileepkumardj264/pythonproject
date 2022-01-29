from homepage import HomePage
from excel_lib import read_locators


class LoginPage(HomePage):
    login_locators = read_locators('login_page')

    def login_enter_email(self, email):
        self.enter_text(self.login_locators['txt_email'], value=email)

    def login_enter_password(self, password):
        self.enter_text(self.login_locators['txt_password'], value=password)

    def login_click_login(self):
        self.click_element(self.login_locators['btn_login'])
