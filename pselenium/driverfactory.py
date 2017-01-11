# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement

from .selenium import selectDriver
from .selenium import drivername
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging

logger = logging.getLogger(__name__)

def create(name, *arg, **kwarg):
	if 'command_executor' in kwarg:
		logger.debug('select remote driver for %s', name)

		command_executor = kwarg.pop('command_executor')
		Driver =  selectDriver(drivername.REMOTE)
		if 'desired_capabilities' in kwarg:
			capability = kwarg.pop('desired_capabilities')
		else:
			capability = getattr(DesiredCapabilities, name.upper()).copy()

		driver = Driver(command_executor = command_executor, desired_capabilities = capability, *arg, **kwarg)
	else:
		logger.debug('select %s driver', name)

		Driver =  selectDriver(name)
		driver = Driver(*arg, **kwarg)

	return driver

