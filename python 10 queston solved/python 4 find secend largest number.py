# 4 Find second largest number
lis = [1 , 2 ,3 ,4 , 5 ,6 , 7, 8 , 9]
count_values  = lis[0]
for i in lis:
    if i > count_values:
        count_values = i
secend_largest = float('-inf')
for i in lis:
    if i != count_values and i > secend_largest:
        secend_largest = i
print(secend_largest)
