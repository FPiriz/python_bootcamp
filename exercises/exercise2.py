#!/usr/bin/python

import re

# filename=unicode(raw_input('Enter file name: '))
filename = 'commands.txt'

try:
	# open the file
	f = open(filename, 'r')
	# initialise variables
	obtained = f.readline()
	dic = {}
	commands = 0
	
	#read until end of file
	while obtained != '':
		
		m = re.search(r'(?<=^switchport trunk allowed vlan )[\d,]+$', obtained)
		# if the line begins with the "switchport...", process it
		if (m):
			commands += 1
			vlans = set(m.group().split(','))
			# count number of ocurrences of a vlan
			for vlan in vlans:
				count = dic.get(vlan)
				if count:
					dic.update({vlan: count + 1})
				else:
					dic[vlan] = 1

		obtained = f.readline()

	# initialise variables
	p_list1 = []
	p_list2 = []

	# get repeated and uniques vlans
	for vlan, repetitions in dic.iteritems():
		if repetitions == commands:
			p_list1.append(int(vlan))
		elif repetitions == 1:
			p_list2.append(int(vlan))
	# sort the list
	p_list1.sort(key=int)
	p_list2.sort(key=int)

	# print the list
	print 'List_1=[\'' + '\',\''.join(str(i) for i in p_list1) + '\']'
	print 'List_2=[\'' + '\',\''.join(str(i) for i in p_list2) + '\']'

	f.close()

except IOError:
	print "The file cannot be opened"
