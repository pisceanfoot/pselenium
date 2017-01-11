# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement

from .common.driver import Driver
from .import drivername

import time
import re
import logging

logger = logging.getLogger(__name__)

class WebDriver(Driver):
	def __init__(self, name, *arg, **kwarg):
		super(WebDriver, self).__init__(name, *arg, **kwarg)

	def implicitly_wait(self, second):
		logger.debug('override implicitly_wait, sleep %s', second)
		self.__wait(second)

	def __wait(timeout):
	    timeout = float(timeout)
	    start = time()
	    while time() - start < timeout:
	        sleep(0.2)

