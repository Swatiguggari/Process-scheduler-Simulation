import threading
import time
import queue

# Process class
class Process:
    def _init_(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.wait_time = 0
        self.turnaround_time = 0

# First Come First Serve (FCFS) Scheduling
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)
    time_elapsed = 0
    print("\nFCFS Scheduling:")
    for process in processes:
        if time_elapsed < process.arrival_time:
            time_elapsed = process.arrival_time
        process.wait_time = time_elapsed - process.arrival_time
        process.turnaround_time = process.wait_time + process.burst_time
        time_elapsed += process.burst_time
        print(f"Process {process.pid} - Waiting Time: {process.wait_time}, Turnaround Time: {process.turnaround_time}")

# Round Robin Scheduling
def round_robin_scheduling(processes, quantum):
    queue = processes[:]
    time_elapsed = 0
    print("\nRound Robin Scheduling:")
    
    while queue:
        process = queue.pop(0)
        if process.remaining_time > quantum:
            process.remaining_time -= quantum
            time_elapsed += quantum
            queue.append(process)
        else:
            time_elapsed += process.remaining_time
            process.remaining_time = 0
            process.turnaround_time = time_elapsed - process.arrival_time
            process.wait_time = process.turnaround_time - process.burst_time
            print(f"Process {process.pid} - Waiting Time: {process.wait_time}, Turnaround Time: {process.turnaround_time}")

# Priority Scheduling
def priority_scheduling(processes):
    processes.sort(key=lambda x: (x.priority, x.arrival_time))  # Lower priority value = higher priority
    time_elapsed = 0
    print("\nPriority Scheduling:")
    for process in processes:
        if time_elapsed < process.arrival_time:
            time_elapsed = process.arrival_time
        process.wait_time = time_elapsed - process.arrival_time
        process.turnaround_time = process.wait_time + process.burst_time
        time_elapsed += process.burst_time
        print(f"Process {process.pid} - Priority: {process.priority}, Waiting Time: {process.wait_time}, Turnaround Time: {process.turnaround_time}")

# Example Usage
if __name__ == "_main_":
    processes = [
        Process(1, 0, 8, 3),
        Process(2, 1, 4, 1),
        Process(3, 2, 9, 2),
        Process(4, 3, 5, 4)
    ]
    
    fcfs_scheduling(processes)
    round_robin_scheduling(processes, quantum=3)
    priority_scheduling(processes)