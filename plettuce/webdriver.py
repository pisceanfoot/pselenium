# -*- coding: utf-8 -*-
# heavily inspiring or copy:) from https://github.com/pisceanfoot/lettuce_webdriver/blob/master/lettuce_webdriver/webdriver.py
from __future__ import absolute_import, division, print_function, with_statement

import logging
from lettuce import step, world
from selenium.webdriver.common.keys import Keys

from . import util
from .assertUtil import *
from . import screenshot

logger = logging.getLogger(__name__)

@util.wait_for
def wait_for_elem(browser, field_name):
    return util.find_element(world.browser, field_name)

@step(' open "(.*?)"$')
def ide_open(step, url):
    with AssertContextManager(step):
        world.browser.get(url)

@step(' click "(.*?)"$')
def ide_click(step, field_name):
    with AssertContextManager(step):
        element = util.find_element(world.browser, field_name)
        if isinstance(element, list):
            element[0].click()
        else:
            element.click()

@step(' wait\s+"([\d.]+?)s"$')
def ide_wait(step, second):
    util.wait(second)

@step(' waitcheck\s+"(.*?)" in "([\d.]+?)s"$')
def ide_check_visiable_util(step, field_name, timeout):
    timeout = float(timeout)

    with AssertContextManager(step):
        element = wait_for_elem(world.browser, field_name, timeout=timeout)
        if isinstance(element, list):
            element[0].is_displayed()
        else:
            element.is_displayed()

@step(' check\s+"(.*?)"$')
def ide_check_visiable(step, field_name):
    with AssertContextManager(step):
        element = util.find_element(world.browser, field_name)
        if isinstance(element, list):
            element[0].is_displayed()
        else:
            element.is_displayed()

@step(' checklog')
def ide_check_log(step):
    message = None
    serverlog = util.get_log(world.browser)
    logger.debug('browser console error log %s', serverlog)
    
    if serverlog:
        message = ','.join(str(e['message']) for e in serverlog)

    if message:
        screenshot.capture_screenshot(step)
    assert_true(step, not message, 'has error in browser console: %s' % message)

@step(' input "(.*?)" with "(.*?)"$')
def fill_in_textfield(step, field_name, value):
    logger.debug('field_name %s, value %s', field_name, value)

    with AssertContextManager(step):
        element = util.find_element(world.browser, field_name)

        assert_true(step, element,
                    'Can not find a field named "%s"' % field_name)            
        element.send_keys(value)


@step('current url is "(.*?)"$')
def url_should_be(step, url):
    assert_true(step, url == world.browser.current_url)

@step('current url contain "(.*?)"$')
def url_should_contain(step, url):
    assert_true(step, url in world.browser.current_url)


