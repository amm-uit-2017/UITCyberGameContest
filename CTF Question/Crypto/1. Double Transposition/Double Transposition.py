a=[102, 108, 97, 103, 123, 84, 104, 105, 115, 32, 105, 115, 32, 97, 32, 102, 108, 97, 103, 125]
d =[-58,-58,12,7,14,33,1,-6,7,12,13,18,13,18,35,7,5,25,25,-58]
e = []
for i in d:
    e.append(i+90)
print e , "\n" , a
b =[12, 18, 7, 13, 33, -6, 14, 15, 25, -58, 15, 25, -58, 7, -58, 12, 18, 7, 13, 35]
c = []
st=""
for i in b:
    c.append(i+90)
for i in c:
    st+=chr(i)

print st
