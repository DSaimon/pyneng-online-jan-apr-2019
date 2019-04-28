# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

a1=command1.split()
a2=command2.split()
b1=a1[-1].split(',')
b2=a2[-1].split(',')
c1=set(b1)
c2=set(b2)
uniq = c1 & c2
result= list(uniq)
result.sort()
print(result)