#coding=utf-8

class test(object):
	"""docstring for test"""
	AAA = 1
	def __init__(self, arg):
		super(test, self).__init__()
		self.arg = arg

	# @classmethod
	@staticmethod
	def haha():
		print('jhaha')

if __name__ == '__main__':
	# print(test().AAA)
	test.haha()