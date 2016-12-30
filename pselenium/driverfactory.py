# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement

from .selenium import selectDriver


class DriverFactory(object):

	@classmethod
	def create(cls, name):
		Driver =  selectDriver('Chrome')
		driver = Driver('/Users/leo/Documents/Workspace/dev/selenium/chromedriver')

		return driver

