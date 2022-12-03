f = open("input.txt","rt") #open file in read text mode'
line=0
for line in f:
   line=line.rstrip()
   length=len(line)
   print ("Line lenght:",length)
f.close()