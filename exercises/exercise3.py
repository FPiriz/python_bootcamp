#!/usr/bin/python

import re


def protocol_identify(protocolT):
	switcher = {
		'R': 'RIP',
		'M': 'Mobile',
		'B': 'BGP',
		'D': 'EIGRP',
		'EX': 'EIGRP external',
		'O': 'OSPF',
		'IA': 'OSPF inter area',
		'N1': 'OSPF NSSA external type 1',
		'N2': 'OSPF NSSA external type 2',
		'O E2': 'OSPF external type 2',
		'i L1': 'IS-IS level-1',
		'E': 'EGP',
		'O E1': 'OSPF external type 1',
		'i L2': 'IS-IS level-2',
		'i': 'IS-IS',
		'ia': 'IS-IS inter area',
		'U': 'per-user static route',
		'o': 'ODR',
		'P': 'periodic downloaded static route',
		'H': 'NHRP',
		'l': 'LISP',
		'a': 'application route'
	}
	return switcher.get(protocolT, "invalid")  # DEFECT NOTHING


# regex to detect dynamic protocol entry
# (?P<PROTO>[\w\t ]+?)\b\s*\b(?P<NET>([0-9]{1,3}|\.){7})\b\s*(?P<COST>\[\d+/\d+\])
#       \s*via\s*\b(?P<NEXT>([0-9]{1,3}|\.){7})\b\s*,?\s*(?P<UPD>(\d|\:)+)\s*,\s*(?P<INT>\w+)\s*
# regex to detect default
# (?<=Gateway of last resort is)\b\s*\b(?P<GTW>([0-9]{1,3}|\.){7})\b\s*to network\s*\b(?P<NEXT>([0-9]{1,3}|\.){7})
# regex to detect directly connected
# C\s*(?P<NET>([0-9]{1,3}|\.){7})\b\s*\b(?P<MASK>([0-9]{1,3}|\.){7})\b\s*.+?,\s*(?P<INT>\w+)

filename = 'ShowIpRoute.txt'
lit_protocol = r'(?P<PROTO>(R|M|B|D|EX|O|IA|N1|N2|E1|E2|E|i|su|L1|L2|ia|U|o|p|H|l|a|O\s+E[12])+?)\b\s*\b(?P<NET>(0{,2}[1-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(0{,2}[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(0{,2}[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(0{,2}[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))\b\s*\[(?P<COST>\d+/\d+)\]\s*via\s*\b(?P<NEXT>(0{,2}[1-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(0{,2}[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(0{,2}[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(0{,2}[1-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))\b\s*,?\s*(?P<UPD>(\d|\:)+)\s*,\s*(?P<INT>\w+)\s*'
re_protocol = re.compile(lit_protocol)

try:
	f = open(filename, "r")
	line = f.readline()

	while line != '':
		# by protocol route
		match = re.match(re_protocol, line)
		if match:
			print '\n------------------------\n'
			print "Protocol: " + protocol_identify(match.group('PROTO')) + '\n'
			print "Prefix: " + match.group('NET') + '\n'
			print "AD/Metric: " + match.group('COST') + '\n'
			print "Next-Hop: " + match.group('NEXT') + '\n'
			print "Last update: " + match.group('UPD') + '\n'
			print "Outbound interface: " + match.group('INT')

		line = f.readline()

	f.close()
except IOError:  # Si da error, no hace nada
	pass
