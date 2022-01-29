from time import sleep

from selenium.common.exceptions import NoSuchElementException

from project_wrapper import ProjectWrapper
from excel_lib import read_locators


class HomePage(ProjectWrapper):

    home_locators = read_locators('home_page')

    def homepage_click_login(self):
        self.click_element(self.home_locators['lnk_login'])

    def homepage_click_register(self):
        self.click_element(self.home_locators['lnk_register'])

    def is_user_logged_in(self, email):
        for _ in range(10):
            try:
                print(f'Trying to find element with link text {email}')
                return self.driver.find_element("xpath", f"//a[text()='{email}']").is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_login_error_displayed(self, message):
        _xpath = f"//span[text()='{message}']"
        for _ in range(5):
            try:
                return self.driver.find_element("xpath", _xpath).is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False
