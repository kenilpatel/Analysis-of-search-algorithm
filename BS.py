def bsearch(list,key,low,high): 
	if low<high:
		mid=int((low+high)/2) 
		if(list[mid]==key):
			return mid
		elif(list[mid]>key):  
			return bsearch(list,key,low,mid-1)
		elif(list[mid]<key): 
			return bsearch(list,key,mid+1,high)
	else:
		return -1
print("Welcome to Binary search")
print("Press 1 to run algorithm on inbuilt data")
print("Press 2 to run algorithm from user input")
choice=int(input("enter ur choice:"))
if(choice==1):
	data=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	print(data)
	data=sorted(data) 

	key1=10 
	print("key:",key1)
	index1=bsearch(data,key1,0,len(data)) 
	if(index1!=-1):
		print("Element found")
	else:
		print("Element not found") 
elif(choice==2):
	n=int(input("enter size of data:"))
	data=[]
	for i in range(0,n):
		d=int(input("enter data:"))
		data.append(d)  
	data=sorted(data) 
	key1=int(input("enter key:"))
	index1=bsearch(data,key1,0,len(data)) 
	if(index1!=-1):
		print("Element found")
	else:
		print("Element not found")

print("\n\nEnd of Binary search")