from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.imdb.com/search/name/"

    def open(self):
        self.driver.get(self.url)

    def fill_search_form(self, name, birth_month, birth_day, birth_year):
        name_input = self.wait_for_element(By.ID, "name")
        name_input.send_keys(name)

        month_select = Select(self.wait_for_element(By.ID, "birth_month"))
        month_select.select_by_visible_text(birth_month)

        day_select = Select(self.wait_for_element(By.ID, "birth_day"))
        day_select.select_by_visible_text(birth_day)

        year_input = self.wait_for_element(By.ID, "birth_year")
        year_input.send_keys(birth_year)

    def submit_search(self):
        submit_button = self.wait_for_element(By.XPATH, "//button[contains(text(), 'Search')]")
        submit_button.click()
