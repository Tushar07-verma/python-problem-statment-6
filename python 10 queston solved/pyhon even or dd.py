# 2 count even or odd number
lis = [1 , 1 , 2 ,2 ,33 ,2 , 3 , 4 , 5]
even = 0
odd = 0
for i in lis:
    if i%2==0:
        even +=1
    else:
        odd +=1
print("here is " , even)
print("here is" , odd)
        
