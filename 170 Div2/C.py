from collections import Counter

t = int(input())
for _ in range(t):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  counts = Counter(a)
  nums = sorted(counts.keys())
  # print(nums)
  
  max_counts = 0
  left = 0
  total_counts = 0
  
  for right in range(len(nums)):
    if right > 0 and nums[right] - nums[right - 1] > 1:
      left = right
      total_counts = 0
    total_counts += counts[nums[right]]
    while right - left + 1 > k:
      total_counts -= counts[nums[left]]
      left += 1
    max_counts = max(max_counts, total_counts)
  print(max_counts)
