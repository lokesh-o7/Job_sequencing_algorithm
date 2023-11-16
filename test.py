import sys


def job_scheduling(job_list):
    # Sort jobs in decreasing order of gain
    job_list.sort(key=lambda x: x[2], reverse=True)

    # Find the maximum deadline to determine the schedule length
    max_deadline = max(job[1] for job in job_list)
    schedule = [0] * (max_deadline + 1)

    total_gain = 0

    # Iterate through the jobs and schedule them
    for job_id, deadline, gain in job_list:
        # Find the latest available time slot before the deadline
        while deadline > 0 and schedule[deadline] != 0:
            deadline -= 1

        # If a slot is available, allocate the job to that slot
        if deadline > 0:
            schedule[deadline] = job_id
            total_gain += gain

    return schedule, total_gain


# Read the input from the file and convert it to a list of tuples
with open(sys.argv[1], 'r') as file:
    job_list = [tuple(map(int, line.strip().split())) for line in file]

# Run the job scheduling algorithm
schedule, total_gain = job_scheduling(job_list)

# Print the input (sorted by gain) and the schedule
with open('Output.txt', 'w') as file:
    for job in sorted(job_list, key=lambda x: x[2], reverse=True):
        file.write(' '.join(map(str, job)) + '\n')

    file.write('// Output Schedule - Jobs by End Times (0 means not scheduled)\n')
    for job_id in schedule[1:]:
        file.write(str(job_id) + ' ')
    file.write('\n')

    file.write(str(total_gain) + '\n')
