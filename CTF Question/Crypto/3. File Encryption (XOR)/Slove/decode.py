f = open("output_one","rb")
a = f.readlines()
f1 = open("final_one.png",'wb')
st = ""
for i in a:
   for j in i:
      st+=chr(ord(j)^24)
f1.write(st)
f1.close()
f.close()
