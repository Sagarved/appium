import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

xpath_base = '//android.widget.LinearLayout[@content-desc="Numbers and basic operations"]/android.view.ViewGroup[1]/' \
             'android.widget.Button'
xpath_result ='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/' \
              'android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/' \
              'android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView'



class CalcTest(unittest.TestCase):
    """Test Class method"""
    @classmethod
    def setUpClass(self):
        desired_caps = {
            "deviceName": "emulator-5554",
            "platformName": "Android",
            "version": "10.0",
            "appPackage": "com.google.android.calculator",
            "appActivity": "com.android.calculator2.Calculator",
            #"realDevice": true
        }

        #Custom changes for devices
        desired_caps["deviceName"] = "HT8271A01820"

        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                    desired_capabilities=desired_caps)
        try:
            clear_screen = elm_id_click('clear', 3)  # Workaround for swipe
        except:
            pass

    """ sending value as text with object method"""

    def elm_id_click(self, locator, max_time=30):
        """Locate element and click"""
        elmid = WebDriverWait(self.driver, max_time).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, locator))
        )
        elmid.click()

    def elm_xpath_click(self, locator_xpath, max_time=30):
        """Locate element by Xpath and click"""
        elm_xpath = WebDriverWait(self.driver, max_time).until(
            EC.element_to_be_clickable((MobileBy.XPATH, locator_xpath)))
        elm_xpath.click()

    def elm_xpath(self, locator_xpath, max_time=30):
        """Locate element by Xpath"""
        #elm_xpath = self.driver.find_element_by_xpath(locator_xpath)
        elm_xpath = WebDriverWait(self.driver, max_time).until(
            EC.element_to_be_clickable((MobileBy.XPATH, locator_xpath)))
        return elm_xpath

    def test_mul(self):
        """4 multiply 5 and verifying result"""
        xpath_4 = xpath_base + '[4]'
        xpath_5 = xpath_base + '[5]'
        #time.sleep(2)
        number_4 = self.elm_xpath_click(xpath_4)
        select_AB = self.elm_id_click('multiply', 5)
        number_5 = self.elm_xpath_click(xpath_5)
        multi = self.elm_xpath(xpath_result)
        #print(sum.text)
        #time.sleep(5)
        result = self.elm_id_click('equals')

        self.assertEqual(multi.text, '20')

    def test_divide(self):
        """4 divide 2 and verifying result"""
        xpath_4 = xpath_base + '[4]'
        xpath_2 = xpath_base + '[8]'
        time.sleep(2) #First time launch calculator
        number_4 = self.elm_xpath_click(xpath_4)
        select_AB = self.elm_id_click('divide', 5)
        number_5 = self.elm_xpath_click(xpath_2)
        remainder = self.elm_xpath(xpath_result)
        result = self.elm_id_click('equals')
        self.assertEqual(remainder.text, '2')

    def test_sum(self):
        """4 sum 2 and verifying result"""
        xpath_4 = xpath_base + '[4]'
        xpath_2 = xpath_base + '[8]'
        #time.sleep(2)
        number_4 = self.elm_xpath_click(xpath_4)
        select_AB = self.elm_id_click('plus', 5)
        number_5 = self.elm_xpath_click(xpath_2)
        sum = self.elm_xpath(xpath_result)
        result = self.elm_id_click('equals')
        self.assertEqual(sum.text, '6')

    def test_minus(self):
        """4 minus 2 and verifying result"""
        xpath_4 = xpath_base + '[4]'
        xpath_2 = xpath_base + '[8]'
        #time.sleep(2)
        number_4 = self.elm_xpath_click(xpath_4)
        select_AB = self.elm_id_click('minus', 5)
        number_5 = self.elm_xpath_click(xpath_2)
        minus = self.elm_xpath(xpath_result)
        result = self.elm_id_click('equals')
        self.assertEqual(minus.text, '2')
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()