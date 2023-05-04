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
        command_executor="https://user1:1234@elenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.base_url = 'https://demoqa.com'

    yield

    attach.add_screenshot()
    attach.add_html()
    attach.add_video()
    attach.add_logs()

    browser.quit()
