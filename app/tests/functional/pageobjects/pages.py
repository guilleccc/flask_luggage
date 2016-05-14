from elements import (TicketElement, NameElement, BagCountElement, LocationElement, LoggedInByElement,
                      CloseTicketInitialsElement)
from locators import MainPageLocators, EditTicketPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class EditTicketPage(BasePage):
    close_ticket_initials = CloseTicketInitialsElement()

    def ask_for_initials(self):
        self.driver.find_element(*EditTicketPageLocators.STORE_BUTTON).click()

    def modify_ticket(self):
        self.driver.find_element(*EditTicketPageLocators.CLOSE_TICKET).click()


class MainPage(BasePage):
    ticket = TicketElement()
    name = NameElement()
    bag_count = BagCountElement()
    location = LocationElement()
    logged_in_by = LoggedInByElement()
    close_ticket_initials = CloseTicketInitialsElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Luggage" appears in page title"""
        return "Luggage" in self.driver.title

    def store_ticket(self):
        element = self.driver.find_element(*MainPageLocators.STORE_BUTTON)
        element.click()

    def has_stored_ticked(self, ticket_number):
        ticket_row = [
            value.format(ticket_number) if i == 1 else value
            for i, value in enumerate(MainPageLocators.TICKET_ROW)
        ]
        return self.driver.find_element(*ticket_row)

    def ask_for_initials(self, ticket_number):
        TICKET_ROW = self._get_formatted_locator(ticket_number, MainPageLocators.TICKET_ROW)
        TICKET_ACTION_BUTTON = self._get_formatted_locator(ticket_number, MainPageLocators.TICKET_ACTION_BUTTON)
        TICKET_COMPLETE_BUTTON = self._get_formatted_locator(ticket_number, MainPageLocators.TICKET_COMPLETE_BUTTON)

        self.driver.find_element(*TICKET_ROW)
        actions_element = self.driver.find_element(*TICKET_ACTION_BUTTON)
        actions_element.click()

        complete_button = self.driver.find_element(*TICKET_COMPLETE_BUTTON)
        complete_button.click()

    def modify_ticket_url(self, ticket_number):
        MODIFY_TICKET = self._get_formatted_locator(ticket_number, MainPageLocators.MODIFY_TICKET)
        modify_link = self.driver.find_element(*MODIFY_TICKET)

        return modify_link.get_attribute('href')

    def close_ticket(self):
        self.driver.find_element(*MainPageLocators.CLOSE_TICKET).click()

    @staticmethod
    def _get_formatted_locator(ticket_number, locator):
        return [
            value.format(ticket_number) if i == 1 else value
            for i, value in enumerate(locator)
        ]


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source