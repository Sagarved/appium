import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


"""
Web browser on mobile phone can tested by CSS and Xpath only.As through CSS all
Element can be access of web browser ID, Class, Name method are not supported in W3C standard.
link: https://github.com/appium/appium/issues/13306
1: Moreover for capability follow browser name and automation name
link: http://appium.io/docs/en/writing-running-appium/web/mobile-web/
2: Download and points to chromedriver for running web browser test
Links:http://appium.io/docs/en/commands/interactions/actions/
      http://appium.io/docs/en/writing-running-appium/caps/
"""
class BrowserTest(unittest.TestCase):
    """Test Class method"""
    @classmethod
    def setUpClass(self):
        desired_caps = {
            "deviceName": "emulator-5554",
            "platformName": "Android",
            "version": "10.0",
            'automationName': 'UIAutomator2',
            'browserName': 'Chrome',
            'chromedriverExecutable': 'C:\\Users\\door4\\Documents\\library\\chromedriver_win32\\chromedriver.exe'
            #"realDevice": true
        }

        #Custom changes for devices
        desired_caps["deviceName"] = "HT8271A01820"

        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                    desired_capabilities=desired_caps)


    def elm_css(self, locator, max_time=10):
        elm_css = WebDriverWait(self.driver, max_time).until(
            EC.element_to_be_clickable((MobileBy.CSS_SELECTOR, locator)))
        elm_css.click()


    def test_launch_lynda(self):
        """ Launch Lynda and verify it launched"""
        self.driver.get('https://www.lynda.com')
        self.assertEqual(self.driver.title,'Lynda: Online Courses, Classes, Training, Tutorials')

    def test_search_catalog(self):
        """search through catalog"""
        wait_d = WebDriverWait(self.driver,10)

        self.driver.find_element_by_css_selector("button#toggle-search").click()
        elm_in = self.driver.find_element_by_css_selector("input.autocomplete").clear()
        elm_in.send_keys("pytorch")
        time.sleep(5)



    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()