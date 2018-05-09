#Binary search with Python

#Takes in the array and the target number
def bs(array, find):
	
	#Finds the middle of the array (everytime this is used)
	mid = arr[len(arr)//2]
	
	#Prints the middle value everytime
	print('the new middle is %d'%(mid))
	
	#When the search number is not in the array or is a letter
	#Returning a value if failed
	if len(arr) == 0 or (len(arr)==1 and arr[0]!= find):
		return False
	
	#If statement for when the target is found and is a mid number
	if find == mid: return True
	
	#Condtional for lower & upper half
	#Recursion, passing into the new arr, find the target number
	if find > mid: return b_search(arr[len(arr)//2+1:], find)
	if find < mid: return b_search(arr[:len(arr)//2], find)

array = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(bs(array,2))
