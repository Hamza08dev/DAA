profit = [15, 20, 30, 18, 18, 10, 23, 16, 25]
deadline = [7, 2, 5, 3, 4, 5, 2, 7, 3]
mix = []
for i in range(len(profit)):
    mix.append((profit[i], deadline[i]))

for i in range(len(mix)):
    for j in range(i + 1, len(mix)):
        if mix[i][0] <= mix[j][0]:
            mix[i] , mix[j] = mix[j], mix[i]

job = [0 for i in range(max(deadline))]
ctr = len(job) - 1
tot = 0
for i in range(len(job)):
    if job[ctr] == 0:
        job[ctr] = mix[i][0]
        ctr -= 1
    else:
        continue
print(job)
for i in range(len(job)):
    tot += job[i]
print(tot)