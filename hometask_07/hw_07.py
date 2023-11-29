from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def test_button_color_changed(dyn_prop_page):
    driver = dyn_prop_page
    assert WebDriverWait(driver, 6).until(
        ec.text_to_be_present_in_element_attribute((By.XPATH, '//*[@id="colorChange"]'),
                                                   attribute_='class', text_="text-danger"))
    # assert that an attribute of the element is presented on the DOM.
