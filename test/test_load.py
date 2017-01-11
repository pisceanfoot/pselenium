# -*- coding: utf-8 -*-
# from __future__ import absolute_import, division, print_function, with_statement
# import os
# cwd = os.getcwd()
# print(cwd)
# print(__file__)

# import sys
# import time
# sys.path.insert(0, '/Users/leo/Documents/Workspace/dev/pselenium')


# from pselenium import driverfactory



# driver =  driverfactory.create('Chrome')
# driver.get('https://www.baidu.com/')
# # time.sleep(4)
# driver.implicitly_wait(4)
# print(driver.log_types)
# browserlogs = driver.get_log('browser')
# serverlogs = filter(lambda x: x['level'] == 'SEVERE', browserlogs)
# print(serverlogs)
# assert not serverlogs
# # print(driver.get_log('client'))
# # print(driver.get_log('driver'))
# # print(driver.get_log('server'))
# driver.close()

def a(*arg, **kwarg):
	print arg
	print kwarg

a(a=1)

