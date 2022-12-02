f = open("input.txt","rt") #open file in read text mode
win  = 0
loss = 0
tie  = 0
pick = 0
for line in f:
   line=line.rstrip()
   if line == 'A X':
      tie = tie+1
   elif line == 'A Y':
      loss = loss+1
   elif line == 'A Z':
      win= win+1
   elif line == 'B X':
      win= win+1
   elif line == 'B Y':
      tie = tie+1
   elif line == 'B Z':
      loss = loss+1
   elif line == 'C X':
      loss = loss+1
   elif line == 'C Y':
      win= win+1
   elif line == 'C Z':
      tie = tie+1

print "Win:", win
print "Tie:", tie
print "Loss:", loss
f.close()
