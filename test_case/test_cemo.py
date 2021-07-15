from utils.server import Server
from base.base_page import BasePage
from base.base_driver import Driver


class TestDemo:
    def setup(self):

        app = Server().main()
        self.driver = Driver().android_driver()
        self.base_page = BasePage()

    def teardown(self):
        pass

    def test_demo(self):
        self.base_page.find_and_click('xpath', '//*[@text="Video"]')
