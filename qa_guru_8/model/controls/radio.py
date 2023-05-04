from selene.support.shared import browser
from selene import have


def select_by_value(selector, text):
    browser.all(selector).element_by(have.value(text)).element('..').click()