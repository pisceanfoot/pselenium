# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement

from .common.driver import Driver
from .import drivername

import time

class WebDriver(Driver):
	def __init__(self, name, *arg, **kwarg):
		super(WebDriver, self).__init__(name, *arg, **kwarg)

	def implicitly_wait(self, second):
		if(self.driver_name == drivername.CHROME):
			print('chrome not support implicitly_wait, will use sleep instead')
			time.sleep(second)
		else:
			super(WebDriver, self).implicitly_wait(second)


