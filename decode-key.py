seed = 37
array = str.encode("J9h4j5eNds+aq1==")
array2=[0]*16
for i in range(1,17):
	#print(array[i-1])
	array2[i-1]=array[i-1]^seed
	seed += 13
	print(hex(array2[i-1]))
#str1="".join(array2)
print(array2)