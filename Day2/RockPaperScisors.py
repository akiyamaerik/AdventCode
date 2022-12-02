f = open("input.txt","rt") #open file in read text mode
win  = 0
loss = 0
tie  = 0
for line in f:
   if line == 'A X':
      tie+=1
   elif line == 'A Y':
      loss+=1
   elif line == 'A Z':
      win+=1
   elif line == 'B X':
      win+=1
   elif line == 'B Y':
      tie+=1
   elif line == 'B Z':
      loss+=1
   elif line == 'C X':
      loss+=1
   elif line == 'C Y':
      win+=1
   elif line == 'C Z':
      tie+=1
print "Win:", win
print "Tie:", tie
print "Loss:", loss
f.close()
