
class TreeNode(object): 
	def __init__(self, val): 
		self.val = val 
		self.left = None
		self.right = None
		self.height = 1

	def __str__(self):
		return str(self.val)
  
  
class AVL_Tree(object): 
	#code here

	def insert(self,root,data):
		if root == None:
			return TreeNode(data)
		elif data < root.val:
			root.left = self.insert(root.left,data)
		else:
			root.right = self.insert(root.right,data)

		root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
			
		balance = self.getBalance(root)
			
		# Left Left
		if balance > 1 and data < root.left.val:
			print('Not Balance, Rebalance!')
			return self.rightRotate(root)
		#Right Right
		if balance < -1 and data > root.right.val:
			print('Not Balance, Rebalance!')
			return self.leftRoatate(root)
		#Left Right
		if balance > 1 and data > root.left.val:
			root.left = self.leftRoatate(root.left)
			print('Not Balance, Rebalance!')
			return self.rightRotate(root)
		#Right Left
		if balance < -1 and data < root.right.val:
			root.right = self.rightRotate(root.right)
			print('Not Balance, Rebalance!')
			return self.leftRoatate(root)

		return root

	def getHeight(self,root):
		if not root:
			return 0
		
		return root.height			

	def getBalance(self,root):
		if root == None:
			return 0
		
		return self.getHeight(root.left) - self.getHeight(root.right)

	def leftRoatate(self,node):
		newNode = node.right
		childNode = newNode.left

		newNode.left = node
		node.right = childNode

		node.height = 1 +max(self.getHeight(node.left),self.getHeight(node.right))
		newNode.height = 1 + max(self.getHeight(newNode.left),self.getHeight(newNode.right))

		return newNode

	def	rightRotate(self,node):
		newNode = node.left
		childNode = newNode.right

		newNode.right = node
		node.left = childNode

		node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
		newNode.height = 1 + max(self.getHeight(newNode.left),self.getHeight(newNode.right))

		return newNode

def printTree(node,level = 0):
	if node!= None:
		printTree(node.right ,level + 1)
		print('     ' * level , node)
		printTree(node.left ,level + 1 )

myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
	print("insert :",e)
	root = myTree.insert(root,int(e))
	printTree(root)
	print("===============")