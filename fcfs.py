# FCFS Scheduling

def get_arrival_time(process):
    return process['arrival_time']

def fcfs_scheduling(processes):
    # Sort processes by arrival time using the defined function
    processes = sorted(processes, key=get_arrival_time)
    current_time = 0

    for process in processes:
        if current_time < process['arrival_time']:
            current_time = process['arrival_time']
        process['completion_time'] = current_time + process['burst_time']
        process['turnaround_time'] = process['completion_time'] - process['arrival_time']
        process['waiting_time'] = process['turnaround_time'] - process['burst_time']
        current_time += process['burst_time']

    # Display the results with proper alignment
    print(f"{'PID':<6}{'Arrival':<10}{'Burst':<10}{'Completion':<15}{'Turnaround':<15}{'Waiting':<10}")
    for process in processes:
        print(f"{process['pid']:<6}{process['arrival_time']:<10}{process['burst_time']:<10}{process['completion_time']:<15}{process['turnaround_time']:<15}{process['waiting_time']:<10}")

# Example Usage
processes = [
    {'pid': 1, 'arrival_time': 0, 'burst_time': 5},
    {'pid': 2, 'arrival_time': 2, 'burst_time': 3},
    {'pid': 3, 'arrival_time': 8, 'burst_time': 1},
    {'pid': 4, 'arrival_time': 6, 'burst_time': 2}
]

fcfs_scheduling(processes)
