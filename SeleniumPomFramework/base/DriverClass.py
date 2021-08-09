from selenium import webdriver
import SeleniumPomFramework.utilities.CustomLogger as cl

class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName.lower() == "chrome":
            driver = webdriver.Chrome("C:/Users/YT/Downloads/pythonProject/SeleniumPython/Driver/chromedriver.exe")
            self.log.info("Chrome Driver is initializing")
        elif browserName.lower() == "safari":
            driver = webdriver.Safari()
            self.log.info("Safari Driver is initializing")
        elif browserName.lower() == "firefox":
            driver = webdriver.Firefox(executable_path="C:/Users/YT/Downloads/pythonProject/SeleniumPython/Driver/geckodriver.exe")
            self.log.info("FireFox Driver is initializing")

        return driver
