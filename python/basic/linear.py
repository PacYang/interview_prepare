#coding=utf-8

count = 0
class SingleNode(object):
	"""docstring for SingleNode"""
	def __init__(self, value):
		super(SingleNode, self).__init__()
		self.value = value
		self.next = None

class SingleLingList(object):
	"""docstring for SingleLingList"""
	def __init__(self):
		super(SingleLingList, self).__init__()
		self._head = None

	def is_empty(self):
		return self._head is None

	# @staticmethod
	def length(self):
		cur = self._head
		count = 0
		while cur is not None:
			count += 1
			cur = cur.next
		return count

	# @staticmethod
	def travel(self):
		print('...遍历链表...')
		cur = self._head
		while cur is not None:
			if cur.next is not None:
				print(f'{cur.value}',end='-->')
			else:
				print(f'{cur.value}')
			cur = cur.next

	def add(self, value):
		node = SingleNode(value)
		node.next = self._head
		self._head = node

	def append(self, value):
		node = SingleNode(value)
		cur = self._head
		if cur is None:
			self._head = node
			return
		while cur.next is not None:
			cur = cur.next
		cur.next = node

	def insert(self, index, value):
		node = SingleNode(value)
		count = 0
		cur = self._head
		if index == 0:
			self.add(value)
			return
		while cur is not None:
			count += 1
			if count == index:
				node.next = cur.next
				cur.next= node
				return
			cur = cur.next
		if count <= index:
			self.append(value)

	def pop(self):
		cur = self._head
		while cur.next is not None:
			if cur.next.next is None:
				cur.next = None
			else:
				cur = cur.next

	def delete(self, index):
		pass

	def __reverse_list1(self, pHead):
	    if not pHead or not pHead.next:
	    	return pHead
	    NewHead = self.__reverse_list1(pHead.next)
	    pHead.next.next = pHead
	    pHead.next = None
	    return NewHead

	def __reverse_list2(self):
		if self._head is None or self._head.next is None:
			return self._head
		cur = self._head
		tmp = None
		new_head = None
		while cur:
			tmp = cur.next
			cur.next = new_head
			new_head = cur
			cur = tmp
		return new_head

	def reverse(self):
		print('...反转链表...')
		# self._head = self.__reverse_list1(self._head)
		self._head = self.__reverse_list2()

		
class DoubleNode(object):
	"""docstring for DoubleNode"""
	def __init__(self, value):
		super(DoubleNode, self).__init__()
		self.value = value
		self.pre = None
		self.next = None

class DoubleLinkList(object):
	"""docstring for DoubleLinkList"""
	def __init__(self):
		super(DoubleLinkList, self).__init__()
		self._head = None


class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		super(Stack, self).__init__()
		self.items = []

	def pop(self):
		self.items.pop()

	def append(self, value):
		self.items.append(value)

	def travel(self):
		print(self.items)
		
class Queue(object):
	"""docstring for Queue"""
	def __init__(self):
		super(Queue, self).__init__()
		self.items = []
	
	def append(self, value):
		self.items.insert(0,value)

	def pop(self):
		self.items.pop()

	def travel(self):
		print(self.items)


if __name__ == '__main__':
	link_list = SingleLingList()
	# link_list.append(1)
	# link_list.append(2)
	# link_list.add(3)
	# link_list.insert(4,4)
	for i in range(100):
		link_list.append(i+1)
	link_list.travel()
	link_list.reverse()
	link_list.travel()
	print(link_list.length())


	

	# stack = Stack()
	# for i in range(10):
	# 	stack.append(i)
	# stack.travel()
	# stack.pop()
	# stack.travel()

