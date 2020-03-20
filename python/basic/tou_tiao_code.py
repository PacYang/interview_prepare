#coding=utf-8

# lst = [7864, 284, 347, 7732, 8498]
lst = [384, 38, 48, 92]
#给出一个数组，如 [7864, 284, 347, 7732, 8498]，
#现在需要将数组中的数字拼接起来，如按顺序依次拼接为：786428434777328498，
#数组中的数字拼接顺序可以任意，编写程序，返回「最大的可能拼出的数字」。（以上面数组为例，返回：849878647732347284）

def merge_max_num(lst):
	for i in range(len(lst)-1,0,-1):
		for j in range(i):
			if str(lst[j])+str(lst[j+1]) < str(lst[j+1])+str(lst[j]):
				lst[j], lst[j+1] = lst[j+1], lst[j]
	print(lst)
	return ''.join(str(v) for v in lst)

if __name__ == '__main__':
	max_num = merge_max_num(lst)
	print(max_num)
