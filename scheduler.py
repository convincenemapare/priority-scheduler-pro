import heapq
import pandas as pd
from datetime import datetime

# Priority Queue (Min Heap)
task_queue = []

# List for completed tasks history (Required for Power BI)
completed_tasks_log = []

def add_task(task, priority):
    heapq.heappush(task_queue, (priority, task))
    export_to_powerbi(task_queue)# Update Power BI data source whenever a new task is added

def execute_task():
    if task_queue:
        priority, task = heapq.heappop(task_queue)
        
        # Log data for Power BI visualization
        completed_tasks_log.append({
            "Task": task,
            "Priority": priority,
            "Timestamp": datetime.now().strftime("%H:%M:%S"),
            "Status": "Completed"
        })
        
        # Export the updated log to CSV
        save_for_power_bi()
        
        return priority, task
    return None

def save_for_power_bi():
    if completed_tasks_log:
        df = pd.DataFrame(completed_tasks_log)
        df.to_csv("scheduler_metrics.csv", index=False)

def get_tasks():
    return sorted(task_queue)

def get_completed_tasks():
    # Returns just the task names for your existing GUI listbox
    return [t["Task"] for t in completed_tasks_log]

def delete_task(task_name, priority):
    global task_queue
    try:
        task_queue.remove((priority, task_name))
        heapq.heapify(task_queue)
        return True
    except ValueError:
        return False


def export_to_powerbi(tasks_list, filename="task_data.csv"):
    """
    Converts the list of task dictionaries into a DataFrame 
    and saves it as a CSV for Power BI to read.
    """
    if not tasks_list:
        print("No tasks to export!")
        return

    # Convert your list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(tasks_list)
    
    # Save to CSV (index=False keeps it clean for Power BI)
    df.to_csv(filename, index=False)
    print(f"✅ Data successfully exported to {filename}!")

def export_to_powerbi(heap_data):
    """
    Converts the heap (list of tuples) into a structured DataFrame 
    so Power BI can read it easily.
    """
    if not heap_data:
        return
        
    # Convert the heap tuples into named columns
    df = pd.DataFrame(heap_data, columns=["Priority", "Task_Name"])
    
    # Save the file (index=False keeps the CSV clean)
    df.to_csv("task_data.csv", index=False)
    print("📊 Power BI data source updated!")            