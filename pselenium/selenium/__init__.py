# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement

import sys
from .webdriver import WebDriver
from . import drivername

def selectDriver(name):
	print('start')
	if(name not in [drivername.CHROME]):
		raise Exception('unknow webdriver name %s', name)

	webDriverModule = __import__('selenium.webdriver', fromlist=[name])
	baseDriver = getattr(webDriverModule, name)

	class PSeleniumDriver(WebDriver, baseDriver):
		def __init__(self, *arg, **kwarg):
			super(PSeleniumDriver, self).__init__(name, *arg, **kwarg)
		pass

	return PSeleniumDriver


__all__ = ['selectDriver']
__version__ = '1.0.0'