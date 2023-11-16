import sys


# job sorting algorithm based on profit and time deadlines
def job_sorting_algorithm(job_i, max_j):
    slots = [None] * max_j
    sequence = []
    total_weight = 0
    print(slots)
    for i in job_i:
        for j in range(1, max_j):
            if slots[i[0] - j] is None and i[0] > 0 and (i[0]-j)>0:
                slots[i[0] - j] = i[0]
                total_weight += j
                sequence.append(i[0])
                break
            '''elif slots[i - 2] is None and i > 0 and (i - 2) >= 0:
                slots[i - 2] = i
                total_weight += j
                sequence.append(i - 1)'''
            else:
                sequence.append(0)

    return sequence, total_weight


# Reading the values from the input.txt to lists through command line
time_weight_gain = []
try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            columns = line.strip().split()
            pair = [int(columns[1]), int(columns[2])]
            time_weight_gain.append(pair)


except IOError:
    print("required input.txt file through command line")

print("list:", time_weight_gain)
sorted_gain_weight = sorted(time_weight_gain, key=lambda pair: pair[1], reverse=True)

max_time = max(pair[0] for pair in sorted_gain_weight)

print("sorted list:", sorted_gain_weight)

seq, tot_weight = job_sorting_algorithm(sorted_gain_weight, max_time)
print(seq, tot_weight)
