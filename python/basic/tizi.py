#coding=utf-8

def solution(n):
    n_3,n_2,n_1,result = 4,2,1,0
    for i in range(1,n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        else:
            result = n_3 + n_2 + n_1
            n_1 = n_2
            n_2 = n_3
            n_3 = result

    return result


result = solution(6)
print(result)  
