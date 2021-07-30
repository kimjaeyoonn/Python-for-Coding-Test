# 각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때
# 모든 숫자를 확인하여 숫자 사이에 '×' 혹은 '+' 를 넣어 결과적으로 만들어질 수 있는 가장 큰 수 ?



data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):    # 두 번째 숫자부터 확인
  # 두 수 중에서 하나라도 0 혹은 1인 경우, 곱하기보다는 더하기 수행이 더 효율적
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
   else:
    result *= num
    
print(result)
  
