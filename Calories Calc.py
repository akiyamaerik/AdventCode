f = open("input.txt","rt") #open file in read text mode
total = 0
count= 0
calories = []
for line in f:
   if line == '\n': #if blank line is found
        calories.append(total)
        count+=1
        total=0
        continue
   else:
        num = int(line) #convert from str to int
        total += num

print "Max value element : ", max(calories)

calories.sort(reverse=True)

print "Max three elements:", calories [:3]
x = sum(calories[:3])
print "Three top calories in total:", x
f.close()
