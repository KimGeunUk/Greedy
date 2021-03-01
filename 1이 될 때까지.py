#어떠한 수 N이 1이 될때까지 반복적으로 수행

# 숫자가 작을떄
n,m = map(int, input().split())
result = 0

while n>=m:
  while n%m != 0:
    n -= 1
    result += 1
  n //= m
  result += 1

while n>1:
  n -= 1
  result += 1

print(result)

# 숫자가 클때
n, m = map(int, input().split())
result = 0

while True:
  target = (n//m)*m
  result += (n-target)
  n = target

  if n<m:
    break
  
  result += 1
  n //= m

result += (n-1)
print(result)