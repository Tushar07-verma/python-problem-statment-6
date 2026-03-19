# 3 Find second largest number
lis = [1 ,2 , 3 , 4 , 5 , 6 ,7 , 8 ,9]
count = lis[0]
for i in lis:
    if i > count:
        count = i
print(count)
        
