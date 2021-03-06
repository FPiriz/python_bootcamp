#!/usr/bin/python

import re

# return True if the input is a string and it contains
# a valid IPv4 address, return False otherwise
def is_valid_ip(ip_address):
	if type(ip_adress) is unicode
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
	else:
		correct = False
	return correct

# return True if the input is a string and it contains
# a slash and a number between 0 and 32, return False otherwise
def is_valid_mask(mask):
	if type(mask) is unicode:
		ret = re.match('^/([0-9]|[12][0-9]|3[0-2])$', mask)
	else:
		ret = False
	return ret

# return a integer with the binary representation of the
# input, with the minimun length of bits
def dec_to_bin(dec):
	ret = []
	decimal = int(dec)
	while decimal > 1:
		ret.append(decimal % 2)
		decimal = int(decimal / 2)
	ret.append(int(decimal))
	return ''.join(str(e) for e in ret[::-1])

# return an integer with the base 10 representation
# of the input string, which is binary
def bin_to_dec(bin_value):
	result = 0
	rev_bin = bin_value[::-1]
	for index in range(len(bin_value)):
		result += int(rev_bin[index]) * (2 ** index)
	return result

# inicialise
all_correct = False
ip = '0.0.0.0'

# ask an ip untill the input is a valid IPv4
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
# reset variables
all_correct = False
mask = '/0'

# ask a mask in decimal format ('/XX') until is valid
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

# divide the ip in bytes and print each one right justified
ip_bytes = ip.split('.')

for byte in ip_bytes:
	print '%8d' % int(byte),
print

# print each byte of the ip with 8 bits representation
for byte in ip_bytes:
	binary = int(dec_to_bin(byte))
	print '%08d' % binary,
print

# get mask size
mask_size = int(is_valid_mask(mask).group(1))

# calculate the mask in binary format and its inverse
total_mask = ''.join(str(e) for e in [1] * mask_size) + (''.join(str(e) for e in [0] * (32 - mask_size)))
inverted_mask = ''.join(str(e) for e in [0] * mask_size) + (''.join(str(e) for e in [1] * (32 - mask_size)))
n = 8
# divide mask in octets
byte_mask = [total_mask[i:i + n] for i in range(len(total_mask), n)]
inverted_byte_mask = [inverted_mask[i:i + n] for i in range(len(inverted_mask), n)]
net_addr = []
brd_addr = []

# create the network address (IP & MAKS) and the broadcast address (IP | !MASK
for i in range(4):
	num_net = bin_to_dec(byte_mask[i])
	num_brd = bin_to_dec(inverted_byte_mask[i])
	net_addr.append(int(ip_bytes[i]) & num_net)
	brd_addr.append(int(ip_bytes[i]) | num_brd)

network_addr = '.'.join(str(e) for e in net_addr)
broadcast_addr = '.'.join(str(e) for e in brd_addr)

print('network address is: %s' % network_addr + mask)
print('broadcast address is: %s' % broadcast_addr + mask)
