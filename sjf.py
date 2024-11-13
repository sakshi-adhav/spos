# Simplified SJF Preemptive Scheduling

def sjf_preemptive(processes):
    time = 0
    completed = 0
    n = len(processes)
    remaining_burst_time = [p['burst_time'] for p in processes]  # Remaining burst times
    completion_time = [0] * n  # Completion time for each process
    is_completed = [False] * n  # Track if process is completed
    execution_order = []  # Track the execution order of processes

    while completed < n:
        # Find the process with the shortest remaining burst time
        idx = -1
        min_burst_time = float('inf')

        for i in range(n):
            if not is_completed[i] and processes[i]['arrival_time'] <= time and remaining_burst_time[
                i] < min_burst_time:
                min_burst_time = remaining_burst_time[i]
                idx = i

        if idx == -1:  # No process is ready, move time forward
            time += 1
            continue

        # Execute the process for one time unit
        remaining_burst_time[idx] -= 1
        execution_order.append(processes[idx]['pid'])

        # If process is finished
        if remaining_burst_time[idx] == 0:
            is_completed[idx] = True
            completed += 1
            completion_time[idx] = time + 1
            turnaround_time = completion_time[idx] - processes[idx]['arrival_time']
            waiting_time = turnaround_time - processes[idx]['burst_time']
            processes[idx]['turnaround_time'] = turnaround_time
            processes[idx]['waiting_time'] = waiting_time

        # Increment time
        time += 1

    # Print the results
    print(f"{'PID':<6}{'Arrival':<10}{'Burst':<10}{'Completion':<15}{'Turnaround':<15}{'Waiting':<10}")
    for i in range(n):
        print(
            f"{processes[i]['pid']:<6}{processes[i]['arrival_time']:<10}{processes[i]['burst_time']:<10}{completion_time[i]:<15}{processes[i]['turnaround_time']:<15}{processes[i]['waiting_time']:<10}")

    # Display the execution order
    print(f"\nExecution Order: {execution_order}")


# Example Usage
processes = [
    {'pid': 1, 'arrival_time': 1, 'burst_time': 6},
    {'pid': 2, 'arrival_time': 1, 'burst_time': 8},
    {'pid': 3, 'arrival_time': 2, 'burst_time': 7},
    {'pid': 4, 'arrival_time': 2, 'burst_time': 3}
]

sjf_preemptive(processes)
