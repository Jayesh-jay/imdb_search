import pytest
from pages.search_page import SearchPage


@pytest.mark.usefixtures("setup")
class TestIMDBSearch:
    def test_search_actor(self):
        search_page = SearchPage(self.driver)
        search_page.open()
        search_page.fill_search_form(name="Tom Hanks", birth_month="July", birth_day="9", birth_year="1956")
        search_page.submit_search()
        # Additional assertions can be added here to validate search results
