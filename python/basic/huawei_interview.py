#coding=utf-8

def find_num(lists,num):
	for i in range(len(lists)):
		sub = abs(lists[i] - num)
		# print(sub)
		if i == 0:
			min_sub = sub
			min_num = lists[i]
		if sub < min_sub:
			min_sub = sub
			min_num = lists[i]
	return min_num


def quick_sort(nums, left, right):
	if left < right:
		mid = partition(nums, left, right)
		quick_sort(nums, left, mid-1)
		quick_sort(nums, mid+1, right)


def partition(nums, left, right):
	tmp = nums[left]
	while left < right:
		while left < right and nums[right] >= tmp:
			right -= 1
		nums[left] = nums[right]
		while left < right and nums[left] <= tmp:
			left += 1
		nums[right] = nums[left]
	nums[left] = tmp
	return left


def heap_sort(nums):
	left = 0
	right = len(nums) - 1
	for i in range(len(nums)-1,0,-1):
		heap_adjust(nums, left, right)
		nums[i],nums[0] = nums[0],nums[i]
		right -= 1

def heap_adjust(nums, left, right):
	length = right - left + 1
	for i in range(length//2-1,-1,-1):
		left_leaf = 2*i+1
		right_leaf = 2*i+2
		if nums[i] < nums[left_leaf]:
			nums[i],nums[left_leaf] = nums[left_leaf],nums[i]
		if right_leaf < length and nums[i] < nums[right_leaf]:
			nums[i],nums[right_leaf] = nums[right_leaf],nums[i]

def find_sum(nums,target):
	left,right = 0,len(nums)-1
	while left < right:
		sum_tmp = nums[left] + nums[right]
		if sum_tmp == target:
			return nums[left],nums[right]
		elif sum_tmp < target:
			left += 1
		else:
			right -= 1
	return False,False


def cal_res(num):
	sum_res = 0
	tmp = 1
	for one in range(1,num+1):
		tmp = tmp * one
		sum_res += tmp
	return sum_res


if __name__ == '__main__':
	# nums = [1,3,5,7,9,13,18,33]
	# num1,num2 = find_sum(nums, 33)
	# print(num1,num2)
	sums = cal_res(3)
	print(sums)





