rootval=0 
tree=None
class rbtree:
	def __init__(self):
		self.root=None
class rbnode:
	def __init__(self,val,color="r",root=False):
		self.key=val
		self.left=None
		self.right=None
		self.parent=None
		self.root=root
		self.color=color
	def print(self):
		print(self.key,self.color,self.root) 

def addrbt(root,val):
	node=rbnode(val)
	if(val<root.key):
		if(root.left==None):
			root.left=node
			node.parent=root
			parent=root
			child=node 
			#print("call check rr",parent.key,child.key)
			if(checkrr(parent,child)):
				solverr(parent,child)
				# print(checkrr(parent,child))
		else:
			addrbt(root.left,val)
	elif(val>root.key):
		if(root.right==None):
			root.right=node
			node.parent=root
			parent=root
			child=node
			#print("call check rr",parent.key,child.key)
			if(checkrr(parent,child)):
				# print(checkrr(parent,child))  
				solverr(parent,child)
		else:
			addrbt(root.right,val)
 
def checkrr(parent,child): 
	if(parent.color==child.color=="r"): 
		return True
	else:
		return False

def solverr(parent,child): 
	 gp=parent.parent
	 # print("gp",gp.key,parent.key,child.key)
	 rot_type=""
	 if(gp.left==parent):
	 	rot_type=rot_type+"l"
	 	if(gp.right!=None):
	 		uc=gp.right.color
	 	else:
	 		uc="b"
	 	if(parent.color==uc):
	 		# print("case1")
	 		case1(parent,child)
	 	else:
	 		if(parent.left==child):
	 			rot_type=rot_type+"l"
	 		elif(parent.right==child):
	 			rot_type=rot_type+"r"

	 	if(rot_type=="ll"):
	 		# print("ll")
	 		ll(gp,parent,child)
	 	if(rot_type=="rr"):
	 		# print("rr")
	 		rr(gp,parent,child)
	 	if(rot_type=="lr"):
	 		# print("lr")
	 		lr(gp,parent,child)
	 	if(rot_type=="rl"):
	 		# print("rl")
	 		rl(gp,parent,child)

	 elif(gp.right==parent):
	 	rot_type=rot_type+"r"
	 	if(gp.left!=None):
	 		uc=gp.left.color
	 	else:
	 		uc="b"
	 	if(parent.color==uc):
	 		# print("case2")
	 		case2(parent,child)
	 	else:
	 		if(parent.left==child):
	 			rot_type=rot_type+"l"
	 		elif(parent.right==child):
	 			rot_type=rot_type+"r"

	 	if(rot_type=="ll"):
	 		# print("ll")
	 		ll(gp,parent,child)
	 	if(rot_type=="rr"):
	 		# print("rr")
	 		rr(gp,parent,child)
	 	if(rot_type=="lr"):
	 		# print("lr")
	 		lr(gp,parent,child)
	 	if(rot_type=="rl"):
	 		# print("rl")
	 		rl(gp,parent,child)

 
def changecolor(parent):
	if(parent.parent.root!=True):
		parent.parent.color="r"
		if(checkrr(parent.parent.parent,parent.parent)):
			solverr(parent.parent.parent,parent.parent) 


def case1(parent,child):
	parent.color="b"
	parent.parent.right.color="b"
	changecolor(parent)  
def case2(parent,child):
	parent.color="b"
	parent.parent.left.color="b"
	changecolor(parent) 
def ll(gp,parent,child): 
	A=gp.parent
	B=gp.right
	C=parent.right
	D=child.left
	E=child.right
	if(A!=None): 
		if(A.left==gp):
			A.left=parent
			parent.parent=A
			parent.right=gp
			gp.parent=parent
			parent.left=child
			child.parent=parent
			child.left=D
			if(D!=None):
				D.parent=child
			child.right=E
			if(E!=None):
				E.parent=child
			gp.left=C
			if(C!=None):
				C.parent=gp
			gp.right=B
			if(B!=None):
				B.parent=gp
			parent.color="b"
			gp.color="r"
		if(A.right==gp):
			A.right=parent
			parent.parent=A
			parent.right=gp
			gp.parent=parent
			parent.left=child
			child.parent=parent
			child.left=D
			if(D!=None):
				D.parent=child
			child.right=E
			if(E!=None):
				E.parent=child
			gp.left=C
			if(C!=None):
				C.parent=gp
			gp.right=B
			if(B!=None):
				B.parent=gp
			parent.color="b"
			gp.color="r"
	else:
		parent.right=gp
		gp.parent=parent
		parent.left=child
		child.parent=parent
		child.left=D
		if(D!=None):
			D.parent=child
		child.right=E
		if(E!=None):
			E.parent=child
		gp.left=C
		if(C!=None):
			C.parent=gp
		gp.right=B
		if(B!=None):
			B.parent=gp
		parent.color="b"
		gp.color="r"
		if(parent.key==4):
			printLevelOrder(parent)
		if(gp.root==True):
			gp.root=False
			parent.root=True
			parent.parent=None
			tree.root=parent 
def rr(gp,parent,child):
	A=gp.parent
	B=gp.left
	C=parent.left
	D=child.left
	E=child.right
	if(A!=None):
		if(A.left==gp):
			A.left=parent
			parent.parent=A
			parent.left=gp
			gp.parent=parent
			parent.right=child
			child.parent=parent
			child.left=D
			if(D!=None):
				D.parent=child
			child.right=E
			if(E!=None):
				E.parent=child
			gp.left=B
			if(B!=None):
				B.parent=gp
			gp.right=C
			if(C!=None):
				C.parent=gp
			parent.color="b"
			gp.color="r"
		if(A.right==gp):
			A.right=parent
			parent.parent=A
			parent.left=gp
			gp.parent=parent
			parent.right=child
			child.parent=parent
			child.left=D
			if(D!=None):
				D.parent=child
			child.right=E
			if(E!=None):
				E.parent=child
			gp.left=B
			if(B!=None):
				B.parent=gp
			gp.right=C
			if(C!=None):
				C.parent=gp
			parent.color="b"
			gp.color="r"
	else:
		# print(gp.key,parent.key,child.key)
		parent.left=gp
		gp.parent=parent
		parent.right=child
		child.parent=parent
		child.left=D
		if(D!=None):
			D.parent=child
		child.right=E
		if(E!=None):
			E.parent=child
		gp.left=B
		if(B!=None):
			B.parent=gp
		gp.right=C
		if(C!=None):
			C.parent=gp
		parent.color="b"
		gp.color="r"
		if(gp.root==True):
			gp.root=False
			parent.root=True
			parent.parent=None
			tree.root=parent 
def lr(gp,parent,child):
	A=gp.parent
	B=parent.left
	C=child.left
	D=child.right
	E=gp.right 
	if(A!=None):
		if(A.left==gp):
			 A.left=child
			 child.parent=A
			 child.left=parent
			 parent.parent=child
			 child.right=gp
			 gp.parent=child
			 parent.left=B
			 if(B!=None):
			 	B.parent=parent
			 parent.right=C
			 if(C!=None):
			 	C.parent=parent
			 gp.left=D
			 if(D!=None):
			 	D.parent=gp
			 gp.right=E
			 if(E!=None):
			 	E.parent=gp
			 child.color="b"
			 gp.color="r"
		if(A.right==gp):
			 A.right=child
			 child.parent=A
			 child.left=parent
			 parent.parent=child
			 child.right=gp
			 gp.parent=child
			 parent.left=B
			 if(B!=None):
			 	B.parent=parent
			 parent.right=C
			 if(C!=None):
			 	C.parent=parent
			 gp.left=D
			 if(D!=None):
			 	D.parent=gp
			 gp.right=E
			 if(E!=None):
			 	E.parent=gp
			 child.color="b"
			 gp.color="r"
	else: 
		child.left=parent
		parent.parent=child
		child.right=gp
		gp.parent=child
		parent.left=B
		if(B!=None):
			B.parent=parent
		parent.right=C
		if(C!=None):
			C.parent=parent
		gp.left=D
		if(D!=None):
			D.parent=gp
		gp.right=E
		if(E!=None):
			E.parent=gp
		child.color="b"
		gp.color="r"
		if(gp.root==True):
			gp.root=False
			child.root=True
			child.parent=None
			tree.root=child 
def rl(gp,parent,child):
	# if(gp.key==0):
	# 	print("rl case bug")
	A=gp.parent
	B=gp.left
	C=child.left
	D=child.right
	E=parent.right
	if(A!=None):
		if(A.left==gp):
			 A.left=child
			 child.parent=A
			 child.left=gp
			 gp.parent=child
			 child.right=parent
			 parent.parent=child
			 parent.left=D
			 if(D!=None):
			 	D.parent=parent
			 parent.right=E
			 if(E!=None):
			 	E.parent=parent
			 gp.left=B
			 if(B!=None):
			 	B.parent=gp
			 gp.right=C
			 if(C!=None):
			 	C.parent=gp
			 child.color="b"
			 gp.color="r"
		if(A.right==gp):
			 A.right=child
			 child.parent=A
			 child.left=gp
			 gp.parent=child
			 child.right=parent
			 parent.parent=child
			 parent.left=D
			 if(D!=None):
			 	D.parent=parent
			 parent.right=E
			 if(E!=None):
			 	E.parent=parent
			 gp.left=B
			 if(B!=None):
			 	B.parent=gp
			 gp.right=C
			 if(C!=None):
			 	C.parent=gp
			 child.color="b"
			 gp.color="r"
	else: 
		child.left=gp
		gp.parent=child
		child.right=parent
		parent.parent=child
		parent.left=D
		if(D!=None):
			D.parent=parent
		parent.right=E
		if(E!=None):
			E.parent=parent
		gp.left=B
		if(B!=None):
			B.parent=gp
		gp.right=C
		if(C!=None):
			C.parent=gp
		child.color="b"
		gp.color="r"
		if(gp.root==True):
			gp.root=False
			child.root=True
			child.parent=None
			tree.root=child 

 
def BFS(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i) 
  
  
 
def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print(root.key,root.color,end="  ") 
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


print("Welcome to Red black tree")
print("Press 1 to run algorithm on inbuilt data")
print("Press 2 to run algorithm from user input")
choice=int(input("enter ur choice:"))
if(choice==1):
	data=[23, 57, 42, 36, 84, 66, 33, 46, 51, 31, 65, 52, 12, 89, 55, 83, 8, 99, 87, 27]
	print(data)
	tree=rbtree()
	tree.root=rbnode(data[0],"b",True)  
	for i in range(1,len(data)):
		addrbt(tree.root,data[i])

	print("\nBFS\n")
	BFS(tree.root) 
	key1=83 
	print("key:",key1)
	index1=searchtree(tree.root,key1,0) 
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
	tree=rbtree()
	tree.root=rbnode(data[0],"b",True)  
	for i in range(1,len(data)):
		addrbt(tree.root,data[i])

	print("\nBFS\n")
	BFS(tree.root) 
	key1=int(input("enter key:"))
	index1=searchtree(tree.root,key1,0) 
	if(index1!=-1):
		print("\nElement found at level ",index1)
	else:
		print("\nElement not found")
print("\n\nEnd of Red black tree")