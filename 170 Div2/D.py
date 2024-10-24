import sys
sys.setrecursionlimit(1 << 25)
n, m = map(int, sys.stdin.readline().split())
r = list(map(int, sys.stdin.readline().split()))


attr_positions = []
for idx, val in enumerate(r):
    if val == 0:
        attr_positions.append(idx)

attr_positions.append(n)  
m = len(attr_positions) - 1  


strength_checks = []
intelligence_checks = []
for idx, val in enumerate(r):
    if val < 0:
        strength_checks.append((idx, -val))
    elif val > 0:
        intelligence_checks.append((idx, val))



checks_between_attrs = []
for i in range(m):
    checks = {'S': [], 'I': []}
    start = attr_positions[i]
    end = attr_positions[i+1]
    for idx in range(start, end):
        val = r[idx]
        if val < 0:
            checks['S'].append((-val, idx))
        elif val > 0:
            checks['I'].append((val, idx))
    checks_between_attrs.append(checks)


dp = [ [ -1 ] * (m + 1) for _ in range(m + 1) ]
dp[0][0] = 0


for i in range(1, m + 1):
    for s in range(0, i + 1):
        
        if s > 0 and dp[i - 1][s - 1] != -1:
            passed_checks = dp[i - 1][s - 1]
            
            passed_checks += sum(1 for req, _ in checks_between_attrs[i - 1]['S'] if req <= s)
            passed_checks += sum(1 for req, _ in checks_between_attrs[i - 1]['I'] if req <= (i - s))
            dp[i][s] = max(dp[i][s], passed_checks)
        
        if dp[i - 1][s] != -1:
            passed_checks = dp[i - 1][s]
            
            passed_checks += sum(1 for req, _ in checks_between_attrs[i - 1]['S'] if req <= s)
            passed_checks += sum(1 for req, _ in checks_between_attrs[i - 1]['I'] if req <= (i - s))
            dp[i][s] = max(dp[i][s], passed_checks)


answer = max(dp[m])
print(answer)
