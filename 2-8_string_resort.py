s = input()
s.sort()    # list로 data type 변경됨
result = '' #  문자열 데이터 append
num_sum = 0
for x in s :
    if x.isdigit() == True :    # 숫자합 연산을 위함
        num_sum += int(x)
    else: 
        result += x
print(result+str(num_sum))