import allure
from allure_commons.types import Severity
from qa_guru_8.model.pages import practice_form


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_student_registration_form():
    with allure.step('Открываем главную страницу'):
        practice_form.open()
        practice_form.window_size()
        #practice_form.ad_skip()

    # WHEN
    with allure.step('Открываем главную страницу'):
        practice_form.type_name('Sasha')
        practice_form.type_surname('Sol')
    with allure.step('Открываем главную страницу'):
        practice_form.type_email('name@example.com')
    with allure.step('Открываем главную страницу'):
        practice_form.select_gender('Male')
    with allure.step('Открываем главную страницу'):
        practice_form.type_phone('1234567891')
    with allure.step('Открываем главную страницу'):
        practice_form.select_birthday('May', '1980', '11')
    with allure.step('Открываем главную страницу'):
        practice_form.type_subjects('Computer Science')
    with allure.step('Открываем главную страницу'):
        practice_form.select_hobby('Music')
    with allure.step('Открываем главную страницу'):
        practice_form.type_address('Mira 1')
    with allure.step('Открываем главную страницу'):
        practice_form.select_picture('foto.jpg')
    with allure.step('Открываем главную страницу'):
        practice_form.select_region('NCR')
        practice_form.select_city('Delhi')
    with allure.step('Открываем главную страницу'):
        practice_form.submit_enter()

    # THEN
    with allure.step('Открываем главную страницу'):
        practice_form.assert_form(
                (
                'Sasha Sol',
                'name@example.com',
                'Male',
                '1234567891',
                '11 May,1980',
                'Computer Science',
                'Music',
                'foto.jpg',
                'Mira 1',
                'NCR Delhi',
                )
        )
