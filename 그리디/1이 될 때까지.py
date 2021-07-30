# N이 K 이상인 경우와 아닌 경우로 나누어 진행
# N이 K 이상인 경우 : N에서 1을 빼거나 / K로 나눈다
# N이 K보다 작아진 경우 : N이 1이 될 때까지 -1 해준다

n, k = map(int, input().split())
result = 0

while n >= k:    # n이 k보다 크거나 같을 때만
  
  while n % k != 0:    # n이 k의 배수가 아닌 경우
    n -= 1
    result += 1
    
  n //= k
  result += 1
  

while n > 1:    # 마지막 남은 수에 대하여 -1 반복
  n -= 1
  result += 1
  
print(result)
