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
#  for line in file:

  #something string1=
  #something string2=
  #something string3=

  #replace for comparing 3 strings  a=list(set(string1)&set(string2)) 

#  print("The common letters are:")
#  for i in a:
#    print(i)
#   n = len(i)

#    col_n = column_number(i, n)
#    print(col_n)
#    score +=col_n