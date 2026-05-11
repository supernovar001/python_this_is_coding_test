N = int(input())    # 5
plans = list(map(str, input().split())) # R R R U D D

x, y = 1,  1 # 현재 위치
nx , ny = 1, 1
# Up Left Down Right
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U','D']

# 이동계획 하나씩 확인하기
for plan in plans :
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시한다
    if nx < 1 or ny <1 or nx > N or ny > N :
        continue

    # 이동 수행
    x , y = nx , ny

print(x, y)