# Define a function for non-preemptive priority scheduling
def priority_scheduling(processes):
    # Sort processes based on priority (lower number means higher priority)
    processes.sort(key=lambda x: x['priority'])

    # Initialize variables
    current_time = 0
    waiting_time = 0
    turnaround_time = 0

    # Print the header
    print(f"{'Process':<10}{'Burst Time':<12}{'Priority':<10}{'Waiting Time':<14}{'Turnaround Time':<16}")

    # Process each process in the sorted list
    for process in processes:
        # Calculate waiting time for the current process
        process['waiting_time'] = current_time

        # Calculate turnaround time for the current process
        process['turnaround_time'] = process['waiting_time'] + process['burst_time']

        # Update total waiting time and turnaround time
        waiting_time += process['waiting_time']
        turnaround_time += process['turnaround_time']

        # Print process details
        print(
            f"{process['id']:<10}{process['burst_time']:<12}{process['priority']:<10}{process['waiting_time']:<14}{process['turnaround_time']:<16}")

        # Update current time
        current_time += process['burst_time']

    # Calculate average waiting time and turnaround time
    avg_waiting_time = waiting_time / len(processes)
    avg_turnaround_time = turnaround_time / len(processes)

    # Print average waiting time and turnaround time
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")


# Example usage
processes = [
    {'id': 'P1', 'burst_time': 10, 'priority': 3},
    {'id': 'P2', 'burst_time': 1, 'priority': 1},
    {'id': 'P3', 'burst_time': 2, 'priority': 4},
    {'id': 'P4', 'burst_time': 1, 'priority': 2},
    {'id': 'P5', 'burst_time': 5, 'priority': 2}
]

# Call the priority scheduling function
priority_scheduling(processes)

