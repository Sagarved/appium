from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"Download and installed an App. Add number A and B, verify result"

desired_caps = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "version" : "10.0",
    "app": "https://testingbot.com/appium/sample.apk",
    #"realDevice": true
}

#Custom changes for devices
#desired_caps["deviceName"] = "HT8271A01820"

driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities=desired_caps)

inputA = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputA"))
)
inputA.send_keys("10")

inputB = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputB"))
)
inputB.send_keys("5")

sum = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "sum"))
)

if sum!=None and sum.text=="15":
  assert True
else:
  assert False

driver.quit()