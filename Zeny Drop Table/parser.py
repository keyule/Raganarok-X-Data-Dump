
import re
import csv


with open('data_monster_Monster.txt', "r", encoding = "utf8") as f:
    alist = [line.rstrip() for line in f]


class monster:
  def __init__(self, name = "No Name", nameLocalized = "No Name", staticId = -1, level = -1,  baseExp = -1, jobExp =-1, maxHp =-1,  physicDefenseLevel = -1, zeny = -1):
      self.name = name 
      self.nameLocalized = nameLocalized
      self.staticId = staticId 
      self.level = level 
      self.baseExp = baseExp 
      self.jobExp = jobExp 
      self.maxHp = maxHp 
      self.physicDefenseLevel = physicDefenseLevel 
      self.zeny = zeny 

count = 0
i = 0

ObjectList = []

while (i < len(alist)):
    if re.search("\[\d+\]", alist[i]):
        i+=1
        myObject = monster()

        while True:
            if i == len(alist):
                break
            if re.search("\[\d+\]", alist[i]):
                break
            if "[\"name\"]" in alist[i]:
                myObject.name = re.search("(?<==)[^,]+",alist[i]).group()
            if "[\"nameLocalized\"]" in alist[i]:
                myObject.nameLocalized = re.search("(?<==)[^,]+",alist[i]).group()
            if "[\"staticId\"]" in alist[i]:
                myObject.staticId = re.search("(?<=)[0-9]+",alist[i]).group()
            if "[\"level\"]" in alist[i]:
                myObject.level = re.search("(?<=)[0-9]+",alist[i]).group()
            if "[\"baseExp\"]" in alist[i]:
                myObject.baseExp = re.search("(?<=)[0-9]+",alist[i]).group()
            if "[\"jobExp\"]" in alist[i]:
                myObject.jobExp = re.search("(?<=)[0-9]+",alist[i]).group()
            if "[\"maxHp\"]" in alist[i]:
                myObject.maxHp = re.search("(?<=)[0-9]+",alist[i]).group()
            if "[\"physicDefenseLevel\"]" in alist[i]:
                myObject.physicDefenseLevel = re.search("(?<=)[0-9]+",alist[i]).group()
            if "[\"zeny\"]" in alist[i]:
                myObject.zeny = re.search("(?<=)[0-9]+",alist[i]).group()
                print(myObject.zeny)


            i+=1

        ObjectList.append(myObject)


#for obj in ObjectList:
    #print (obj.id)
    #print (obj.isCardDrop)
    #print(obj.Name)
    #print(obj.staticID)
    #print(obj.probability)
    #print(obj.probabilityDenominator)


with open('rawMonsterTable.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "nameLocalized", "staticId", "level", "baseExp", "jobExp", "maxHp", "physicDefenseLevel", "zeny", ])
    for obj in ObjectList:
        writer.writerow([obj.name, obj.nameLocalized, obj.staticId, obj.level, obj.baseExp, obj.jobExp, obj.maxHp, obj.physicDefenseLevel, obj.zeny])



