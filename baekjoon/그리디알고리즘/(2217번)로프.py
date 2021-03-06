import sys
import heapq

N = int(sys.stdin.readline())
ropes = []

for i in range(N):
    #ropes.append(int(sys.stdin.readline()))
    heapq.heappush(ropes, int(sys.stdin.readline()))
#ropes.sort()

answer = len(ropes) * ropes[0]
heapq.heappop(ropes)
for i in range(len(ropes)):
    if answer < ropes[0]*len(ropes):
        answer = ropes[0]*len(ropes)
    heapq.heappop(ropes)
    #print(ropes)

print(answer)
