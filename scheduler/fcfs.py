from typing import List,Tuple
from .process import Process

"""
Since the processes in a OS keeps coming so we would have used heaps/ sets
to handle that but for now using sorted static container would work
because we are simulating a batch OS and not a multiprogramming OS
"""
def fcfs_schedule(processes: List[Process]) -> Tuple[List[Process], List[Tuple[int, int, int]]]:
    """
    FCFS is a  non preemption scheduling, once scheduled no going back , can suffer from convoy effect
    First-Come-First-Serve scheduling simulation.
    Args:
        processes: List of Process objects (unsorted or sorted by arrival_time).
    Returns:
        List of Process objects with updated start_time and finish_time.
    """
    # Sort by arrival time
    queue = sorted(processes, key=lambda p: p.arrival_time) #sort function
    current_time = 0
    finished = []
    timeline = [] # for the actual time it was working, yeah obviously

    for proc in queue:
        # If CPU is idle, advance time to process arrival
        if current_time < proc.arrival_time:
            current_time = proc.arrival_time

        proc.start_time = current_time
        proc.state = "running"

        
        # Run full duration
        start_slice = current_time
        current_time += proc.burst_time
        end_slice = current_time
        
        # Record the single long slice, this will help in making the actual GanttChart
        timeline.append((proc.pid, start_slice, end_slice))
        
        proc.finish_time = current_time

        proc.state = "terminated"

        finished.append(proc)

    return finished, timeline # result is the list of process objects