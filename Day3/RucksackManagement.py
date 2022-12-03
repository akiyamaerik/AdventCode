f = open("input.txt","rt") #open file in read text mode'
line=0
for line in f:
   line=line.rstrip()
   length=len(line)
   part1 = slice(0,len(line)//2)
   part2 = slice(len(line)//2,len(line))
   print("Part1",line[part1],"Part2",line[part2])
   print ("Line lenght:",length)
f.close()