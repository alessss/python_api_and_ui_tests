import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config
from api.client import BetApiClient


@pytest.fixture
def api_client() -> BetApiClient:
    #Fresh API client per test, scoped to the default test user.
    return BetApiClient()


@pytest.fixture(autouse=True)
def reset_balance(api_client: BetApiClient):
    response = api_client.reset_balance()
    assert response.status_code == 200, (
        f"Pre-test balance reset failed with status {response.status_code}: {response.text}"
    )
    yield


@pytest.fixture
def driver():
    #Selenium Chrome WebDriver, function-scoped so each UI test gets a clean browser.
    options = Options()
    options.add_argument("--window-size=1440,900")

    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(config.IMPLICIT_WAIT_SECONDS)

    yield chrome_driver

    chrome_driver.quit()