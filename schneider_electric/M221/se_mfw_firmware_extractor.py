import os, sys

# Get filename
inf = sys.argv[1]
# Generate output filename
temp_filename = inf.split('.')
if temp_filename[-1] == 'bin': 
	print('Error: %s is a binary blob. Please provide mfw file.'%(sys.argv[1]))
	sys.exit()
temp_filename[-1] = 'bin'
onf = '.'.join(temp_filename)

# Get data from file
d = open(inf,'r').readlines()
# Strip newline for processing
for e in range(len(d)):
    d[e] = d[e].strip()

# Store firmware for writing
fw = b''

# Loop through all ascii data lines and strip out firmware
for e in d:
	# Get the line length to chck for data
	len = int(e[2:4],16)
	# Test if the line has data by checking length is greater than 0x5 bytes
	if len > 0x05:
		# Grab data from between address and crc bytes and convert to bytes
		line_hex = bytes.fromhex((e[12:-2]))
		fw = fw + line_hex

# Write fw to file
ONF = open(onf,'wb')
ONF.write(fw)
ONF.close()