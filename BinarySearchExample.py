numbers = [1,2,3,4,5,6,7,8]
key = int(input("Enter the number : ")) 

low = 0
high = len(numbers) - 1

while low <= high :
	mid = int((low + high) / 2)
	if numbers[mid] == key :
		print(" Key is present on  index : " ,mid)
		break
	elif key  > numbers[mid] :
		low = mid + 1
	else :
		high = mid - 1
		

