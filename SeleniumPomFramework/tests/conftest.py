import time

import pytest
from SeleniumPomFramework.base.BasePage import BaseClass
from SeleniumPomFramework.base.DriverClass import WebDriverClass


@pytest.fixture(scope='class')
def beforeClass(request):
    print("Before Class")
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver("Firefox")
    bp = BaseClass(driver)
    bp.launchWebPage("https://www.wikipedia.org/", "Wikipedia")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(1)
    driver.quit()
    print("After Class")

@pytest.fixture()
def beforeMethod():
    print("Before Method")
    yield
    print("After Method")
