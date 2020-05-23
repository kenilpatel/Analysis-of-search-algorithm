import os
# os.system('python WORST.py')

while(True):
	os.system('cls')
	print("Welcome to analysis of algorithms")
	print("Press 1 for worst case analysis")
	print("Press 2 for average case analysis")
	print("Press 3 for Linear Search")
	print("Press 4 for Binary Search")
	print("Press 5 for Binary Search tree")
	print("Press 6 for Red black tree")
	print("press 0 for exit")
	choice=int(input("Enter your choice:"))
	if(choice==0):
		break
	elif(choice==1):
		os.system('python WORST.py')
	elif(choice==2):
		os.system('python avg.py')
	elif(choice==3):
		os.system('python linear.py')
	elif(choice==4):
		os.system('python bs.py')
	elif(choice==5):
		os.system('python bst.py')
	elif(choice==6):
		os.system('python rbtree.py')
	input("Press Enter to continue")