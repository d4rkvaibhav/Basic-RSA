from Crypto.Util.number import *
import random
from fractions import gcd
print("Enter text to encrypt")
inp=input()
p=getPrime(32)
q= getPrime(32)
n=p*q
t=(p-1)*(q-1)
while(True):
	e=random.randint(1,65537)
	if(gcd(e,t)==1):
		break
for k in range(t):
	d=(1+(k*t))/e
	if(float(d).is_integer()==True):
		break
d=int(d)
m=inp.encode('utf=8')
m=m.hex()
print(m)

m=int(m,16)
c=pow(m,e,n)
print("Modulo (n)	:	",p*q)
print("Orignal message	:	",inp,m)
print("Ciphertext(c)	:	",c)
print("Private key(d)	:	",d)
print("First prime (p)	:	",p)
print("Second prime(q)	:	",q)
print("exponent	:	",e)

