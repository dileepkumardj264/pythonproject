from homepage import HomePage
from excel_lib import read_locators


class RegistrationPage(HomePage):

    reg_locators = read_locators("registration_page")

    def registration_select_male(self):
        self.click_element(self.reg_locators['radio_gender_male'])

    def registration_select_female(self):
        self.click_element(self.reg_locators['radio_gender_female'])

    def registration_enter_first_name(self, fname):
        self.enter_text(self.reg_locators['txt_fname'], value=fname)

    def registration_enter_last_name(self, lname):
        self.enter_text(self.reg_locators['txt_lname'], value=lname)

    def registration_enter_email(self, email):
        self.enter_text(self.reg_locators['txt_email'], value=email)

    def registration_enter_password(self, password):
        self.enter_text(self.reg_locators['txt_password'], value=password)

    def registration_enter_confirm_password(self, password):
        self.enter_text(self.reg_locators['txt_confirm_password'], value=password)

    def registration_click_register(self):
        self.click_element(self.reg_locators['btn_register'])

