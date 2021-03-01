# 공의 개수 n 공의 최대 무게 m
n,m = map(int, input().split())
w = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0]*11

for x in w:
  #각 무게에 해당하는 볼링공의 개수
  array[x] += 1

score = 0

#1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
  #무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
  n -= array[i]
  #B가 선택하는 경우의 수와 곱하기
  score += array[i]*n 

print(score)