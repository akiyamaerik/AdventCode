f = open("input.txt","rt") #open file in read text mode'
line=0
for line in f:
   line=line.rstrip()
   length=len(line) #Checking string lenght

   part1 = slice(0,len(line)//2)
   part2 = slice(len(line)//2,len(line)) #String slicers

   string1=line[part1]
   string2=line[part2]

   a=list(set(string1)&set(string2)) 

   print("The common letters are:")
   for i in a:
      print(i)  
#   print("Part1",line[part1],"Part2",line[part2])
#   print ("Line lenght:",length)
f.close()