from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"Download and installed an App. Add number A and B, verify result"

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

driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities=desired_caps)

# inputA = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputA"))
# )
"""This code wait implicitly for locator load and then create object"""
# inputA.send_keys("10")
""" sending value as text with object method"""
def elm_id_click(locator, max_time=30):
    "Locate element and click"
    elmid = WebDriverWait(driver, max_time).until(
             EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, locator))
        )
    elmid.click()
def elm_xpath_click(locator_xpath):
    "Locate element by Xpath and click"
    elm_xpath = driver.find_element_by_xpath(locator_xpath)
    elm_xpath.click()

def elm_xpath(locator_xpath):
    "Locate element by Xpath"
    elm_xpath = driver.find_element_by_xpath(locator_xpath)
    return elm_xpath

"""4 multiply 5 and verifying result"""
try:
    clear_screen = elm_id_click('clear', 3)# Workaround for swipe
except:
    pass
digit_pre_text = 'com.google.android.calculator:id/digit_4'
xpath_base = '//android.widget.LinearLayout[@content-desc="Numbers and basic operations"]/android.view.ViewGroup[1]/android.widget.Button'
xpath_4 = xpath_base + '[4]'
xpath_5 = xpath_base + '[5]'
number_4 = elm_xpath_click(xpath_4)
select_AB = elm_id_click('multiply', 5)
number_5 = elm_xpath_click(xpath_5)
#result = elm_id_click('equals')
xpath_result ='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView'

sum = elm_xpath(xpath_result)
print(sum.text)
if sum.text == '20':
    assert True
else:
    assert False
driver.quit()