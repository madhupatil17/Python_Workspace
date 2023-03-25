# inputObj = 'B78$5$d90m326u6799A5c67r21i@p#8t' #B78$5$d90m326u6  A5c67r21i@p#8t
# outObj = ''
# listOfSpChars = list()
# listOfOdd = list()
# listOfEven = list()
# finalList = list()
#
# for _ in inputObj:
#     if not _.isalnum():
#         listOfSpChars.append(_)
#     if _.isnumeric() and int(_) % 2 == 0:
#         listOfEven.append(_)
#     elif _.isnumeric() and not int(_) % 2 == 0:
#         listOfOdd.append(_)
#
# largestList = 0
# if len(listOfEven) > len(listOfOdd):
#     largestList = len(listOfEven)
# else:
#     largestList = len(listOfOdd)
#
# def appendAlternate(list1, list2, largelist):
#     for i in range(0, largestList):
#         try:
#             finalList.append(list1[i])
#         except:
#             pass
#         try:
#             finalList.append(list2[i])
#         except:
#             pass
#
# if len(listOfSpChars) % 2 == 0:
#     appendAlternate(listOfEven, listOfOdd, largestList)
# else:
#     appendAlternate(listOfOdd, listOfEven, largestList)
#
# for _ in finalList:
#     outObj += _
#
# print(inputObj)
# print(listOfOdd, listOfEven)
# print(outObj)


import random
import math
list = ["Sandipan", "Naresh", "Madhusudan", "Shilpashree", "Mouna", "Arati"]
listA = []
listB = []

for _ in range(0, len(list)):

    choicee1 = random.choice(list)
    choicee2 = random.choice(list)
    if not choicee1.__eq__(choicee2):
        if choicee1 not in listA and choicee2 not in listA:
            listA.append(choicee1)
        if choicee2 not in listB and choicee1 not in listB:
            listB.append(choicee2)
    else:
        continue

for j in range(0, len(listA)):
    print(listA[j], " : ", listB[j])



