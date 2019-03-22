## Basic RSA implementation



## Encryption


1.Choose two different primes p and q.

2.Our modulus(n) will be n=p*q.

3.Calculate t = (p-1)*(q-1)

4.Now we have to choose **e** (public key exponent) such that 1<e<t and gcd(e,t)=1 .But it is advisable to choose a medium range e becuase if e is very large or very small than RSA can be attacked using various techniques.

5.Then we have to compte d (private key) such that d*e=1+kt where k is a natural number.

Now we have all the things ready to encrypt.

Let the message be m.

Put ciphertext (c) =  power(m,e) % n <br>
{pow(m,e,n) can be used in python}

Now our ciphertext is ready !!! :)


## Decryption

Coming Soon !!!!




# CODE

```markdown
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
m=int(m,16)
c=pow(m,e,n)

```
You can get the python code for encyption [here](encrypt.py).

Decryption of RSA Coming Soon !!

