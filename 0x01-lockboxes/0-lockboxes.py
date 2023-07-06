#!/usr/bin/python3

def join(lst1,lst2):
  results =[]
  for num in lst2:
    results += lst1[num]
  return results

def canUnlockAll(boxes):
  index = 0
  total = list(set(boxes[0])| {0})
  added = True
  while added:
    added = False
    for j in join(boxes,total[index:]):
      if j not in total:
        total.append(j)
        index +=1
        added= True
  
  return len(total)==len(boxes)