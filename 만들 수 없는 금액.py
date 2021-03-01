n = int(input())
num = list(map(int, input().split()))

count = 1

num.sort()

if num[0] != 1:
  print(count)
else:
  for i in num:
    if count < i:
      break     
    count += i
  print(count)

