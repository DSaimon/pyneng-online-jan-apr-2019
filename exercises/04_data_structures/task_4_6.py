# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

r=ospf_route.split()

#print(r)


template = '''
Protocol:             OSPF
Prefix:               {net}
AD/Metric:            {metric}
Next-Hop:             {ip_hop}
Last update:          {time}
Outbound Interface:   {int}
'''

print(template.format(net=r[1], metric=r[2].strip('[]'), ip_hop=r[4].rstrip(','), time=r[5].rstrip(','), int=r[6]))
