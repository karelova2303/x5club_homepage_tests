import allure

from x5club_homepage.pages.page_footer import PageFooter

page_footer = PageFooter()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.title('Проверка отображения попапа "Свяжитесь с нами" в футере')
@allure.link('https://x5club.ru')
def test_should_be_clickable_contact_us(open_homepage):
    page_footer.should_be_contact_us('Свяжитесь с нами')


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.title('Проверка кликабельности иконок соц. сетей в футере')
@allure.link('https://x5club.ru')
def test_should_be_clickable_social_network_icon(open_homepage):
    page_footer.should_be_clickable_vk()
    page_footer.should_be_clickable_telegram()
    page_footer.should_be_clickable_dzen()
    page_footer.should_be_clickable_ok()
