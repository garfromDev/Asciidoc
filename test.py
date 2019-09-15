# -*- coding: utf-8 -*-
from operator import itemgetter

s = [(333, 1, '2019-05-05'),
     (222, 15, '1018-09-30'),
     (999, 15, '2019-02-25'),
     ]
p = sorted(s, key=lambda x: itemgetter(2))
p.sort(key=lambda x: itemgetter(1))
print(s)