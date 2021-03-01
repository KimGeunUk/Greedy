num = input()

result = int(num[0])

for i in range(1, len(num)):
  a = int(num[i])
  if result <= 1 or a <= 1:
    result += a
  else:
    result *= a
    

print(result)