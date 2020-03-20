#coding=utf-8
perms = []
i=0
def perm(listt,stack):
    global perms
    global i
    if not listt:
        print(stack,id(stack))  # 到树的最后，输出结果
        perms.append(list(stack))
    else:  # 没有到树的叶子节点的时候，使用递归继续往下找。
        stack.append(listt[i])
        del listt[i]
        perm(listt,stack)
        listt.insert(i,stack.pop())
        i += 1
    #return perms

listt = [1,2,3,4]
stack=[]
perm(listt,stack)
print(perms)
#print(stack)
