import pytest
from selenium import webdriver
from selene.support.shared import browser
from qa_guru_8.utils import attach
from qa_guru_8.utils.capabilities import selenoid_capabilities
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    options = Options()
    options.capabilities.update(selenoid_capabilities)
    browser.config.driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.base_url = 'https://demoqa.com'

    yield

    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    attach.add_logs(browser)

    browser.quit()
