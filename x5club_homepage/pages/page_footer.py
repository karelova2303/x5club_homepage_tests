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

    def scroll_page_to_footer(self):
        self.footer.perform(command.js.scroll_into_view)

    def should_be_contact_us(self, value):
        with allure.step('Скроллим страницу вниз'):
            self.scroll_page_to_footer()
        with allure.step('Кликаем кнопку "Свяжитесь с нами"'):
            self.connect_with_us_button.click()
        with allure.step('Проверяем название попапа'):
            self.title_popup.should(have.exact_text(value))

    def should_be_clickable_vk(self):
        with allure.step('Скроллим страницу вниз'):
            self.scroll_page_to_footer()
        with allure.step('Проверяем кликабельность иконки "ВКонтакте"'):
            self.vk_icon.should(be.clickable)

    def should_be_clickable_telegram(self):
        with allure.step('Скроллим страницу вниз'):
            self.scroll_page_to_footer()
        with allure.step('Проверяем кликабельность иконки "Телеграм"'):
            self.t_icon.should(be.clickable)

    def should_be_clickable_dzen(self):
        with allure.step('Скроллим страницу вниз'):
            self.scroll_page_to_footer()
        with allure.step('Проверяем кликабельность иконки "Дзен"'):
            self.dzen_icon.should(be.clickable)

    def should_be_clickable_ok(self):
        with allure.step('Скроллим страницу вниз'):
            self.scroll_page_to_footer()
        with allure.step('Проверяем кликабельность иконки "Одноклассники"'):
            self.ok_icon.should(be.clickable)
