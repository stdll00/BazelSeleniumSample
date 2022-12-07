import unittest
from testing.web import webtest  # gazelle:ignore testing.web
import urllib3 as _


class BrowserTest(unittest.TestCase):
    def setUp(self):
        self.driver = webtest.new_webdriver_session()

    def tearDown(self):
        try:
            self.driver.quit()
        finally:
            self.driver = None

    # Your tests here


if __name__ == "__main__":
    unittest.main()
