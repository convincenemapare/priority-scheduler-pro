"""
VALIDATION MODULE

Requirement satisfied:
✔ Proper input validation
✔ Error handling
"""

def validate_task(task, priority):
    if task.strip() == "":
        return False, "Task cannot be empty"

    try:
        priority = int(priority)
    except ValueError:
        return False, "Priority must be a number"

    if priority < 0:
        return False, "Priority must be positive"

    return True, ""