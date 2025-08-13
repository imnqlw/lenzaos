import allure
from web.home_page import mp


@allure.epic('test_check_language')
@allure.label("owner", 'imnqlw')
@allure.feature("Checking English language")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_check_language():
    mp.chose_language()
    mp.check_language()


@allure.epic('test_wrong_mail')
@allure.label("owner", "imnqlw")
@allure.feature("Checking mail")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_w_mail():
    mp.set_wrong_mail()
    mp.check_wrong_mail()


@allure.epic('test_valid_mail')
@allure.label("owner", "imnqlw")
@allure.feature("Checking mail")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_v_mail():
    mp.set_valid_mail()
    mp.check_valid_mail()


@allure.epic('set_wrong_code')
@allure.label("owner", "imnqlw")
@allure.feature("Checking code")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_w_code():
    mp.set_wrong_code()
    mp.check_wrong_code()


@allure.epic('set_code')
@allure.label("owner", "imnqlw")
@allure.feature("Checking code")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_set_success_code():
    mp.set_success_code()
    mp.check_success_code()

@allure.epic('create namescape')
@allure.label("owner", "imnqlw")
@allure.feature("Checking namespace")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_correct_namespace():
    mp.create_workspace_correct_name()
    mp.check_workspace_correct_name()

@allure.epic('create namescape')
@allure.label("owner", "imnqlw")
@allure.feature("Checking namespace")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_workspace_incorrect_name_with_symbol():
    mp.create_workspace_incorrect_name_with_symbol()
    mp.check_workspace_incorrect_name_with_symbol()

@allure.epic('test menu')
@allure.label("owner", "imnqlw")
@allure.feature("Checking button back")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_movie_back_workspace():
    mp.movie_back_workspace()
    mp.check_movie_back_workspace()

@allure.epic('Fill profile')
@allure.label("owner", "imnqlw")
@allure.feature("Checking name")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_fill_only_name():
    mp.fill_only_name()
    mp.check_fill_only_name()

@allure.epic('Fill profile')
@allure.label("owner", "imnqlw")
@allure.feature("Checking surname")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_fill_only_surname():
    mp.fill_only_surname()
    mp.check_fill_only_surname()

@allure.epic('Fill profile')
@allure.label("owner", "imnqlw")
@allure.feature("Checking photo")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_load_only_photo_png():
    mp.load_only_photo_png()
    mp.check_load_only_photo_png()

@allure.epic('Fill profile')
@allure.label("owner", "imnqlw")
@allure.feature("Checking photo")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_load_wrong_photo_f_gif():
    mp.load_wrong_photo_format_gif()
    mp.check_load_wrong_photo_format_gif()

@allure.epic('Fill profile')
@allure.label("owner", "imnqlw")
@allure.feature("Checking photo")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_load_wrong_photo_format_bmp():
    mp.load_wrong_photo_format_bmp()
    mp.check_load_wrong_photo_format_bmp()

@allure.epic('Fill profile')
@allure.label("owner", "imnqlw")
@allure.feature("Checking profile")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_fill_profile():
    mp.fill_profile()
    mp.check_fill_profile()

@allure.epic('Fill profile')
@allure.label("owner", "imnqlw")
@allure.feature("Checking data")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_fill_data_birthday():
    mp.fill_data_birthday()
    mp.check_fill_data_birthday()

@allure.epic('Fill profile')
@allure.label("owner", "imnqlw")
@allure.feature("Checking invite")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_invite_friend_wrong_email():
    mp.invite_friend_wrong_email()
    mp.check_invite_friend_wrong_email()

@allure.epic('Fill profile')
@allure.label("owner", "imnqlw")
@allure.feature("Checking invite")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_invite_friend_link():
    mp.invite_friend_link()
    mp.check_invite_friend_link()

@allure.epic('Fill profile')
@allure.label("owner", "imnqlw")
@allure.feature("Checking invite")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_invite_friend_later():
    mp.invite_friend_later()
    mp.check_invite_friend_later()

@allure.epic('Fill profile')
@allure.label("owner", "imnqlw")
@allure.feature("Checking invite")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_invite_friend_valid_mail():
    mp.invite_friend_valid_mail()
    mp.check_invite_friend_valid_mail()

@allure.epic('Check profile')
@allure.label("owner", "imnqlw")
@allure.feature("Check profile")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_check_profile():
    mp.select_profile()
    mp.check_profile()
