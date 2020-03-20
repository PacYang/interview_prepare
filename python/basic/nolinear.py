#coding=utf-8


class Node():
    #节点类
    def __init__(self,data = -1):
        self.data = data
        self.left = None
        self.right = None
class Tree():
    #树类
    def __init__(self):
        self.root = Node()
 
    def add(self,data):
        # 为树加入节点
        node  = Node(data)
        if self.root.data == -1:        #如果树为空，就对根节点赋值
            self.root = node
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:              #对已有的节点进行层次遍历
                treeNode = myQueue.pop(0)
                if not treeNode.left:
                    treeNode.left = node
                    return
                elif not treeNode.right:
                    treeNode.right = node
                    return
                else:
                    myQueue.append(treeNode.left)

    def pre_travel(self, root):
    	if not root:
    		return False
    	print(root.data, end='-->')
    	self.pre_travel(root.left)
    	self.pre_travel(root.right)

    def pre_travel_stack(self, root):
    	if not root:
    		return False
    	node = root
    	stack = []
    	while stack or node:
    		while node:
    			print(node.data, end='-->')
    			stack.append(node)
    			node = node.left
    		node = stack.pop()
    		node = node.right

    def in_travel(self, root):
    	if not root:
    		return False
    	self.in_travel(root.left)
    	print(root.data, end='-->')
    	self.in_travel(root.right)

    def in_travel_stack(self, root):
    	if not root:
    		return False
    	stack = []
    	node = root
    	while stack or node:
    		while node:
    			stack.append(node)
    			node = node.left
    		node = stack.pop()
    		print(node.data, end='-->')
    		node = node.right

    def post_travel(self, root):
    	if not root:
    		return False
    	self.post_travel(root.left)
    	self.post_travel(root.right)
    	print(root.data, end='-->')

    def post_travel_stack(self, root):
    	if not root:
    		return False
    	stack = []
    	output = []
    	node = root
    	while stack or node:
    		while node:
    			stack.append(node)
    			output.append(node.data)
    			node = node.right
    		node = stack.pop()
    		node = node.left
    	for num in output[::-1]:
    		print(num, end='-->')


if __name__ == '__main__':
	tree = Tree()
	nums = [1,2,3,4,5,6,7,8,9,10]
	for num in nums:
		tree.add(num)
	tree.pre_travel(tree.root)
	print('\t')
	tree.pre_travel_stack(tree.root)
	print('\t')
	tree.in_travel(tree.root)
	print('\t')
	tree.in_travel_stack(tree.root)
	print('\t')
	tree.post_travel(tree.root)
	print('\t')
	tree.post_travel_stack(tree.root)
	print('\t')






