"=================Allert==================="
import time

from .page_alert import BasePage, url


def test_alert(browser):
    page = BasePage(browser, url)
    page.open_page()
    # page.click_button_to_see_alert()
    # page.click_alert_after_5_seconds()
    # page.confirm_box_wll_appear()
    page.prompt_box_will_appear()
    time.sleep(2)
