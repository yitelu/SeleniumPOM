import unittest
import pytest
import time
from SeleniumPomFramework.pages.EnterTextPage import EnterText

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class EnterTextTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.et = EnterText(self.driver)

    @pytest.mark.run(order=1)
    def test_enterDataInEditBox(self):
        self.driver.maximize_window()
        time.sleep(2)
        self.et.enterText()
        self.et.clickOnSubmitButton()
        time.sleep(3)

    # @pytest.mark.run(order=2)
    # def test_clickOnSubmitButton(self):


