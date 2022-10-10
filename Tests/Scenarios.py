import inspect

from selenium.webdriver.common.by import By

import Launch
import unittest
from Common import CommonFunctions as cf
from Common.Constant import Constant
from Common.Locators import Locators

class SmokeTest(Launch.Launch):

    def test_login_no_credentials(self):
        tst_scenario = str(inspect.stack()[0][3].lstrip('test_'))
        print('> Executing test case: ' + tst_scenario)
        # Wait for alert to be displayed and validate its text
        cf.wait_for_alert(self.driver)
        alert = self.driver.switch_to.alert
        alert_message = alert.text
        assert alert_message == 'Este sitio te pide que inicies sesión.'

        # Dismiss alert so authentication can be displayed, error 401
        alert.dismiss()
        cf.wait_for_element(self.driver, Locators.authentication_401_message)
        authorization_message = self.driver.find_element(By.XPATH, Locators.authentication_401_message).text
            # .find_element_by_xpath(Locators.authentication_401_message).text
        assert authorization_message == '401 Authorization Required'
        print('> End of scenario: ' + tst_scenario)
        print('----------------------------------')

    # def test_login_credentials(self):
    #     tst_scenario = str(inspect.stack()[0][3].lstrip('test_'))
    #     print('> Executing test case: ' + tst_scenario)
    #     # Wait for alert to be displayed so we can dismiss it
    #     # It's not possible to set values on alert as per open bug in webdriver
    #     # https://github.com/w3c/webdriver/issues/385
    #     cf.wait_for_alert(self.driver)
    #     alert = self.driver.switch_to.alert
    #     alert.dismiss()
    #     # Wait for 401 authentication error
    #     cf.wait_for_element(self.driver, Locators.authentication_401_message)
    #     # Use URL with authentication parameters, then visit URL again without authentication
    #     # This is a way to bypass the alert as per existing bug mentioned above
    #     self.driver.get(Constant.app_auth)
    #     self.driver.get(Constant.app)
    #     # Validate existence of some elements in the page
    #     cf.wait_for_element(self.driver, Locators.topbar_conduit_title)
    #     self.assertTrue(cf.does_element_exist_xpath(self.driver, Locators.topbar_conduit_title))
    #     self.assertTrue(cf.does_element_exist_xpath(self.driver, Locators.topbar_home_button))
    #     self.assertTrue(cf.does_element_exist_xpath(self.driver, Locators.topbar_sign_in_button))
    #     self.assertTrue(cf.does_element_exist_xpath(self.driver, Locators.topbar_sign_up_button))
    #     print('> End of scenario: ' + tst_scenario)
    #     print('----------------------------------')

    # def test_publish_article(self):
    #     tst_scenario = str(inspect.stack()[0][3].lstrip('test_'))
    #     print('> Executing test case: ' + tst_scenario)
    #     # Wait for alert to be displayed so we can dismiss it
    #     # It's not possible to set values on alert as per open bug in webdriver
    #     # https://github.com/w3c/webdriver/issues/385
    #     cf.wait_for_alert(self.driver)
    #     alert = self.driver.switch_to.alert
    #     alert.dismiss()
    #     # Wait for 401 authentication error
    #     cf.wait_for_element(self.driver, Locators.authentication_401_message)
    #     # Use URL with authentication parameters, then visit URL again without authentication
    #     # This is a way to bypass the alert as per existing bug mentioned above
    #     self.driver.get(Constant.app_auth)
    #     self.driver.get(Constant.app)
    #     # Sign in with a previously created user
    #     cf.click_on_element(self.driver, Locators.topbar_sign_in_button)
    #     cf.write_on_element(self.driver, Locators.signin_email, Constant.sign_in_user)
    #     cf.write_on_element(self.driver, Locators.signin_password, Constant.sign_in_pass)
    #     cf.click_on_element(self.driver, Locators.signin_button)
    #
    #     # Publish an article
    #     title = cf.generate_random_upper_string(10)
    #     about = cf.generate_random_lower_string(20)
    #     markdown = cf.generate_random_lower_string(50)
    #     tag = cf.generate_random_lower_string(5)
    #     cf.click_on_element(self.driver, Locators.topbar_new_article_button)
    #     cf.write_on_element(self.driver, Locators.new_article_title, title)
    #     cf.write_on_element(self.driver, Locators.new_article_about, about)
    #     cf.write_on_element(self.driver, Locators.new_article_markdown, markdown)
    #     cf.write_on_element(self.driver, Locators.new_article_tags, tag)
    #     cf.click_on_element(self.driver, Locators.new_article_publish_button)
    #
    #     # Validate article content
    #     cf.wait_for_element(self.driver, Locators.article_title)
    #     cf.wait_for_element(self.driver, Locators.article_content)
    #     assert self.driver.find_element_by_xpath(Locators.article_title).text == title
    #     assert self.driver.find_element_by_xpath(Locators.article_content).text == markdown
    #
    #     # Validate that article is published in the main page
    #     cf.click_on_element(self.driver, Locators.topbar_home_button)
    #     cf.click_on_element(self.driver, Locators.section_global_feed)
    #     assert self.driver.find_element_by_xpath(Locators.global_feed_article_preview_title).text == title
    #     assert self.driver.find_element_by_xpath(Locators.global_feed_article_preview_about).text == about
    #
    #     print('> End of scenario: ' + tst_scenario)
    #     print('----------------------------------')

    def test_sign_up_new_user(self):
        tst_scenario = str(inspect.stack()[0][3].lstrip('test_'))
        print('> Executing test case: ' + tst_scenario)
        # Wait for alert to be displayed so we can dismiss it
        # It's not possible to set values on alert as per open bug in webdriver
        # https://github.com/w3c/webdriver/issues/385
        cf.wait_for_alert(self.driver)
        alert = self.driver.switch_to.alert
        alert.dismiss()
        # Wait for 401 authentication error
        cf.wait_for_element(self.driver, Locators.authentication_401_message)
        # Use URL with authentication parameters, then visit URL again without authentication
        # This is a way to bypass the alert as per existing bug mentioned above
        self.driver.get(Constant.app_auth)
        self.driver.get(Constant.app)

        # Sign up to create new user
        random_user = cf.generate_random_lower_string(5)
        random_mail = random_user + '@testmail.com'
        password = '12345'
        cf.click_on_element(self.driver, Locators.topbar_sign_up_button)
        cf.write_on_element(self.driver, Locators.signup_user, random_user)
        cf.write_on_element(self.driver, Locators.signup_email, random_mail)
        cf.write_on_element(self.driver, Locators.signup_password, password)
        cf.click_on_element(self.driver, Locators.signup_button)

        # Go to user profile and validate username
        cf.click_on_element(self.driver, Locators.topbar_user_profile)
        cf.wait_for_element(self.driver, Locators.profile_username)
        assert self.driver.find_element_by_xpath(Locators.profile_username).text == random_user

        print('> End of scenario: ' + tst_scenario)
        print('----------------------------------')

if __name__ == '__main__':
    unittest.main()