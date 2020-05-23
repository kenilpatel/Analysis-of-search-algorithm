import random
import timeit
import matplotlib.pyplot as plt  
import numpy as np 

#---------------------------------------------------------------

#For Binary Search Tree


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

#---------------------------------------------------------------

#For Red-black Search Tree

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

def addrbt(root,val,tree):
	node=rbnode(val)
	if(val<root.key):
		if(root.left==None):
			root.left=node
			node.parent=root
			parent=root
			child=node 
			#print("call check rr",parent.key,child.key)
			if(checkrr(parent,child,tree)):
				solverr(parent,child,tree)
				# print(checkrr(parent,child))
		else:
			addrbt(root.left,val,tree)
	elif(val>root.key):
		if(root.right==None):
			root.right=node
			node.parent=root
			parent=root
			child=node
			#print("call check rr",parent.key,child.key)
			if(checkrr(parent,child,tree)):
				# print(checkrr(parent,child))  
				solverr(parent,child,tree)
		else:
			addrbt(root.right,val,tree)
 
def checkrr(parent,child,tree): 
	if(parent.color==child.color=="r"): 
		return True
	else:
		return False

def solverr(parent,child,tree): 
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
	 		case1(parent,child,tree)
	 	else:
	 		if(parent.left==child):
	 			rot_type=rot_type+"l"
	 		elif(parent.right==child):
	 			rot_type=rot_type+"r"

	 	if(rot_type=="ll"):
	 		# print("ll")
	 		ll(gp,parent,child,tree)
	 	if(rot_type=="rr"):
	 		# print("rr")
	 		rr(gp,parent,child,tree)
	 	if(rot_type=="lr"):
	 		# print("lr")
	 		lr(gp,parent,child,tree)
	 	if(rot_type=="rl"):
	 		# print("rl")
	 		rl(gp,parent,child,tree)

	 elif(gp.right==parent):
	 	rot_type=rot_type+"r"
	 	if(gp.left!=None):
	 		uc=gp.left.color
	 	else:
	 		uc="b"
	 	if(parent.color==uc):
	 		# print("case2")
	 		case2(parent,child,tree)
	 	else:
	 		if(parent.left==child):
	 			rot_type=rot_type+"l"
	 		elif(parent.right==child):
	 			rot_type=rot_type+"r"

	 	if(rot_type=="ll"):
	 		# print("ll")
	 		ll(gp,parent,child,tree)
	 	if(rot_type=="rr"):
	 		# print("rr")
	 		rr(gp,parent,child,tree)
	 	if(rot_type=="lr"):
	 		# print("lr")
	 		lr(gp,parent,child,tree)
	 	if(rot_type=="rl"):
	 		# print("rl")
	 		rl(gp,parent,child,tree)

 
def changecolor(parent,tree):
	if(parent.parent.root!=True):
		parent.parent.color="r"
		if(checkrr(parent.parent.parent,parent.parent,tree)):
			solverr(parent.parent.parent,parent.parent,tree) 


def case1(parent,child,tree):
	parent.color="b"
	parent.parent.right.color="b"
	changecolor(parent,tree)  
def case2(parent,child,tree):
	parent.color="b"
	parent.parent.left.color="b"
	changecolor(parent,tree) 
def ll(gp,parent,child,tree): 
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
def rr(gp,parent,child,tree):
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
def lr(gp,parent,child,tree):
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
def rl(gp,parent,child,tree):
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

def BFSrbt(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevelrbt(root, i) 
  
  
 
def printGivenLevelrbt(root , level): 
    if root is None: 
        return
    if level == 1: 
        print(root.key,root.color,end="  ") 
    elif level > 1 : 
        printGivenLevelrbt(root.left , level-1) 
        printGivenLevelrbt(root.right , level-1) 
 
def heightrbt(node): 
    if node is None: 
        return 0 
    else :  
        lheight = height(node.left) 
        rheight = height(node.right)  
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1

#-------------------------------------------------------------------------------------------------------

#common method for searching in tree

def searchtree(root,key,i):
	if(root==None):
		return -1
	elif(root.key==key): 
		return i
	elif(key<root.key):  
		return searchtree(root.left,key,i+1)
	elif(key>root.key): 
		return searchtree(root.right,key,i+1)


#--------------------------------------------------------------------------------------------------------

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

#--------------------------------------------------------------------------------------------------------

def lsearch(list,key): 
	for i in range(0,len(list)):
		if(key==list[i]):
			return i
	return -1

#--------------------------------------------------------------------------------------------------------

#Random data of different size 

#for linear,bst and red black tree
num10=[]
num100=[]
num500=[] 

 

num10=[i for i in range(0,10)]
# random.shuffle(num10)  
num100=[i for i in range(0,100)]
# random.shuffle(num100)
num500=[i for i in range(0,500)]
# random.shuffle(num500) 

num10_S=sorted(num10)
num100_S=sorted(num100)
num500_S=sorted(num500) 

root10=node(num10[0])
for i in range(1,len(num10)):
	add(root10,num10[i])
root100=node(num100[0])
for i in range(1,len(num100)):
	add(root100,num100[i]) 
root500=node(num500[0])
for i in range(1,len(num500)):
	add(root500,num500[i])  

tree10=rbtree()
tree10.root=rbnode(num10[0],"b",True) 
for i in range(1,len(num10)):
	addrbt(tree10.root,num10[i],tree10)
tree100=rbtree()
tree100.root=rbnode(num100[0],"b",True) 
for i in range(1,len(num100)):
	addrbt(tree100.root,num100[i],tree100)
tree500=rbtree()
tree500.root=rbnode(num500[0],"b",True) 
for i in range(1,len(num500)):
	addrbt(tree500.root,num500[i],tree500) 

#--------------------------------------------------------------------------------------------------------

def startbsearch10():  
	bsearch(num10_S,num10[9],0,10)
def startbsearch100(): 
	bsearch(num100_S,num100[99],0,100) 
def startbsearch500(): 
	bsearch(num500_S,num500[499],0,500)  

def startlsearch10():  
	lsearch(num10,num10[9] )
def startlsearch100(): 
	lsearch(num100,num100[99] ) 
def startlsearch500(): 
	lsearch(num500,num500[499] )  

def startbst10():  
	searchtree(root10,num10[9],0)
def startbst100(): 
	searchtree(root100,num100[99],0) 
def startbst500(): 
	searchtree(root500,num500[499],0)  

def startrbt10():  
	searchtree(tree10.root,num10[9],0)
def startrbt100(): 
	searchtree(tree100.root,num100[99],0) 
def startrbt500():  
	searchtree(tree500.root,num500[499],0)  	

#--------------------------------------------------------------------------------------------------------

#analysis of different algorithms 

no=[10,100,500]

time10_b=timeit.timeit(startbsearch10, number=100)/100
time100_b=timeit.timeit(startbsearch100, number=100)/100
time500_b=timeit.timeit(startbsearch500, number=100)/100 

time10_l=timeit.timeit(startlsearch10, number=100)/100
time100_l=timeit.timeit(startlsearch100, number=100)/100
time500_l=timeit.timeit(startlsearch500, number=100)/100 

time10_bst=timeit.timeit(startbst10, number=100)/100
time100_bst=timeit.timeit(startbst100, number=100)/100
time500_bst=timeit.timeit(startbst500, number=100)/100 

time10_rbt=timeit.timeit(startrbt10, number=100)/100
time100_rbt=timeit.timeit(startrbt100, number=100)/100
time500_rbt=timeit.timeit(startrbt500, number=100)/100 


time_binary=[time10_b,time100_b,time500_b]
time_linear=[time10_l,time100_l,time500_l] 
time_bst=[time10_bst,time100_bst,time500_bst] 
time_rbt=[time10_rbt,time100_rbt,time500_rbt] 

print("Binary Search")
print(format(time10_b, 'f'))
print(format(time100_b, 'f'))
print(format(time500_b, 'f'))  

print("Linear Search")
print(format(time10_l, 'f'))
print(format(time100_l, 'f'))
print(format(time500_l, 'f')) 

print("Binary Search Tree")
print(format(time10_bst, 'f'))
print(format(time100_bst, 'f'))
print(format(time500_bst, 'f')) 

print("Red black  Search Tree")
print(format(time10_rbt, 'f'))
print(format(time100_rbt, 'f'))
print(format(time500_rbt, 'f')) 
#---------------------------------------------------------------------------------------------------------

#ploting 

bline=plt.plot(no,time_linear,color='red',marker='x',label="Linear Search") 
lline=plt.plot(no,time_binary,color='blue',marker='+',label="Binary Search")
bstline=plt.plot(no,time_bst,color='green',marker='o',label="Binary search tree")
rbtline=plt.plot(no,time_rbt,color='purple',marker='*',label="Red black tree")
plt.legend()
plt.title('Worst case analysis')
plt.xlabel('Number of input')
plt.ylabel('Time')  
plt.show()