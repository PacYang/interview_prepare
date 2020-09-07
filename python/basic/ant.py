# 给定一个数组和一个数，都是整数型的，使之满足list[i]+list[j]+...+list[k] = M,求出所有的组合
total = []
allSet = []
from copy import deepcopy
def getAll(array,notInIndex, M, nowList):
	# print(nowList)
	global total
	for i in range(len(array)):
		notInIndexx = deepcopy(notInIndex)
		nowListt = deepcopy(nowList)
		if i in notInIndexx:
			continue
		if array[i] == M:
			notInIndexx.append(i)
			nowListt.append(array[i])
			notInIndexx.sort()
			if notInIndexx not in allSet:
				total.append(nowListt)
				allSet.append(notInIndexx)
		else:
			notInIndexx.append(i)
			nowListt.append(array[i])
			getAll(array, notInIndexx, M-array[i], nowListt)
      
if __name__ == '__main__':
	a = [1,2,3,3,2,1,5]
	M = 6
	getAll(a, [], M, [])
	print(total)
