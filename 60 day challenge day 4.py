data=[10, "apple", "", 25, "banana", 40]

numberList=[]
stringList=[]

numberCount=0
stringCount=0

for i in data:
  if type(i)==int:
    numberList.append(i)
    numberCount=numberCount+1
  elif type(i)==str:
    if i!="":
      stringList.append(i)
      stringCount=stringCount+1

name="Mahesh"
nameLength=0

for j in name:
    nameLength=nameLength+1

if nameLength % 2!=0:
     if len(numberList)>0:
       numberList.pop()
     if len(stringList)>0:
       stringList.pop()
else:
    if len(numberList)>0:
        numberList.pop(0)
    if len(stringList)>0:
     stringList.pop(0)

print("Number List : ",numberList)
print("String List : ",stringList)
print("Total Numbers : ",numberCount)
print("Total Strings : ",stringCount)