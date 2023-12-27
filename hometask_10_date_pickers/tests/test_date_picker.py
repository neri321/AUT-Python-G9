from time import sleep

from hometask_10_date_pickers.pages.page_date_picker import PageDatePicker


class TestDatePicker:

    def test_select_date(self, chrome):
        target_date = "9/19/2019"
        # target_date = 'August/19/2025'
        page = PageDatePicker(driver=chrome)
        page.open()
        # page.set_date_directly(target_date)
        # assert page.get_date() == target_date
        # pass
        # date = '11/19/2023'
        # page.selected_date_by_picker(date)
        # page.selected_date_by_picker('January/15/2023')

        target_year = int(target_date.split('/')[-1])
        target_month = target_date.split('/')[0]
        page.scroll_to_target_year(target_year)
        page.scroll_to_target_month(target_month)
        sleep(5)
        # print(page.get_target_month(target_month))

        # page.scroll_to_target_day(target_day)
        pass

    def test_get_current_date(self, chrome):
        page = PageDatePicker(driver=chrome)
        page.open()
        page.get_current_date()
        print(page.get_current_date())


