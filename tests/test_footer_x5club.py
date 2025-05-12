import allure

from x5club_homepage.pages.page_footer import PageFooter

page_footer = PageFooter()

@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.feature('Проверка отображения попапа "Свяжитесь с нами" в футере')
@allure.link('https://x5club.ru')
def test_should_be_clickable_contact_us(open_homepage):
    page_footer.should_be_contact_us('Свяжитесь с нами')

@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.feature('Проверка кликабельности иконок соц. сетей в футере')
@allure.link('https://x5club.ru')
def test_should_be_clickable_social_network_icon(open_homepage):
    with allure.step('Проверяем кликабельность иконки "ВКонтакте"'):
        page_footer.should_be_clickable_vk()
    with allure.step('Проверяем кликабельность иконки "Телеграмм"'):
        page_footer.should_be_clickable_telegram()
    with allure.step('Проверяем кликабельность иконки "Дзен"'):
        page_footer.should_be_clickable_dzen()
    with allure.step('Проверяем кликабельность иконки "Одноклассники"'):
        page_footer.should_be_clickable_ok()