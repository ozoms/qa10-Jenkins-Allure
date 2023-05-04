from selene import have
from selene.support.shared import browser


def select_option(selector, text):
    browser.element(selector).type(text).press_enter()
    '''
    browser.element(selector).click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text(text)
    ).type(text).press_enter()
    '''
    #browser.element('#react-select-3-input').type(text).press_enter()
    #browser.element('#react-select-4-input').type('Noida').press_enter()