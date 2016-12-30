# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement

print(__file__)
from pselenium.selenium import selectDriver



Driver =  selectDriver('Chrome')
driver = Driver('/Users/leo/Documents/Workspace/dev/selenium/chromedriver')
driver.get('http://www.baidu.com')

driver.implicitly_wait(2)
driver.close()