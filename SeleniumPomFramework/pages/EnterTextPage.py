from SeleniumPomFramework.base.BasePage import BaseClass
import SeleniumPomFramework.utilities.CustomLogger as cl


class EnterText(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # elements in the page
    _enterTextEditBox = "searchInput"  # id
    _submitButton = ".pure-button"  # css

    # def clickOnLocatorsPage(self):
    #     self.clickOnElement(self._locatorsPage,"link")

    def enterText(self):
        self.sendText("Selenium",self._enterTextEditBox,"id")
        cl.allureLogs("Entered Text in Edit Box")

    def clickOnSubmitButton(self):
        self.clickOnElement(self._submitButton,"css")
