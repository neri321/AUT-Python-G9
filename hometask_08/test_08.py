import pytest
from hometask_08.helper import select_radio_button, dict_of_radio_buttons


@pytest.mark.usefixtures('chrome')
class TestRadioButtons:

    def test_select_button_yes(self):
        driver = self.driver.get('https://demoqa.com/radio-button')
        select_radio_button(self.driver, name='Yes')

    def test_select_radio_button_impressive(self, element_input=None):
        driver = self.driver.get('https://demoqa.com/radio-button')
        select_radio_button(self.driver, name='Impressive')

    def test_select_button_no(self):
        driver = self.driver.get('https://demoqa.com/radio-button')
        select_radio_button(self.driver, name='No')

    def test_dict_of_radio_buttons(self):
        driver = self.driver.get('https://demoqa.com/radio-button')
        dict_of_radio_buttons(self.driver)
