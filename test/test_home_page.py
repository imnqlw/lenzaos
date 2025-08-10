from selene import browser, have, be, by, command
import time

from selene.support.conditions.be import clickable


def test_chose_language():
    browser.open("/")
    browser.element('[class="content"]').click()
    browser.element("//div[contains(@class, 'context-menu__option') and .//span[text()='English (США)']]").click()
    browser.element('[class="content"]').should(have.text('English'))


def test_input_unvalid_mail():
    browser.open('/')
    browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
    browser.element('#email-input').type('почта@.ru').press_tab()
    browser.element(".form-field__error.no-select").should(have.text('Неверный адрес электронной почты'))

def test_input_valid_mail():
    browser.open('/')
    browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
    browser.element('#email-input').type('dd@test.com').click()
    browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
    browser.element('.hdi_title').should(have.text('Проверьте почту'))

def test_wrong_code():
    browser.open('/')
    browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
    browser.element('#email-input').type('dd1@test.com').click()
    browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
    browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('664555')
    browser.element('.cd_code__error').should(have.text('Код введен неправильно'))

def test_success_code():
    browser.open('/')
    browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
    browser.element('#email-input').type('dd@test.com').click()
    browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
    browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
    browser.element('.hdi_title.hdi_title_nodescription').wait_until(have.text('Похоже, вы еще не используете Lenza'))

def test_create_workspace_correct_name():
    browser.open('/')
    browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
    browser.element('#email-input').type('dd8@test.com').click()
    browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
    browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
    browser.element('[class="list-item__info-wrapper"]').click()
    browser.element('#domain-company').type('test_name_23')
    time.sleep(1)
    browser.element("//span[@class='btn__title']").click()
    browser.element(".pr_profile").should(have.text('Настройка личного профиля'))

def test_create_workspace_incorrect_name():
    browser.open('/')
    browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
    browser.element('#email-input').type('dd9@test.com').click()
    browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
    browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
    browser.element('[class="list-item__info-wrapper"]').click()
    browser.element('#domain-company').type('te')
    browser.element(".form-field__error").should(have.text('Имя домена не может быть короче 3-х символов'))

def test_create_workspace_incorrect_name_with_symbol():
    browser.open('/')
    browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
    browser.element('#email-input').type('dd9@test.com').click()
    browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
    browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
    browser.element('[class="list-item__info-wrapper"]').click()
    browser.element('#domain-company').type('***')
    browser.element(".form-field__error").should(have.text('Разрешены латинские буквы и символы aA-zZ, 0-9, -, _'))

def test_movie_back_workspace():
    browser.open('/')
    browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
    browser.element('#email-input').type('dde1@test.com').click()
    browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
    browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
    browser.element('[class="list-item__info-wrapper"]').click()
    browser.element(".d_domain__back-link").click()
    browser.element('.hdi_title.hdi_title_nodescription').wait_until(have.text('Похоже, вы еще не используете Lenza'))



