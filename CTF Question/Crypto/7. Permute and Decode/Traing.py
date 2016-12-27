import itertools
from base64 import b64decode

d = ["ZmxhZ","3tKdX","N0X0F","fRWFz","eV9Dc","nlwdG"]

for x in itertools.permutations(d):
	print(b64decode(''.join(x) + "8hfQ=="))
