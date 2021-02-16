# split 으로 구분하여 n,m,k 입력받기
n,m,k = map(int, input().split())

#n개의 자연수 입력받기 (배열)
data = list(map(int, input().split()))

#오름차순으로 정렬
data.sort()
first = data[-1]    #가장 큰 수
second = data[-2]   #두번째로 큰 수

sum = 0

while True:
  for i in range(k):
    if m==0:
      break
    sum += first
    m -= 1
  if m==0:
    break
  sum += second
  m -= 1

print(sum)

