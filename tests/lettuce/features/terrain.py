from selenium import webdriver

class Tester(object):

    def __init__(self):
        self._browser = None

    def browser():
        doc = "A selenium browser"

        def fget(self):
            if self._browser is None:
                # self._browser = webdriver.Firefox()
                self._browser = webdriver.Chrome()
            return self._browser

        def fset(self, value):
            self._browser = value

        def fdel(self):
            self._browser.quit()
            del self._browser
        return locals()
    browser = property(**browser())

    def cleanup(self):
        del self.browser

    def browse(self, path):
        self.browser.get("http://localhost:5000/%s" % path)

    def click(self, text):
        try:
            element = self.browser.find_element_by_partial_link_text(text)
        except:
            raise AssertionError("Could not find anything to click on with label %s" % text)
        element.click()
        