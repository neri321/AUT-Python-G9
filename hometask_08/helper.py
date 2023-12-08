from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec


def select_radio_button(driver: WebDriver, name: str) -> object:
    locator = f'//label[text()="{name}"]//ancestor::div[contains(@class,"radio")]'
    label_ = f'{locator}/label'
    input_ = f'{locator}/input'
    element_label = driver.find_element(By.XPATH, label_)
    element_input = driver.find_element(By.XPATH, input_)
    driver.execute_script('arguments[0].removeAttribute("disabled");', element_input)
    if not element_input.is_selected():
        element_label.click()
    assert element_input.is_selected()
    assert ec.text_to_be_present_in_element_attribute((By.CLASS_NAME, "mt-3"), attribute_="class", text_="{name}")


def dict_of_radio_buttons(driver: WebDriver):
    dict = {}
    locator = '//div[contains(@class,"radio")]'
    lst_of_buttons = driver.find_elements(By.XPATH, locator)
    for div in lst_of_buttons:
        button_name = div.text
        radio_button_locator = f'//label[text()="{button_name}"]//ancestor::div[contains(@class,"radio")]'
        fnd_radio_button = driver.find_element(By.XPATH, radio_button_locator)
        radio_button_enabled = fnd_radio_button.is_enabled()
        radio_button_selected = fnd_radio_button.is_selected()
        dict[button_name] = {'enabled': radio_button_enabled, 'selected': radio_button_selected}

    print(dict)
