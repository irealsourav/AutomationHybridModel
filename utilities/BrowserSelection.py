from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class BrowserSelection(object):

    def __init__(self,browser):
        self.browser=browser


    def get_browser(self):
        if self.browser == "chrome":
            return webdriver.Chrome(executable_path=ChromeDriverManager().install())
        if self.browser == "firefox":
            return webdriver.firefox(executable_path=GeckoDriverManager().install())