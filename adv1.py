import time

nums = {0,1,2,3,4,5,6,7,8,9}
nums = set(map(str, nums))
morenums = {'zero':'0', 'one': '1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
f = open('input', 'r')
sum = 0
count = 0
while(True):
    line = f.readline()
    if not line:
        break
    min_indices = {}
    max_indices = {}
    for i in morenums.keys():
        if i in line:
            min_indices[line.find(i)] = morenums[i]
            max_indices[line.rfind(i)] = morenums[i]
    for i in nums:
        if i in line:
            min_indices[line.find(i)] = i
            max_indices[line.rfind(i)] = i
    mn = min(min_indices.keys())
    mx = max(max_indices.keys())
    cal = min_indices[mn] + max_indices[mx]
    sum += int(cal)
    count+=1
print(sum)
print(count)