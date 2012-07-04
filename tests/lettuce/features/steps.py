from lettuce import *
from terrain import Tester
from nose.tools import assert_equals
import pdb

tester = Tester()


@after.all
def cleanup(total):
    tester.cleanup()


@step("I navigate to the front page$")
def navigate(step):
    tester.browse('')


@step('I click on the "([^"]*)" link$')
def click_link(step, link):
    tester.click(link)


@step('I am on the "([^"]*)" page')
def verify_page(step, title):
    assert_equals(tester.browser.title, title)


@step('I enter "([^"]*)" in the ([^"]*) ([^"]*) field')
def type_in_field(step, text, qualifier, type):
    element = tester.browser.find_element_by_xpath("//input")
    pdb.set_trace()
    element.send_keys(text)