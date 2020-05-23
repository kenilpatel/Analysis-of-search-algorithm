class node:
	def __init__(self,val):
		self.key=val
		self.right=None
		self.left=None
	def data(self):
		print(self.key)

def add(root,val):
	if(val<root.key):
		if(root.left==None): 
			temp=node(val)
			root.left=temp
		else:
			add(root.left,val)
	elif(val>root.key):
		if(root.right==None):
			temp=node(val)
			root.right=temp
		else:
			add(root.right,val)

def bst(root,key,i):
	if(root==None):
		return -1
	elif(root.key==key): 
		return key
	elif(key<root.key):  
		return bst(root.left,key,i+1)
	elif(key>root.key): 
		return bst(root.right,key,i+1)

def BFS(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i) 
  
  
 
def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print(root.key,end="  ") 
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 
 
def height(node): 
    if node is None: 
        return 0 
    else :  
        lheight = height(node.left) 
        rheight = height(node.right)  
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1

def searchtree(root,key,i):
	if(root==None):
		return -1
	elif(root.key==key): 
		return i
	elif(key<root.key):  
		return searchtree(root.left,key,i+1)
	elif(key>root.key): 
		return searchtree(root.right,key,i+1)

print("Welcome to Binary search tree")
print("Press 1 to run algorithm on inbuilt data")
print("Press 2 to run algorithm from user input")
choice=int(input("enter ur choice:"))
if(choice==1):
	data=[23, 57, 42, 36, 84, 66, 33, 46, 51, 31, 65, 52, 12, 89, 55, 83, 8, 99, 87, 27]
	print(data)
	root=node(data[0])
	for i in range(1,len(data)):
		add(root,data[i])
	print("\nBFS\n")
	BFS(root) 
	key1=83 
	print("key:",key1)
	index1=searchtree(root,key1,0) 
	if(index1!=-1):
		print("\nElement found at level ",index1)
	else:
		print("\nElement not found")
	 
elif(choice==2):
	n=int(input("enter size of data:"))
	data=[]
	for i in range(0,n):
		d=int(input("enter data:"))
		data.append(d) 
	root=node(data[0])
	for i in range(1,len(data)):
		add(root,data[i])
	print("\nBFS\n")
	BFS(root) 
	key1=int(input("enter key:")) 
	index1=searchtree(root,key1,0) 
	if(index1!=-1):
		print("\nElement found at level ",index1)
	else:
		print("\nElement not found")
print("\n\nEnd of Binary search tree")