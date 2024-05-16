for __ in range(int(input())):
    n, x = map(int,input().split())
    nums = list(map(int, input().split()))
    mi, mx = min(nums), max(nums)
    curDiff = 0
    if 1 < mi:
        curDiff += min(abs(nums[0] - 1), abs(nums[-1] - 1), 2*abs(mi-1))
    if x > mx:
        curDiff += min(abs(nums[0] - x), abs(nums[-1] - x), 2*abs(mx-x))
    for i in range(n-1):
        curDiff += abs(nums[i] - nums[i+1])
    print(curDiff)  

