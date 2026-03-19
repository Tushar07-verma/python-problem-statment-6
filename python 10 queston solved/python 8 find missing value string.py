# 9 missing Values in String
string = ['a' , 'b' , 'd']
for i in range(ord('a') , ord(max(string))+1):
    if chr(i) not in string:
        print("missing values" , chr(i))
