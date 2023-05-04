from selene import have
from selene.support.shared import browser


def select(selector, text):
    browser.all(selector).element_by(have.text(text)).click()
