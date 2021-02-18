# 모험가 N명 
# 공포도 X

n = int(input())
x = list(map(int, input().split()))
x.sort()

group = 0
count = 0

for i in x:
  count += 1
  if count >= i:
    group += 1
    count = 0



print(group)
