from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, alert_is_present, \
    invisibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class _visibilty_of_element_located(visibility_of_element_located):

    def __call__(self, driver):
        displayed = super().__call__(driver)

        if isinstance(displayed, WebElement):
            return displayed.is_enabled()
        else:
            return False


def wait(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        locator = args[1]
        w = WebDriverWait(instance.driver, 20)
        v = _visibilty_of_element_located(locator)
        w.until(v)
        return func(*args, **kwargs)
    return wrapper
#
# def wait(visible=True, enable=True, is_alert=False):
#     def _wait(func):
#         def wrapper(*args, **kwargs):
#             instance = args[0]
#             locator = args[1]
#             w = WebDriverWait(instance.driver, 20)
#             if visible and enable:
#                 v = _visibilty_of_element_located(locator)
#             elif visible and not enable:
#                 v = _visibilty_of_element_located(locator)
#             elif is_alert:
#                 v = alert_is_present()
#             if not visible:
#                 v = invisibility_of_element_located(locator)
#             w.until(v)
#             return func(*args, **kwargs)
#         return wrapper
#     return _wait

