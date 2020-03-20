#coding=utf-8
import time
from math import floor as floor

class Sort(object):
	"""docstring for Sort"""
	def __init__(self, lists):
		super(Sort, self).__init__()
		self.lists = lists
		self.length = len(lists)

	def insert_sort(self):
		for i in range(1,self.length):
			# print(f'第{i+1}个数插入:')
			for j in range(i,0,-1):
				if j >= 1 and self.lists[j] < self.lists[j-1]:
					self.lists[j-1],self.lists[j] = self.lists[j],self.lists[j-1]
				# print(self.lists)

	def bubble_sort(self):
		for i in range(self.length-1, 0, -1):
			# print(f'第{self.length-i}轮两两比较处理:')
			for j in range(i):
				if self.lists[j] > self.lists[j+1]:
					self.lists[j], self.lists[j+1] = self.lists[j+1], self.lists[j]
				# print(self.lists)

	def shell_sort(self):
		dis = floor(self.length / 2)
		while dis > 0:
			for i in range(dis, self.length):
				while self.lists[i] < self.lists[i-dis]:
					self.lists[i], self.lists[i-dis] = self.lists[i-dis], self.lists[i]
				print(self.lists)
			dis = floor(dis / 2)

	def select_sort(self):
		for i in range(self.length-1, 0, -1):
			# print(f'第{self.length-i}轮找最大数:')
			max_index = i
			for j in range(i):
				if self.lists[j] > self.lists[max_index]:
					max_index = j
			self.lists[i], self.lists[max_index] = self.lists[max_index], self.lists[i]
			# print(self.lists)

	def heap_sort(self):
		pass

	def quick_sort(self, left, right):
		if left < right:
			mid = self.partition(self.lists, left, right)
			self.quick_sort(left, mid-1)
			self.quick_sort(mid+1, right)

	def partition(self, array, left, right):
		tmp = array[left]
		while left < right:
			while left < right and array[right] >= tmp:
				right -= 1
			array[left] = array[right]
			while left < right and array[left] <= tmp:
				left += 1
			array[right] = array[left]
			# print(array)
		array[left] = tmp
		return left


def heap_sort(array):
	# print('start:',array)
	begin = 0
	end = len(array)-1
	for i in range(len(array)):
		heap_adjust(array,begin,end)
		array[begin],array[end] = array[end],array[begin]
		end -= 1
	# print('end:',array)

def heap_adjust(array, begin, end):
	length = end - begin + 1
	for j in range(length//2-1,-1,-1):
		left = j*2+1
		right = j*2+2
		if array[j] < array[left]:
			array[j],array[left] = array[left],array[j]
		if right < length and array[j] < array[right]:
			array[j],array[right] = array[right],array[j]
	# print(array)

def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


if __name__ == '__main__':
	import random
	count = 10000
	# nums = [random.randint(0,count) for i in range(count)]
	nums = [4,1,5,2,3,6,3,9,5,4]
	sort = Sort(lists=nums)
	start = time.time()*1000
	# heap_sort(nums)
	# sort.insert_sort()
	# sort.bubble_sort()
	# sort.shell_sort()
	# sort.select_sort()
	# sort.quick_sort(0, sort.length-1)
	print(merge_sort(nums))
	end = time.time()*1000
	print(nums)
	print(f'cost time:{end-start}ms')