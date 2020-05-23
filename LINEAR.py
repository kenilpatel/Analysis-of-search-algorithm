def lsearch(list,key): 
	for i in range(0,len(list)):
		if(key==list[i]):
			return i
	return -1

print("Welcome to Linear search")
print("Press 1 to run algorithm on inbuilt data")
print("Press 2 to run algorithm from user input")
choice=int(input("enter ur choice:"))
if(choice==1):
	data=[23, 57, 42, 36, 84, 66, 33, 46, 51, 31, 65, 52, 12, 89, 55, 83, 8, 99, 87, 27]  
	print(data)
	key1=83 
	print("key:",key1)
	index1=lsearch(data,key1 ) 
	if(index1!=-1):
		print("Element found at index ",index1)
	else:
		print("Element not found")
elif(choice==2):
	n=int(input("enter size of data:"))
	data=[]
	for i in range(0,n):
		d=int(input("enter data"))
		data.append(d) 
	key1=int(input("enter key"))
	index1=lsearch(data,key1) 
	if(index1!=-1):
		print("Element found at index ",index1)
	else:
		print("Element not found")
print("\n\nEnd of Linear search")