#coding = utf-8

import time
import threading

def tstart(args):
	time.sleep(0.5)
	print(f'{args} running ....')

if __name__ == '__main__':
	t1 = threading.Thread(target=tstart, args=('thread 1',))
	t2 = threading.Thread(target=tstart, args=('thread 2',))
	t1.start()
	t2.start()
	print('this is main function')
