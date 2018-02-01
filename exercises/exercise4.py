access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']

mode = unicode(raw_input('Enter interface mode (access/trunk): '))
mode = mode.lower()
vlan = 1

if mode == 'access' or mode == 'trunk':
	interface = unicode(raw_input('Enter interface type and number: '))
	if mode == 'access':
		try:
			vlan = int(raw_input('Enter VLAN number: '))
		except ValueError:
			print('The VLAN number is invalid')
			exit(1)
		template = access_template
		template[1] = template[1].format(vlan)
	else:
		vlans = unicode(raw_input('Enter allowed VLANs: '))
		template = trunk_template
		template[2] = template[2].format(vlans)

	print('Interface ' + interface)
	for command in template:
		print(command)


else:
	print('The access mode is invalid')
