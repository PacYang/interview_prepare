#coding=utf-8

s = []
def perm(nums,begin,end):
    global s
    if begin == end:
        s.append(list(nums))
    else:
        for i in range(begin,end):
            nums[begin],nums[i] = nums[i],nums[begin]
            perm(nums,begin+1,end)
            nums[begin],nums[i] = nums[i],nums[begin]

a=[1,2,3]
perm(a,0,len(a))
print(s)
