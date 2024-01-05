import time

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

start_time = time.time()
data.sort()

print((M // K) * data[N-1] *K + (M % K) * data[N-2])

end_time = time.time()

execution_time = end_time - start_time
print(f"실행 시간: {execution_time} 초")
