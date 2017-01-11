# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement

from .selenium import selectDriver



def create(name, *arg, **kwarg):
	Driver =  selectDriver(name)
	driver = Driver(*arg, **kwarg)

	return driver

