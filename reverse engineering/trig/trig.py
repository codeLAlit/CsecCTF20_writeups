from pwn import *
from Crypto.Util.number import *


op = 'ephcmbhkmemndpkagnebjbcbdpcbglelpnfpdpcbokhpdbahdpfpdjboemeodpkehfphfbhcdpfmpmbpifdkbeimmdpkjjai'.encode()

l = [op[2*i:2*(i+1)] for i in range(len(op)//2)] #take 2 chars together
l = [o[::-1] for o in l] #reverse the 2 chars
l = [hex(bytes_to_long(i)-0x6161) for i in l] #subtract
op = []
for s in l:
    if (len(s) < 4):
        op.append('0'+s[2])
    else:
        op.append(s[2]+s[4])
#join the higher and lower bytes the shitty way
op = op[::-1] #reverse the memory

op = [''.join(op[6*i:6*i+6]) for i in range(len(op)//6)]
# print(op) #op contains bytes in little-endian form, need to be careful
int_val = '0000'+op[0] #integer has lower bytes as zero
float_vals = [s+'d6bf' for s in op[1:]] #float has higher bytes as 'd6bf' coz cosine

(int_val,) = struct.unpack('d',bytes.fromhex(int_val)) #read the value as a double

import gmpy2

l = []
for s in float_vals:
    (a,) = struct.unpack('d',bytes.fromhex(s)) #read as double
    l.append(a)

l = [gmpy2.mpz((gmpy2.acos(i)-gmpy2.mpq(1)-gmpy2.mpq(15,16)-gmpy2.mpq(8,16**12))*gmpy2.mpz(16**11)) for i in l] #find out X, and make it integer
l.insert(3,gmpy2.mpz(int_val)) #0:4, 4:8, 8:12 then insert the integer([12:16])
s = []
for i in l:
    (a,) = struct.unpack('4s',bytes.fromhex(hex(i)[2:])) #read integer as qword, convert to 4-length string
    s.append(a[::-1]) #need to reverse because X was reversed(X4 X3 X2 X1, remember)
print(b''.join(s)) #flag :)