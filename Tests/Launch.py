import unittest
from selenium import webdriver
from Common.Constant import Constant

class Launch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = Constant.driver_location)
        self.driver.set_window_size(Constant.screen_width, Constant.screen_height)
        self.driver.get(Constant.app)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()