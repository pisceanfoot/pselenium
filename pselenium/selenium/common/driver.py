# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement

class Driver(object):
	def __init__(self, name, *arg, **kwarg):
		super(Driver, self).__init__(*arg, **kwarg)

		self.driver_name = name
		print('driver name:', self.driver_name)



