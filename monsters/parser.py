
import re
import csv


with open('data_monster_Monster', "r", encoding = "utf8") as f:
    alist = [line.rstrip() for line in f]


class drop:
  def __init__(self, id = -1, isCardDrop = -1, Name = "No Name", staticID = -1, probability = -1, probabilityDenominator = -1):
      self.id = id 
      self.isCardDrop = isCardDrop 
      self.Name = Name 
      self.staticID = staticID 
      self.probability = probability 
      self.probabilityDenominator = probabilityDenominator 

count = 0
i = 0

ObjectList = []

while (i < len(alist)):
    if re.search("\[\d+\]", alist[i]):
        i+=1
        myObject = drop()

        while True:
            if i == len(alist):
                break
            if re.search("\[\d+\]", alist[i]):
                break
            if "[\"id\"]" in alist[i]:
                myObject.id = re.search("(?<=)[0-9]+",alist[i]).group()
            if "[\"IsCardDrop\"]" in alist[i]:
                myObject.isCardDrop = re.search("(?<=)[0-9]+",alist[i]).group()
            if "[\"Name\"]" in alist[i]:
                myObject.Name = re.search("(?<==)[^,]+",alist[i]).group()
            if "[\"staticId\"]" in alist[i]:
                myObject.staticID = re.search("(?<=)[0-9]+",alist[i]).group()
            if "[\"probability\"]" in alist[i]:
                myObject.probability = re.search("(?<=)[0-9]+",alist[i]).group()
            if "[\"probabilityDenominator\"]" in alist[i]:
                myObject.probabilityDenominator = re.search("(?<=)[0-9]+",alist[i]).group()

            i+=1

        ObjectList.append(myObject)


#for obj in ObjectList:
    #print (obj.id)
    #print (obj.isCardDrop)
    #print(obj.Name)
    #print(obj.staticID)
    #print(obj.probability)
    #print(obj.probabilityDenominator)


with open('rawdroptable.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "isCardDrop", "Name", "staticID", "probability", "probabilityDenominator"])
    for obj in ObjectList:
        writer.writerow([obj.id, obj.isCardDrop, obj.Name, obj.staticID, obj.probability, obj.probabilityDenominator])



