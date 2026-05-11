##########################################by 나동빈풀이 하단
# 현재 나이트의 위치 입력받기
inputdata = input() #input : a1     # output : 2
column =  ord(inputdata[0])-ord('a')+1
row = int(inputdata[1])

# 나이트가 이동할 수 있는 8가지 방향 정의 
steps = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인하기
count = 0
for step in steps :

    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
        count += 1
print(count)


'''
# 현재 나이트의 위치 입력받기
inputdata = input()
current_position = [int(inputdata[1]), ord(inputdata[0])-ord('a')+1]

# 나이트가 이동할 수 있는 8가지 방향 정의 
steps = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인하기
count = 0
for dx, dy in steps :
    # 이동하고자 하는 위치 확인
    if 0 < current_position[0] + dx and current_position[0] + dx <=8 and \
    0 < current_position[1] + dy and current_position[1] + dy <=8 :
        nx = current_position[0] + dx
        ny = current_position[1] + dy
        count +=1   
        #print(dx,dy,">>>",nx,ny)
print(count)
'''