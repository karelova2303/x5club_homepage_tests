import allure

from x5club_homepage.pages.page_footer import PageFooter

page_footer = PageFooter()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Проверка кликабельности кнопок и иконок в футере')
@allure.title('Отображения всплывающего окна при клике на кнопку "Свяжитесь с нами"')
@allure.link('https://x5club.ru')
def test_should_be_clickable_contact_us(setup_browser):
    page_footer.should_be_contact_us('Свяжитесь с нами')


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Проверка кликабельности кнопок и иконок в футере')
@allure.title('Кликабельность иконок социальных сетей: ВК, Телеграм, Дзен, Одноклассники')
@allure.link('https://x5club.ru')
def test_should_be_clickable_social_network_icon(setup_browser):
    page_footer.should_be_clickable_social_network_icon()
