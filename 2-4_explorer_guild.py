# 문제 4. 모험가 길드
# 모험가 N명 공포도 X
# 공포도가 X인 모험가는 반드시 X명이상으로 구성한 모험가 그룹에 참여해야함.
# 여행을 떠날 수 있는 그룹 수의 최댓값?

n = int(input())
data = list(map(int, input().split()))
data.sort()
count = 0 # group 내 모험가 수
result = 0 # group 수

for i in data : # 공포도를 낮은것부터 하나씩 확인하기
	count += 1# 현재 그룹에 모험가를 포함시키기
	if count >= i :	# 현재그루벵 포함된 모험가 수가 현재의 공포도 이상이라면 그룹을 결성한다
		result +=1 # 총 그룹의 수 증가시키기
		count = 0 	# 현재 그룹에 포함된 모험가 수 초기화

print(result)	# 총 그룹의 수 출력

