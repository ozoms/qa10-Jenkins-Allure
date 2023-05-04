import pytest
from selenium import webdriver
from selene.support.shared import browser
from qa_guru_8.utils import attach
from qa_guru_8.utils.capabilities import capabilities


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.driver = webdriver.Remote(
        command_executor="https://user1:1234@elenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities
    )

    browser.config.base_url = 'https://demoqa.com'

    yield

    attach.add_screenshot()
    attach.add_html()
    attach.add_video()
    attach.add_logs()

    browser.quit()
