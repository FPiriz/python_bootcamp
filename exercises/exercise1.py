#!/usr/bin/python

import re

def is_valid_ip(ip_address):
	ip_bytes = ip_address.split('.')
	correct = True
	if len(ip_bytes) == 4:
		for i in range(len(ip_bytes)):
			octeto = int(ip_bytes[i])
			if 255 >= octeto >= 0:
				correct = correct and True
				if i == 0 or i == 3:
					if octeto == 255 or octeto == 0:
						correct = correct and False
			else:
				correct = correct and False
	else:
		correct = False
	return correct


def is_valid_mask(mask):
	if type(mask) is unicode:
		ret = re.match('^/([0-9]|[12][0-9]|3[0-2])$', mask)
	else:
		ret = False
	return ret


def dec_to_bin(dec):
	ret = []
	decimal = int(dec)
	while decimal > 1:
		ret.append(decimal % 2)
		decimal = int(decimal / 2)
	ret.append(int(decimal))
	return ''.join(str(e) for e in ret[::-1])


def bin_to_dec(bin_value):
	result = 0
	rev_bin = bin_value[::-1]
	for index in range(len(bin_value)):
		result += int(rev_bin[index]) * (2 ** index)
	return result


all_correct = False
ip = '0.0.0.0'
while not all_correct:
	try:
		ip = unicode(raw_input('Enter Ip address: '))
		if is_valid_ip(ip):
			all_correct = True
		else:
			print('Invalid IP address format\n')
	except KeyboardInterrupt:
		print('Abort...')
		exit(1)

all_correct = False
mask = '/0'

while not all_correct:
	try:
		mask = unicode(raw_input('Enter subnet mask in decimal format: '))
		if is_valid_mask(mask):
			all_correct = True
		else:
			print('Subnet mask is invalid\n')
	except KeyboardInterrupt:
		print('Abort...')
		exit(1)

ip_bytes = ip.split('.')

for byte in ip_bytes:
	print '%8d' % int(byte),
print

for byte in ip_bytes:
	binary = int(dec_to_bin(byte))
	print '%08d' % binary,
print

mask_size = int(is_valid_mask(mask).group(1))

total_mask = ''.join(str(e) for e in [1] * mask_size) + (''.join(str(e) for e in [0] * (32 - mask_size)))
inverted_mask = ''.join(str(e) for e in [0] * mask_size) + (''.join(str(e) for e in [1] * (32 - mask_size)))
n = 8
byte_mask = [total_mask[i:i + n] for i in range(len(total_mask), n)]
inverted_byte_mask = [inverted_mask[i:i + n] for i in range(len(inverted_mask), n)]
net_addr = []
brd_addr = []
for i in range(4):
	num_net = bin_to_dec(byte_mask[i])
	num_brd = bin_to_dec(inverted_byte_mask[i])
	net_addr.append(int(ip_bytes[i]) & num_net)
	brd_addr.append(int(ip_bytes[i]) | num_brd)

network_addr = '.'.join(str(e) for e in net_addr)
broadcast_addr = '.'.join(str(e) for e in brd_addr)

print('network address is: %s' % network_addr + mask)
print('broadcast address is: %s' % broadcast_addr + mask)
