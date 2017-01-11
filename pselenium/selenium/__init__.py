# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement

from .webdriver import WebDriver
from . import drivername
import logging

logger = logging.getLogger(__name__)

def selectDriver(name):
	logger.debug('select driver')

	if(name not in [drivername.CHROME, drivername.FIREFOX, drivername.REMOTE]):
		logger.critical('driver name "%s" current not support', name)
		raise Exception('unknow webdriver name %s', name)

	logger.info('use drivername %s', name)

	webDriverModule = __import__('selenium.webdriver', fromlist=[name])
	baseDriver = getattr(webDriverModule, name)

	class PSeleniumDriver(WebDriver, baseDriver):
		def __init__(self, *arg, **kwarg):
			super(PSeleniumDriver, self).__init__(name, *arg, **kwarg)
		pass

	return PSeleniumDriver


__all__ = ['selectDriver']
__version__ = '1.0.0'
