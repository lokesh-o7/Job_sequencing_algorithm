import sys


# Greedy Scheduling
def get_job_scheduling(jobs):
    n = len(jobs)

    t = get_max_deadline(jobs, n)

    # Sort jobs in descending order
    for i in range(n):
        for j in range(n - 1 - i):
            if jobs[j][2] < jobs[j + 1][2]:
                jobs[j], jobs[j + 1] = jobs[j + 1], jobs[j]

    # Slots for assigning jobs
    slots = [None] * t
    print("initial slots:", slots)
    selected_jobs = [None] * t
    print("initial selected jobs:", selected_jobs)
    profit = 0
    for i in range(n):
        for j in range(min(t - 1, jobs[i][1] - 1), -1, -1):
            if not slots[j]:
                slots[j] = True
                selected_jobs[j] = jobs[i][0]
                profit += jobs[i][2]
                break
    return selected_jobs, profit


def get_max_deadline(jobs, n):
    res = 0
    for i in range(n):
        if jobs[i][1] > res:
            res = jobs[i][1]
    print("deadline job", res)
    return res


def get_input(filepath):
    arr = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            item = list(map(int, line.split()))
            arr.append(item)
        print(arr)
    return arr


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception("Please pass valid arguments. Ex: python test4.py input.txt output.txt")
    file_name = sys.argv[1]
    outfile = sys.argv[2]
    arr = get_input(file_name)
    # Function Call
    selected_jobs, profit = get_job_scheduling(arr)
    with open(outfile, 'w') as f:
        f.write("Output Schedule by end time  \n")
        for i in range(1, len(arr) + 1):
            try:
                f.write("{} {}\n".format(i, selected_jobs.index(i) + 1))
            except:
                f.write("{} {}\n".format(i, 0))
        f.write("Total Gain \n")
        f.write(str(profit))