from typing import List
import calendar
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class PageDatePicker:
    URL = 'https://demoqa.com/date-picker'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.select_date_input = (By.ID, 'datePickerMonthYearInput')

    def open(self):
        self.driver.get(self.URL)

    def set_date_directly(self, selected_date):
        date_input = self.open_date_picker()
        date_input.send_keys(Keys.CONTROL + 'A')
        date_input.send_keys(Keys.DELETE)
        date_input.send_keys(selected_date)
        date_input.send_keys(Keys.ENTER)
        pass

    def open_date_picker(self) -> WebElement:
        element = self.driver.find_element(*self.select_date_input)
        element.click()
        return element

    def selected_date_by_picker(self, selected_date) -> None:
        month = selected_date.split('/')[0]
        try:
            month = int(month)
        except ValueError:
            month = month
        day = selected_date.split('/')[1]
        year = selected_date.split('/')[2]
        try:
            month = int(month)
        except ValueError:
            month = month
        self.__set_date_by_picker(month=month, day=day, year=year)

    def __set_date_by_picker(self, month: int | str, day: int, year: int) -> None:
        self.open_date_picker()
        self.__set_month(month=month)
        self.__set_day(day=day)
        self.__set_year(year=year)

    def __set_month(self, month: int | str):
        locator = '//select[contains(@class, "month-select")]'
        element = self.driver.find_element(By.XPATH, locator)
        select = Select(element)
        if type(month) is int:
            select.select_by_index(month)
        elif type(month) is str:
            select.select_by_visible_text(month)
        else:
            raise TypeError(f'Month type should be int or str, but given {type(month)}')

    def __set_day(self, day: int):
        locator = '//div[contains(@aria-label, "{month}")][contains(@aria-label, "{day}")][contains(@aria-label, ' \
                  '"{year}")]'
        element = self.driver.find_element(By.XPATH, locator)
        pass

    def __set_year(self, year: int):
        locator = '//select[contains(@class, "year-select")]'
        element = self.driver.find_element(By.XPATH, locator)
        select = Select(element)
        pass

    def get_current_date(self):
        self.open_date_picker()
        locator = '//div[contains(@class, "today")]'
        current_date = self.driver.find_element(By.XPATH, locator).get_dom_attribute('aria-label').split(' ', 2)[2]
        return current_date

    def __set_date_by_picker_with_scrolling(self, month: int | str, day: int, year: int) -> None:
        pass

    def scroll_to_target_year(self, target_year: int):
        self.open_date_picker()
        button_locator_previous = (By.XPATH, '//button[contains(@class, "previous")]')
        button_locator_next = (By.XPATH, '//button[contains(@class, "next")]')
        prev_button = self.driver.find_element(*button_locator_previous)
        next_button = self.driver.find_element(*button_locator_next)

        if target_year >= self.get_current_year():
            while target_year >= self.get_current_year():
                next_button.click()
        elif target_year <= self.get_current_year():
            while target_year <= self.get_current_year():
                prev_button.click()

    def get_current_year(self) -> int:
        current_year_locator = (By.XPATH, '//div[@class="react-datepicker__header"]/div[contains(@class, "current")]')
        current_year = int(self.driver.find_element(*current_year_locator).text.split(' ')[1])
        return current_year

    def scroll_to_target_month(self, target_month: str):
        self.open_date_picker()
        button_locator_previous = (By.XPATH, '//button[contains(@class, "previous")]')
        button_locator_next = (By.XPATH, '//button[contains(@class, "next")]')
        prev_button = self.driver.find_element(*button_locator_previous)
        next_button = self.driver.find_element(*button_locator_next)
        if self.get_target_month(target_month) > self.get_current_month():
            while self.get_target_month(target_month) > self.get_current_month():
                next_button.click()
        elif self.get_target_month(target_month) < self.get_current_month():
            while self.get_target_month(target_month) < self.get_current_month():
                prev_button.click()

    def get_current_month(self) -> str:
        current_month_locator = (By.XPATH, '//div[@class="react-datepicker__header"]/div[contains(@class, "current")]')
        current_month = self.driver.find_element(*current_month_locator).text.split(' ')[0]
        return current_month

    @staticmethod
    def get_target_month(target_month: int | str) -> str:
        try:
            target_month = int(target_month)
            return calendar.month_name[int(target_month)]
        except ValueError:
            target_month = target_month
            return target_month


