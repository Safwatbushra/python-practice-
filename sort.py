
gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

answer = int(input("Q1) Do you like Dawn or Dusk?"))
if answer ==1 :
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin +=1
else:
  print("wrong input")


answer = int(input("Q2)When I’m dead, I want people to remember me as:"))
if answer == 1:
  hufflepuff += 2
elif answer == 2:
  slytherin += 2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor += 2
else:
  print('Wrong input.')


answer = int(input("Q3) Which kind of instrument most pleases your ear?"))
if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw +=4
elif answer == 4:
  gryffindor += 4
else:
  print('Wrong input.')
print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

top_score = max( gryffindor ,hufflepuff ,ravenclaw ,slytherin )
if gryffindor > hufflepuff and gryffindor > ravenclaw and gryffindor > slytherin :
  print ("gryffindor is with most points")
elif gryffindor < hufflepuff and hufflepuff > ravenclaw and hufflepuff > slytherin :
  print ("hufflepuff is with most points")
elif ravenclaw > hufflepuff and gryffindor < ravenclaw and ravenclaw > slytherin :
  print (" ravenclaw is with most points ")
else :
  print( "slytherin is with most points")





