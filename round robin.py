def round_robin(processes, quantum):
    n = len(processes)
    remaining_burst_time = [process['burst_time'] for process in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    current_time = 0
    arrival_time = [process['arrival_time'] for process in processes]
    execution_log = []

    while True:
        done = True
        for i in range(n):
            if remaining_burst_time[i] > 0 and arrival_time[i] <= current_time:
                done = False
                if remaining_burst_time[i] > quantum:
                    execution_log.append((current_time, processes[i]['id'], 'runs'))
                    current_time += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    execution_log.append((current_time, processes[i]['id'], 'runs'))
                    current_time += remaining_burst_time[i]
                    waiting_time[i] = current_time - processes[i]['burst_time'] - arrival_time[i]
                    remaining_burst_time[i] = 0
                    execution_log.append((current_time, processes[i]['id'], 'completes'))

        if done:
            break

    for i in range(n):
        turnaround_time[i] = processes[i]['burst_time'] + waiting_time[i]

    print(f"{'Process':<10}{'Arrival Time':<14}{'Burst Time':<12}{'Waiting Time':<14}{'Turnaround Time':<16}")
    for i in range(n):
        print(f"{processes[i]['id']:<10}{processes[i]['arrival_time']:<14}{processes[i]['burst_time']:<12}{waiting_time[i]:<14}{turnaround_time[i]:<16}")

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

    print("\nExecution Flow:")
    print(f"{'Time':<6}{'Process':<10}{'Action':<12}")
    for log in execution_log:
        time, process, action = log
        print(f"{time:<6}{process:<10}{action:<12}")

# Example usage
processes = [
    {'id': 'P1', 'arrival_time': 0, 'burst_time': 10},
    {'id': 'P2', 'arrival_time': 1, 'burst_time': 5},
    {'id': 'P3', 'arrival_time': 2, 'burst_time': 8}
]
quantum = 2

round_robin(processes, quantum)

