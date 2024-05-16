n=int(input())
nums=list(map(int, input().split()))

runningValue=0
maxChange=0
for j in nums:
    runningValue+=1-2*j
    maxChange=max(maxChange, runningValue)
    if runningValue<0:
        runningValue=0
if maxChange==0:
    print(nums.count(1)-1)
else:
    print(maxChange + nums.count(1))
