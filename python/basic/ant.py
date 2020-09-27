# 给定一个数组和一个数，都是整数型的，使之满足list[i]+list[j]+...+list[k] = M,求出所有的组合\

def getAll(nums, M):
	total = []
	nums.sort()
	def dfs(tmp,begin,left_num):
		if left_num == 0:
			total.append(tmp[:])
		else:
			for i in range(begin, len(nums)):
				if nums[i] > left_num:
					return
				tmp.append(nums[i])
				dfs(tmp, i+1, left_num-nums[i])
				tmp.pop()
	dfs([], 0, M)
	return total
	
if __name__ == '__main__':
	a = [1,2,3,3,2,1,5]
	M = 6
	print(getAll(a, M))
