# -*- coding: utf-8 -*-

print u'Hello World!'

# Git test in branch dev
for i in range(1,10):
    print u'%d^3 : %d' % (i, i*i*i)

# 分支管理策略--no-ff
sum = 1
for i in range(1,10):
    sum *= i
print u'sum(1,9)=', sum
