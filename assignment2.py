import sys

'''
Pseudo code:

Read the input.txt file and sort them based on profit

Algorithm
Initialize two empty lists (slots, sequence) one for slot availability
and other for adding the allocated timeline for the job
 
Iterate through the sorted jobs and its deadline:
    check if the highest slot (deadline-1) is available
    if slot is None
    Allocate the slot to that
    add allocated timeline to the sequence list
    elif:
    Decrease the slot value by (deadline-1) and up to 0
    check if the slot is available and allocate it
    add allocated timeline to the sequence list
    else:
    add zero to the sequence list
    
    Computation Complexity:
    job scheduling algorithm - O(n*max_deadline)
    sorting based on profit - O(nlogn)
    reading input and writing - O(n)
     
     Total Complexity is Maximum for - O(n*max_deadline)

'''


def job_sorting_algorithm(jobs, max_deadline):
    # Declare two lists one for availability and one for storing final scheduled jobs
    slots = [None] * max_deadline
    sequence = []
    total_weight = 0

    # iterate through the sorted job list
    for job_id, deadline, gain in jobs:
        for j in range(deadline - 1, -1, -1):  # Allocate the highest job first if not check for slots below the deadline
            if slots[j] is None:
                slots[j] = job_id
                total_weight += gain
                sequence.append((job_id, j + 1))  # Job ID and end time (1-based index)
                break       # Breaking the loop after the job allocation is done
        else:
            # Job couldn't be scheduled within its deadline
            sequence.append((job_id, 0))

    return sequence, total_weight


# Reading input from a file specified in the command line
time_weight_gain = []
try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            columns = line.strip().split()
            pair = (int(columns[0]), int(columns[1]), int(columns[2]))
            time_weight_gain.append(pair)
except IndexError:
    print("Usage: python script.py input.txt")
    sys.exit(1)
except FileNotFoundError:
    print("File not found.")
    sys.exit(1)

# Finding the Max deadline and sorting the given input based on profit
sorted_gain_weight = sorted(time_weight_gain, key=lambda pair: pair[2], reverse=True)
max_time = max(pair[1] for pair in sorted_gain_weight)

# Writing sorted input to output.txt
with open("output.txt", "w") as output_file:
    for job in sorted_gain_weight:
        output_file.write(f"{job[0]} {job[1]} {job[2]}\n")

seq, tot_weight = job_sorting_algorithm(sorted_gain_weight, max_time)

# Writing schedule and total gain to output.txt
with open("output.txt", "a") as output_file:
    for job_id, end_time in seq:
        output_file.write(f"{job_id} {end_time}\n")

    # writing the total profit gain by jobs
    output_file.write(str(tot_weight))
