import allure

from x5club_homepage.pages.page_header import PageHeader

page_header = PageHeader()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.title('Проверка работы линка "О Х5 Клубе" в хедере')
@allure.link('https://x5club.ru')
def test_be_clickable_link_about(open_homepage):
    page_header.should_be_clickable_link_about()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.title('Проверка работы линка "Как стать участником"  в хедере')
@allure.link('https://x5club.ru')
def test_be_clickable_link_participant(open_homepage):
    page_header.should_be_clickable_link_participant()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.title('Проверка работы линка "Партнеры"  в хедере')
@allure.link('https://x5club.ru')
def test_be_clickable_link_partners(open_homepage):
    page_header.should_be_clickable_link_partners()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.title('Проверка работы линка "Мобильные приложения"  в хедере')
@allure.link('https://x5club.ru')
def test_be_clickable_link_mobile_app(open_homepage):
    page_header.should_be_clickable_link_mobile_app()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.title('Проверка работы линка "Вопросы и ответы"  в хедере')
@allure.link('https://x5club.ru')
def test_common_be_clickable_link_question(open_homepage):
    page_header.should_be_clickable_link_common_question()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.title('Проверка работы кнопки "Войти"  в хедере')
@allure.link('https://x5club.ru')
def test_be_clickable_login_button(open_homepage):
    page_header.should_be_clickable_login_button()
