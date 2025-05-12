import allure
from selene import browser, be, have


class PageHeader():
    def __init__(self):
        self.link_about = browser.element('[href="#about"]')
        self.about_content_card = browser.element('#about')

        self.link_participant = browser.element('[href="#participant"]')
        self.participant_content_card = browser.element('#participant')

        self.link_partners = browser.element('[href="/partners"]')
        self.partners_content_card = browser.element('#root')

        self.link_mobile_app = browser.element('[href="#mobile-app"]')
        self.mobile_app_content_card = browser.element('#mobile-app')

        self.link_common_question = browser.element('[href="#common-question"]')
        self.common_question_content_card = browser.element('#common-question')

        self.login_button = browser.element('[data-testid="loginButton"]')
        self.form_login = browser.element('#kc-form-login')

    def should_be_clickable_link_about(self):
        with allure.step('Кликаем линк "О Х5 Клубе"'):
            self.link_about.click()
        with allure.step('Проверяем отображение контента "О Х5 Клубе"'):
            self.about_content_card.should(be.visible)

    def should_be_clickable_link_participant(self):
        with allure.step('Кликаем линк "Как стать участником"'):
            self.link_participant.click()
        with allure.step('Проверяем отображение контента "Как стать участником"'):
            self.participant_content_card.should(be.visible)

    def should_be_clickable_link_partners(self):
        with allure.step('Кликаем линк "Партнеры"'):
            self.link_partners.click()
        with allure.step('Проверяем отображение контента "Партнеры"'):
            self.partners_content_card.should(be.visible)

    def should_be_clickable_link_mobile_app(self):
        with allure.step('Кликаем линк "Мобильные приложения"'):
            self.link_mobile_app.click()
        with allure.step('Проверяем отображение контента "Мобильные приложения"'):
            self.mobile_app_content_card.should(be.visible)

    def should_be_clickable_link_common_question(self):
        with allure.step('Кликаем линк "Вопросы и ответы"'):
            self.link_common_question.click()
        with allure.step('Проверяем отображение контента "Вопросы и ответы"'):
            self.common_question_content_card.should(be.visible)

    def should_be_clickable_login_button(self):
        with allure.step('Кликаем кнопку "Войти"'):
            self.login_button.click()
        with allure.step('Проверяем открытие страницы авторизации'):
            self.form_login.should(be.visible)
