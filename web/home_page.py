import allure
from selene import browser, have, be, by, command
import time


class MainPage:

    def open(self):
        browser.open('')


    @allure.step("Выбор языка")
    def chose_language(self):
        browser.open("/")
        browser.element('[class="content"]').click()
        browser.element("//div[contains(@class, 'context-menu__option') and .//span[text()='English (США)']]").click()

    def check_language(self):
        browser.element('[class="content"]').should(have.text('English'))

    @allure.step("Неверный адрес электронной почты")
    def set_wrong_mail(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('почта@.ru').press_tab()

    @allure.step("Проверка почты")
    def check_wrong_mail(self):
        browser.element(".form-field__error.no-select").should(have.text('Неверный адрес электронной почты'))

    @allure.step("Верный адрес электронной почты")
    def set_valid_mail(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()

    @allure.step("Проверка верного адреса почты")
    def check_valid_mail(self):
        browser.element('.hdi_title').should(have.text('Проверьте почту'))


    @allure.step("Неверный код от почты")
    def put_wrong_code(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('664555')

    @allure.step("Код введен неправильно")
    def check_wrong_code(self):
        browser.element('.cd_code__error').should(have.text('Код введен неправильно'))

    @allure.step("Верный код от почты")
    def set_success_code(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')

    @allure.step("Проверка кода от почты")
    def check_success_code(self):
        browser.element('.hdi_title.hdi_title_nodescription').wait_until(
            have.text('Похоже, вы еще не используете Lenza'))

    @allure.step("Создание пространства")
    def create_workspace_correct_name(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        browser.element('#domain-company').type('name_21_24')
        time.sleep(1)
        browser.element("//span[@class='btn__title']").click()

    @allure.step("Проверка пространства")
    def check_workspace_correct_name(self):
        browser.element(".pr_profile").should(have.text('Настройка личного профиля'))

    @allure.step("Неверное имя для пространства")
    def create_workspace_incorrect_name(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        browser.element('#domain-company').type('te')

    @allure.step("Проверка ошибки неверного имя")
    def check_workspace_incorrect_name(self):
        browser.element(".form-field__error").should(have.text('Имя домена не может быть короче 3-х символов'))

    @allure.step("Запрещенные символы для пространства")
    def create_workspace_incorrect_name_with_symbol(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt1@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        browser.element('#domain-company').type('***')

    @allure.step("Проверка ошибки на запрещенные символы для пространства")
    def check_workspace_incorrect_name_with_symbol(self):
        browser.element(".form-field__error").should(have.text('Разрешены латинские буквы и символы aA-zZ, 0-9, -, _'))

    @allure.step("Шаг назад в меню")
    def movie_back_workspace(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt2@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        browser.element(".d_domain__back-link").click()

    @allure.step("Проверка шага назад в меню")
    def check_movie_back_workspace(self):
        browser.element('.hdi_title.hdi_title_nodescription').wait_until(
            have.text('Похоже, вы еще не используете Lenza'))

    @allure.step("Заполняем только имя")
    def fill_only_name(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        browser.element(by.text("Мне понятно. Вперед!")).click()
        browser.element("//input[@placeholder='Введите имя']").type('Имя')

    @allure.step("Проверка на заполнение обязательных полей")
    def check_fill_only_name(self):
        browser.element("#rcaec']").should(be.disabled)

    @allure.step("Заполняем только фамилия")
    def fill_only_surname(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        browser.element(by.text("Мне понятно. Вперед!")).click()
        browser.element("//input[@placeholder='Введите фамилию']").type('Фамилия')

    @allure.step("Проверка на заполнение обязательных полей")
    def check_fill_only_surname(self):
        browser.element("#rcaec']").should(be.disabled)

    @allure.step("Загружаем фото")
    def load_only_photo_png(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        browser.element(by.text("Мне понятно. Вперед!")).click()
        browser.element(".avatar__img-upload-input").send_keys('pages/ava.png')
        time.sleep(1)

    @allure.step("Проверяем загрузку фото")
    def check_load_only_photo_png(self):
        browser.element("#rcaec']").should(be.disabled)

    @allure.step("Заполняем фото форматом гиф")
    def load_wrong_photo_format_gif(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        browser.element(by.text("Мне понятно. Вперед!")).click()
        browser.element(".avatar__img-upload-input").send_keys('pages/ava.gif')
        time.sleep(1)

    @allure.step("Заполняем фото форматом гиф")
    def check_load_wrong_photo_format_gif(self):
        browser.element(".pr_profile__avatar_btn").should(have.text('Добавить фотографию'))

    @allure.step("Заполняем фото форматом бмп")
    def load_wrong_photo_format_bmp(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        browser.element(by.text("Мне понятно. Вперед!")).click()
        browser.element(".avatar__img-upload-input").send_keys('E:\\proect\\lenzaos\pages\\ava.bmp')
        time.sleep(1)
    @allure.step('Проверка ошибки')
    def check_load_wrong_photo_format_bmp(self):    
        browser.element(".pr_profile__avatar_btn").should(have.text('Добавить фотографию'))

    @allure.step("Заполняем поле имя и фамилия")
    def fill_profile(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        browser.element(by.text("Мне понятно. Вперед!")).click()
        browser.element("//input[@placeholder='Введите имя']").type('Имя')
        browser.element("//input[@placeholder='Введите фамилию']").type('Фамилия')

    @allure.step("Проверка заполнения обязательных полей")
    def check_fill_profile(self):    
        browser.element("#rcaec']").wait_until(be.enabled)

    @allure.step("Заполняем день рождение")
    def fill_data_birthday(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        browser.element(by.text("Мне понятно. Вперед!")).click()
        browser.element("//input[@placeholder='Введите имя']").type('Имя')
        browser.element("//input[@placeholder='Введите фамилию']").type('Фамилия')
        browser.element("//span[@class='btn__title']").should(be.visible).click()
        browser.element("//input[@value='1']").click()
        browser.element(by.text("2")).click()
        browser.element("//input[@value='Январь']").click()
        browser.element(by.text("Март")).click()
        browser.element("//input[@value='1999']").click()
        browser.element(by.text('1995')).perform(command.js.scroll_into_view)
        browser.element(by.text('1995')).click()

    @allure.step("Проверка даты рождения")
    def check_fill_data_birthday(self): 
        browser.element("//div[contains(@class, 'small-day') and .//span[text()='День']]//input").should(
            have.value("2"))
        browser.element("//div[contains(@class, 'middle-day')]//input").should(have.value("Март"))
        browser.element("//div[contains(@class, 'small-day')][.//span[text()='Год']]//input").should(have.value("1995"))


    @allure.step("Заполняем поле приглашение")
    def invite_friend_wrong_email(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt3@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        browser.element('#domain-company').type('name_21_333')
        time.sleep(1)
        browser.element("//span[@class='btn__title']").click()
        browser.element("//input[@placeholder='Введите имя']").type('Имя')
        browser.element("//input[@placeholder='Введите фамилию']").type('Фамилия')
        browser.element("#0psox").wait_until(be.not_.disabled)
        browser.element(by.text("Продолжить")).click()
        browser.element("//input[@value='1']").click()
        browser.element(by.text("2")).click()
        browser.element("//input[@value='Январь']").click()
        browser.element(by.text("Март")).click()
        browser.element("//input[@value='1999']").click()
        browser.element(by.text('1995')).perform(command.js.scroll_into_view).click()
        browser.element("//button[.//span[text()='Продолжить']]").should(be.clickable).click()
        browser.element("//input[@id='tags-row-input']").type("почта").press_enter()
        browser.element(".tag__remove-icon").click()

    @allure.step("Проверяем поле приглашение")
    def check_invite_friend_wrong_email(self):
        browser.element("//input[@id='tags-row-input']").should(have.text(""))

    @allure.step("Копируем ссылку на приглашение")
    def invite_friend_link(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt4@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        browser.element('#domain-company').type('name_21_343')
        time.sleep(1)
        browser.element("//span[@class='btn__title']").click()
        browser.element("//input[@placeholder='Введите имя']").type('Имя')
        browser.element("//input[@placeholder='Введите фамилию']").type('Фамилия')
        browser.element("#0psox").wait_until(be.not_.disabled)
        browser.element(by.text("Продолжить")).click()
        browser.element("//input[@value='1']").click()
        browser.element(by.text("2")).click()
        browser.element("//input[@value='Январь']").click()
        browser.element(by.text("Март")).click()
        browser.element("//input[@value='1999']").click()
        browser.element(by.text('1995')).perform(command.js.scroll_into_view).click()
        browser.element("//button[.//span[text()='Продолжить']]").should(be.clickable).click()
        browser.element('.cp_copy').click()

    @allure.step("Проверяем ссылку на приглашение")
    def check_invite_friend_link(self):
        browser.element(".cp_popup").should(
            have.text("Ссылка скопирована. Теперь вы можете поделиться ей и с другими!"))

    @allure.step("Приглашаем друзей пойзже")
    def invite_friend_later(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt5@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        browser.element('#domain-company').type('name_21_36')
        time.sleep(1)
        browser.element("//span[@class='btn__title']").click()
        browser.element("//input[@placeholder='Введите имя']").type('Имя')
        browser.element("//input[@placeholder='Введите фамилию']").type('Фамилия')
        browser.element("#0psox").wait_until(be.not_.disabled)
        browser.element(by.text("Продолжить")).click()
        browser.element("//input[@value='1']").click()
        browser.element(by.text("2")).click()
        browser.element("//input[@value='Январь']").click()
        browser.element(by.text("Март")).click()
        browser.element("//input[@value='1999']").click()
        browser.element(by.text('1995')).perform(command.js.scroll_into_view).click()
        browser.element("//button[.//span[text()='Продолжить']]").should(be.clickable).click()
        browser.element(".inu_invite__link_skip").click()

    @allure.step("Проверка перехода пойзже")
    def check_invite_friend_later(self):
        browser.element(".component-dialog-title-title-text").should(have.text('Видео для владельцев и админов'))

    @allure.step("Создаем приглашение")
    def invite_friend_valid_mail(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt7@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        browser.element('#domain-company').type('name_21_48')
        time.sleep(1)
        browser.element("//span[@class='btn__title']").click()
        browser.element("//input[@placeholder='Введите имя']").type('Имя')
        browser.element("//input[@placeholder='Введите фамилию']").type('Фамилия')
        browser.element("#0psox").wait_until(be.not_.disabled)
        browser.element(by.text("Продолжить")).click()
        browser.element("//input[@value='1']").click()
        browser.element(by.text("2")).click()
        browser.element("//input[@value='Январь']").click()
        browser.element(by.text("Март")).click()
        browser.element("//input[@value='1999']").click()
        browser.element(by.text('1995')).perform(command.js.scroll_into_view).click()
        browser.element("//button[.//span[text()='Продолжить']]").should(be.clickable).click()
        browser.element("//input[@id='tags-row-input']").type("example@mail.com").press_enter()
        browser.element("//button[contains(@class, 'inu_invite__buttons_send')]").click()

    @allure.step("Проверяем приглашение")
    def check_invite_friend_valid_mail(self):
        browser.element("//p[contains(@class, 'text-size-dialog-title')]").should(
            have.exact_text("Приглашение отправлено"))

    @allure.step("Выбираем свой профиль")
    def select_profile(self):
        browser.open('/')
        browser.element('[class="button-ui btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('#email-input').type('tt7@test.com').click()
        browser.element('[class="btn btn--full-width with-border btn--lg no-select"]').click()
        browser.element('[class="code-input__field focus-shadow code-input__field--current"]').type('666555')
        browser.element('[class="list-item__info-wrapper"]').click()
        time.sleep(4)
        browser.element("#close-view").click()
        browser.element("//button[contains(@class, 'profile-button__menu-item-trigger')]").click()
        browser.element(by.text('OK')).click()
        browser.element('.list-item__info-text').click()

    @allure.step("Проверка профиля")
    def check_profile(self):
        browser.element(".component-dialog-title-title-text").should(have.text('Имя Фамилия'))


mp = MainPage()
