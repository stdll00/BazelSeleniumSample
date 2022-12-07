import unittest
from testing.web import webtest  # gazelle:ignore testing.web
import urllib3 as _
from selenium.webdriver.remote.webdriver import WebDriver


class BrowserTest(unittest.TestCase):
    def setUp(self):
        self.driver: WebDriver = webtest.new_webdriver_session()

    def tearDown(self):
        try:
            self.driver.quit()
        finally:
            self.driver = None

    def test_sample_google_title(self):
        self.driver.get("https://google.com")
        if self.driver.title != "Google":
            raise ValueError("title seems invalid")


if __name__ == "__main__":
    unittest.main()
