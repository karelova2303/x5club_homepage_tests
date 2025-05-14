import allure

from x5club_homepage.pages.page_header import PageHeader

page_header = PageHeader()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Проверка кликабельности линков и кнопок в хедере')
@allure.title('Отображение контента при клике "О Х5 Клубе"')
@allure.link('https://x5club.ru')
def test_be_clickable_link_about(setup_browser):
    page_header.should_be_clickable_link_about()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Проверка кликабельности линков и кнопок в хедере')
@allure.title('Отображение контента при клике "Как стать участником"')
@allure.link('https://x5club.ru')
def test_be_clickable_link_participant(setup_browser):
    page_header.should_be_clickable_link_participant()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Проверка кликабельности линков и кнопок в хедере')
@allure.title('Отображение контента при клике "Партнеры"')
@allure.link('https://x5club.ru')
def test_be_clickable_link_partners(setup_browser):
    page_header.should_be_clickable_link_partners()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Проверка кликабельности линков и кнопок в хедере')
@allure.title('Отображение контента при клике "Мобильные приложения"')
@allure.link('https://x5club.ru')
def test_be_clickable_link_mobile_app(setup_browser):
    page_header.should_be_clickable_link_mobile_app()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Проверка кликабельности линков и кнопок в хедере')
@allure.title('Отображение контента при клике "Вопросы и ответы"')
@allure.link('https://x5club.ru')
def test_common_be_clickable_link_question(setup_browser):
    page_header.should_be_clickable_link_common_question()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Проверка кликабельности линков и кнопок в хедере')
@allure.title('Загрузка страницы авторизации при клике на кнопку "Войти"')
@allure.link('https://x5club.ru')
def test_be_clickable_login_button(setup_browser):
    page_header.should_be_clickable_login_button()
