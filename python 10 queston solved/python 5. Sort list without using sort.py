# 5. Sort list without using sort()

def my_fun():
    lis = [2 , 1 , 5 , 4]
    for i in range(len(lis)):
        for j in range(i+1 , len(lis)):
            if lis[i] > lis[j]:
                lis[i] , lis[j] = lis[j],lis[i]
    return lis
result = my_fun()
print(result)
