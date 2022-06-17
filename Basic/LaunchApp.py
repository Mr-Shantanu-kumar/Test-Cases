import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


# Appium1 points to http://127.0.0.1:4723/wd/hub by default

class AppiumTest(unittest.TestCase):

    def setUp(self):
        print("Setup")
        options = UiAutomator2Options()
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
        self.wait = WebDriverWait(self.driver, 10)

        try:
            element = self.wait.until(ec.presence_of_element_located((AppiumBy.ID, "com.ATG.World:id/getStartedTv")))
        except:
            print("Already Logged in!")
            return

        getStartedButton = self.driver.find_element(AppiumBy.ID, "com.ATG.World:id/getStartedTv")
        getStartedButton.click()

        print("login")
        time.sleep(1)
        signinButton = self.driver.find_element(AppiumBy.ID, "com.ATG.World:id/login_email")
        signinButton.click()

        time.sleep(1)
        emailBox = self.driver.find_element(AppiumBy.ID, "com.ATG.World:id/email_phone_login")
        emailBox.send_keys("hello@atg.world")
        continueButton = self.driver.find_element(AppiumBy.ID, "com.ATG.World:id/signinbutton")
        continueButton.click()

        time.sleep(1)
        passwordBox = self.driver.find_element(AppiumBy.ID, "com.ATG.World:id/password")
        passwordBox.send_keys("Pass@123")
        loginButton = self.driver.find_element(AppiumBy.ID, "com.ATG.World:id/passwordloginbutton")
        loginButton.click()
        time.sleep(1)

    def testpostPhoto(self):
        try:
            element = self.wait.until(ec.presence_of_element_located((AppiumBy.ID, "com.ATG.World:id/fab")))
        except:
            print("Check app connection!")
        finally:
            print(element)

        print("Photo test")
        detailsIcon = self.driver.find_element(AppiumBy.ID, "com.ATG.World:id/fab")
        detailsIcon.click()
        time.sleep(1)

        imageIcon = self.driver.find_element(AppiumBy.ID, "com.ATG.World:id/image_fab_clicked")
        imageIcon.click()
        time.sleep(1)

        nextButton = self.driver.find_element(AppiumBy.ID, "com.ATG.World:id/toolbar_post_action")
        nextButton.click()
        time.sleep(1)

        caption = self.driver.find_element(AppiumBy.ID, "com.ATG.World:id/caption_edit_text")
        caption.send_keys("new new post")
        postButton = self.driver.find_element(AppiumBy.ID, "com.ATG.World:id/toolbar_post_action")
        postButton.click()
        time.sleep(1)
        print("Posted")

        try:
            element = self.wait.until(
                ec.presence_of_element_located((AppiumBy.ID, "com.ATG.World:id/selection_done_btn")))
        except:
            print("Check Internet or increase wait!")
        finally:
            print(element)

        doneButton = self.driver.find_element(AppiumBy.ID, "com.ATG.World:id/selection_done_btn")
        doneButton.click()

        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



