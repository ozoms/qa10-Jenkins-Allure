from selene import have, command
from selene.support.shared import browser
from qa_guru_8.model.controls import datepicker, radio, checkbox, dropdown
from qa_guru_8.utils import resource


def open():
    browser.open('/automation-practice-form')


def window_size():
    browser.driver.set_window_size(1920, 1080)

'''
def ad_skip():
    browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
        have.size_greater_than_or_equal(3)
    )
    browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
'''


def type_name(name):
    browser.element('#firstName').type(name)


def type_surname(surname):
    browser.element('#lastName').type(surname)


def select_gender(text):
    radio.select_by_value('[name=gender]', text)


def select_birthday(month, year, day):
    datepicker.select('#dateOfBirthInput', month, year, day)


def type_subjects(text):
    browser.element('#subjectsInput').type(text).press_enter()


def type_phone(number):
    browser.element('#userNumber').type(number)


def type_email(email):
    browser.element('#userEmail').type(email)


def select_hobby(text):
    checkbox.select('[for^=hobbies-checkbox]', text)


def type_address(address):
    browser.element('#currentAddress').type(address)


def select_picture(name_file):
    resource.path('#uploadPicture', name_file)


def select_region(text):
    dropdown.select_option('#react-select-3-input', text)


def select_city(text):
    dropdown.select_option('#react-select-4-input', text)


def submit_enter():
    browser.element('#submit').press_enter()


def assert_form(text):
    browser.element('.table').all('td').even.should(
        have.exact_texts(text)
    )
