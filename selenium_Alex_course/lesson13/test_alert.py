"=================Allert==================="
from .page_alert import BasePage, url
from .locators import AlertPage


def test_alert(browser):
    page = BasePage(browser, url)
    page.open_page()
    page.click_button_to_see_alert()
    page.click_alert_after_5_seconds()




