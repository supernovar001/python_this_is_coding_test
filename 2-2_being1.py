# 어떤 수 n이 1이 될 때 까지, 1번 혹은 2번 과정을 수행해야하는 횟수의 최솟값을 출력한다.
# 1. N에서 1을 뺀다 (n-1)
# 2. N을 K로 나눈다. (n/k) when n/k == n//k
# 1번 혹은 2번 과정을 수행해야하는 최소 횟수를 구한다.

# keyboard input
n, k = map(int, input().split())    # 25 5 
count = 0

while n > 1 :       ## 수정 version
# while n >= k:     ## 잘못된 풀이
    target = n // k * k
    count += (n - target)   # N-1 연산 횟수(1)
    
    n = target      ## 추가
    if n < k :      ## 추가
        break

    n = n // k
    count +=1       ### N%K 연산 횟수

#### N-1 연산 횟수 (2)
count += (n-1)
print(f"n : {n}, count : {count}")


