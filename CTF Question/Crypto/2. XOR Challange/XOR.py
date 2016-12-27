# Author : L0V3R IN MSF <3

keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#keys = "abcdefghijklmnopqrstuvwxyz"
xored = "0a202d2b37292d3f35132a233e1334233e132f3e353c382331"

def decrypt(key):
    ans = ""
    for i in xored.decode("hex"):
        #print ord(i)
        tmp = ord(i) ^ ord(key)
        ans += chr(tmp)
    print "Using key [ %s ] : %s"%(key,ans)

for key in keys:
    decrypt(key)
