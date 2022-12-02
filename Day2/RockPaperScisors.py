f = open("input.txt","rt") #open file in read text mode
win  = 0
loss = 0
tie  = 0
score = 0
for line in f:
   line=line.rstrip()
   if line == 'A X': #rock rock Need to Lose
      tie+=1
      score+=4
   elif line == 'A Y': #rock paper Need to Draw
      win+=1
      score+=8
   elif line == 'A Z': #rock scissors Need to Win
      loss+=1
      score+=3
   elif line == 'B X':#paper rock Need to Lose
      loss+=1
      score+=1
   elif line == 'B Y': #paper paper Need to Draw
      tie+=1
      score+=5
   elif line == 'B Z': #paper scissors Need to Win
      loss+=1
      score+=9
   elif line == 'C X': #scissors rock Need to Lose
      win+=1
      score+=7
   elif line == 'C Y': #scissors paper Need to Draw
      loss+=1
      score+=2
   elif line == 'C Z': #scissors scissors Need to Win
      tie+=1
      score+=6

print "Win:", win
print "Tie:", tie
print "Loss:", loss
print "Score:", score
f.close()
