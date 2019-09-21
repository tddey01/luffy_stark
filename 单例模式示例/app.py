#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

import utils
# print(utils.site) #<utils.AdminSite object at 0x1017928d0>
utils.site.name = 'kn'
import  commons



'''
在python中，如果已经倒入过的文件再次重新导入时候，python不会在解释一遍，而是选择从内存中直接将原来导入的值拿过来用，
'''