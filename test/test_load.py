# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement
# import os
# cwd = os.getcwd()
# print(cwd)
# print(__file__)

from pselenium.driverfactory import DriverFactory



driver =  DriverFactory.create('Chrome')
driver.get('http://www.baidu.com')

driver.implicitly_wait(2)
driver.close()