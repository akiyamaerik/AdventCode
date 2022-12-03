#Global Variables
priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
line=0
score=0

# retrieve position of a letter in the alphabet set
def position(letter):
  pos = priority.index(letter) + 1
  return pos

# function to recursively find the column number  
def column_number(label, n):
  if n==1:
    return position(label)

  else:
    return ((26**(n-1)) * position(label[0])) + column_number(label[1:], n-1)

#main code
with open("input.txt", "r") as file:
  for line in file:
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
      n = len(i)

      col_n = column_number(i, n)
      print(col_n)
      score +=col_n
print("Score: ",score)