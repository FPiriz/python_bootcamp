#!/usr/bin/python

import re

# filename=unicode(raw_input('Enter file name: '))
filename = 'commands.txt'

try:
	f = open(filename, 'r')

	obtained = f.readline()
	dic = {}
	commands = 0

	while obtained != '':

		m = re.search(r'(?<=^switchport trunk allowed vlan )[\d,]+$', obtained)

		if (m):
			commands += 1
			vlans = set(m.group().split(','))
			for vlan in vlans:
				count = dic.get(vlan)
				if count:
					dic.update({vlan: count + 1})
				else:
					dic[vlan] = 1

		obtained = f.readline()

	p_list1 = []
	p_list2 = []

	for vlan, repetitions in dic.iteritems():
		if repetitions == commands:
			p_list1.append(int(vlan))
		elif repetitions == 1:
			p_list2.append(int(vlan))

	p_list1.sort(key=int)
	p_list2.sort(key=int)

	print 'List_1=[\'' + '\',\''.join(str(i) for i in p_list1) + '\']'
	print 'List_2=[\'' + '\',\''.join(str(i) for i in p_list2) + '\']'

	f.close()

except IOError:
	print "The file cannot be opened"
