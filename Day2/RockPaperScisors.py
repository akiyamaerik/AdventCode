f = open("input.txt","rt") #open file in read text mode
win  = 0
loss = 0
tie  = 0
score = 0
for line in f:
   line=line.rstrip()
   if line == 'A X': #rock Need to Lose
      loss+=0
      score+=3  #pick scissors Lose:0, Scissors:3
   elif line == 'A Y': #rock Need to Draw
      tie+=1
      score+=4  #pick rock Draw:3, Rock:1
   elif line == 'A Z': #rock scissors Need to Win
      win+=1
      score+=8 #pick paper Win:6, Paper:2
   elif line == 'B X':#paper rock Need to Lose
      loss+=1
      score+=1 #pick rock Lose:0, Rock:1
   elif line == 'B Y': #paper Need to Draw
      tie+=1
      score+=5 #pick paper Draw:3, Paper:2
   elif line == 'B Z': #paper Need to Win
      win+=1
      score+=9 #pick scissors Win:6, Scissors:3
   elif line == 'C X': #scissors rock Need to Lose
      loss+=1
      score+=2  #pick paper Lose:0, Paper:2
   elif line == 'C Y': #scissors Need to Draw
      tie+=1
      score+=6 #pick scissors Draw:3, Scissors:3
   elif line == 'C Z': #scissors Need to Win
      win+=1
      score+=7 #pick rock Win:6, Rock:1

print "Win:", win
print "Tie:", tie
print "Loss:", loss
print "Score:", score
f.close()
