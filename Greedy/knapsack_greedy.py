Profit = [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147, 86, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,  87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,  314]
Weights = [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,  42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,  3, 86, 66, 31, 65, 0, 79, 20, 64, 58, 17]

ratio = [0 for i in range(len(Profit))]

for i in range(len(Profit)):
    if Weights[i]!= 0:
        ratio[i] = Profit[i]/Weights[i]
    else:
        ratio[i] = Profit[i]

capacity = 800
total_profit = 0
bag = [0 for i in range(capacity)]

fractions = []

sorted_weights = [x for _, x in sorted(zip(ratio, Weights), reverse=True)]
sorted_profits = [x for _, x in sorted(zip(ratio, Profit), reverse=True)]

ratio.sort(reverse= True)
print(ratio)

total_weight = 0

for i in range(capacity):
    if sorted_weights[i] == 0:
        fractions.append(0)
        continue
    if sorted_weights[i] + total_weight <= capacity:
        bag.append(sorted_weights[i])
        total_profit += sorted_profits[i]
        total_weight += sorted_weights[i]
        fractions.append(1)
    else:
        val = (capacity - total_weight) / sorted_weights[i]
        fractions.append(val)
        total_profit += val * sorted_profits[i]
        total_weight += val * sorted_weights[i]
        break

print(total_profit)
