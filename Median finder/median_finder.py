import math

class MedianFinder:

  '''parameters: list of naumbers
   output: Median of this list'''
  

  def __init__(self,list = [1,5,9]):
    self.list = list

  def addNum(self, num):
    self.list.append(num)
    self.list = sorted(self.list)
    return self.list

  def findMedain(self):
    middle_value = math.floor(len(self.list)/2)-1
    if len(self.list) % 2 == 0:
      return print((self.list[middle_value]+self.list[middle_value+1])/2)
    else:
      return self.list[middle_value+1]

list1 = MedianFinder([1.5, 3 , 20])

list1.list

list1.addNum(0)

list1.findMedain()

help(MedianFinder)

