import allure
from selene import browser, have, command, be


class PageFooter():
    def __init__(self):
        self.footer = browser.element('footer')

        self.connect_with_us_button = self.footer.element('button')
        self.title_popup = browser.element('.tp-h2-medium')

        self.vk_icon = browser.element('[href="https://vk.com/x5club"]')
        self.t_icon = browser.element('[href="https://t.me/x5clubru"]')
        self.dzen_icon = browser.element('[href="https://dzen.ru/x5club"]')
        self.ok_icon = browser.element('[href="https://ok.ru/group/70000002639516"]')

    def open_homepage(self):
        browser.open('/')

    def scroll_page_to_footer(self):
        self.footer.perform(command.js.scroll_into_view)

    def should_be_contact_us(self, value):
        with allure.step('Открываем Главную страницу'):
            self.open_homepage()
        with allure.step('Скроллим страницу вниз'):
            self.scroll_page_to_footer()
        with allure.step('Кликаем кнопку "Свяжитесь с нами"'):
            self.connect_with_us_button.click()
        with allure.step('Проверяем название всплывающего окна'):
            self.title_popup.should(have.exact_text(value))

    def should_be_clickable_social_network_icon(self):
        with allure.step('Открываем Главную страницу'):
            self.open_homepage()
        with allure.step('Скроллим страницу вниз'):
            self.scroll_page_to_footer()
        with allure.step('Иконка "ВКонтакте" кликабельна'):
            self.vk_icon.should(be.clickable)
        with allure.step('Иконка "Телеграм" кликабельна'):
            self.t_icon.should(be.clickable)
        with allure.step('Иконка "Дзен" кликабельная'):
            self.dzen_icon.should(be.clickable)
        with allure.step('Иконка "Одноклассники" кликабельна'):
            self.ok_icon.should(be.clickable)
