from services import get_task
TASK_ID = 1
TASK_TEXT = 'text task'
TASKS = {TASK_ID: TASK_TEXT}


def test_id_exist():
    task_id = TASK_ID
    result_task = get_task(task_id)
    if not result_task:
        raise KeyError, "Task with this ID is not in taskks"
    if result_task != TASK_TEXT:
        raise ValueError, "Wrong text in task"


def test_id_doesnt_exist():
    task_id = 2
    result_task = get_task(task_id)
    if result_task:
        raise KeyError, "Task with this ID shoult not be in tasks"
