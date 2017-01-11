# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement

import re
from time import time, sleep

from .assertUtil import *

def wait(timeout):
    timeout = float(timeout)
    start = time()
    while time() - start < timeout:
        sleep(0.2)

def wait_for(func):
    """
    A decorator to invoke a function periodically until it returns a truthy
    value.
    """

    def wrapped(*args, **kwargs):
        timeout = kwargs.pop('timeout', 15)

        start = time()
        result = None

        while time() - start < timeout:
            result = func(*args, **kwargs)
            if result:
                break
            sleep(0.2)

        return result

    return wrapped

COMMAND_PATTERN = re.compile("(xpath|css|id|name|link|plink|tag|class)=(.*)$")
def find_element(browser, strValue):
    match = COMMAND_PATTERN.match(strValue)
    if match:
        typename = match.group(1)
        value = match.group(2)
    else:
        raise Exception('not support: %s' % strValue)

    element = None
    if typename == 'xpath':
        element = browser.find_element_by_xpath(value)
    elif typename == 'css':
        element = browser.find_element_by_css_selector(value)
    elif typename == 'id':
        element = browser.find_element_by_id(value)
    elif typename == 'name':
        element = browser.find_element_by_name(value)
    elif typename == 'link':
        element = browser.find_element_by_link_text(value)
    elif typename == 'plink':
        element = browser.find_element_by_partial_link_text(value)
    elif typename == 'tag':
        element = browser.find_element_by_tag_name(value)
    elif typename == 'class':
        element = browser.find_element_by_class_name(value)
    else:
        raise Exception('not support: %s' % strValue)

    return element
        
def get_log(browser):
    browserlogs = browser.get_log('browser')
    serverlogs = filter(lambda x: x['level'] == 'SEVERE', browserlogs)
    return serverlogs


