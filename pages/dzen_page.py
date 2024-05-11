import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urls import URLS


class DzenPage(BasePage):
    dzen_logo_in_header = (By.CLASS_NAME, 'desktop-base-header__logo-tA')

    @allure.step('Ожидание загрузки главной страницы "Дзен"')
    def loading_dzen_page(self):
        self.wait_for_visibility_of_element(self.dzen_logo_in_header)

    @allure.step('Проверка открытия страницы "Дзен"')
    def check_go_to_dzen(self):
        self.wait_for_visibility_of_element(self.dzen_logo_in_header)
        current_url = self.get_current_url()
        assert current_url == URLS.DZEN_URL