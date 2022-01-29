from selenium.webdriver.support.select import Select
from wait_ import wait


class ProjectWrapper:

    def __init__(self, driver):
        self.driver = driver

    @wait
    def click_element(self, locator: tuple) -> None:
        self.driver.find_element(*locator).click()

    @wait
    def enter_text(self, locator: tuple, value: str) -> None:
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def select_item(self, locator: tuple, item: str) -> None:
        list_ = self.driver.find_element(*locator)
        s = Select(list_)
        if isinstance(item, str):
            s.select_by_visible_text(item)
        else:
            s.select_by_index(item)

    @wait
    def select_items(self, locator: tuple, items: list) -> None:
        for item in items:
            self.select_item(locator, item)

    # @wait(is_alert=True, visible=False, enable=False)
    # def accept_alert(self):
    #     self.driver.switch_to_alert.accept()
    #
    # @wait(is_alert=True, visible=False, enable=False)
    # def get_alert_text(self):
    #     return self.driver.switch_to_alert.text

