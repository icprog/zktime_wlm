# -*- coding: utf-8 -*-

menus = (
         ('att_simulate',u'模拟操作', 'grup_alarm'),
#         ('att_report',u'报表数据', 'grup_info'),
         )

####### 自定义视图 #########


import routes

from mole.const import TEMPLATE_PATH
TEMPLATE_PATH.append('./apps/att/templates/')