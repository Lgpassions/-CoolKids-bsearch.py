#Glenisha Smith @02679391
# November 17, 2013
# SYCS 100
# Binary Search



def bsearch(myItem, myList):
	found = False
	low = 0
	high = len(myList)-1
	while low <= high and not found:
		mid = (low + high)//2
		if myList[mid]== myItem:
			found = True
		elif myList[mid] < myItem:
			low = mid + 1
		else :
			high = mid - 1
	return found

List = sorted([67,78,9,67,53,24,23,87])
Item = 7
isitFound = bsearch(Item, List)
if isitFound:
	print List.index(Item)
else:
	print -1
