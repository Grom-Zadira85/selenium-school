from selenium.webdriver.common.by import By


class AlertPage():
    Click_Button_To_See_Alert = (By.CSS_SELECTOR, '[id="alertButton"]')
    After_5_seconds = (By.CSS_SELECTOR, '[id="timerAlertButton"]')
    Confirm_Box_Will_Appear = (By.CSS_SELECTOR, '[id="confirmButton"]')
    Prompt_Box_Will_Appear = (By.CSS_SELECTOR, '[id="promtButton"]')
