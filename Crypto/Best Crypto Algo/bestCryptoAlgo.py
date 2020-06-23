from math import floor,sqrt
from random import randint as rand
str = 'S7rinG_t0_b3_enCRYpt3D';

dec_array=[]
for i in range(len(str)):
	dec_array.append(ord(str[i]))

maxval=max(dec_array)
key=rand(10,maxval)
key=key*101
for i in range(len(str)):
	x=dec_array[i]
	am=(key+x)/2
	gm=sqrt(key*x)
	enc=am+gm
	print(floor(enc)%255,end=" ")


#153 33 113 45 118 185 228 27 33 51 252 236 90 252 160 252 33 27 85 252 176 33 106 139 228 101 252 33 179 176 33 106 252 236 123 160 68 62 33 99 236 79 123