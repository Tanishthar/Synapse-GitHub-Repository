customers = [[5, 2], [5, 4], [10, 3], [20, 1]]

t=0
sum = 0

for arrival_time, time_required in customers:
    if (arrival_time > t):
        t = arrival_time

    t += time_required
    sum += t - arrival_time

print(f"Average wait time of each customer is {sum/len(customers)}")

# Output
# Average wait time of each customer is 3.25