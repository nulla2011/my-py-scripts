import struct
fr=open('config.bin','rb')
by=fr.read()
print(by)
fw=open('out.bin','wb')
for b in by:
#b=struct.unpack('!B',a)
	b=b>>1
	if (b>127):
		b-=127	
	print(hex(b))
	bi=struct.pack('B',b)
	fw.write(bi)