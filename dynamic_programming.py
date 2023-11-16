import sys

def maximize_gain_schedule(jobs):
    # Sort jobs by deadline in ascending order
    jobs.sort(key=lambda x: x[1])

    # Initialize a table to store the maximum gain at each deadline
    max_gain_at_deadline = [0] * (max(job[1] for job in jobs) + 1)

    for job_id, deadline, gain in jobs:
        # Update the table based on the current job's gain and deadline
        for t in range(deadline, 0, -1):
            if max_gain_at_deadline[t] < max_gain_at_deadline[t - 1] + gain:
                max_gain_at_deadline[t] = max_gain_at_deadline[t - 1] + gain

    # Calculate the total gain by summing the maximum gains at each deadline
    total_gain = sum(max_gain_at_deadline)

    # Construct the schedule based on the maximum gain at each deadline
    schedule = [(job[0], max_gain_at_deadline[job[1]]) for job in jobs]

    return schedule, total_gain

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

# Printing sorted input
for job in time_weight_gain:
    print(*job)

schedule, total_gain = maximize_gain_schedule(time_weight_gain)

# Printing schedule and total gain
for job_id, gain in schedule:
    print(f"{job_id} {gain}")

print(total_gain)