# DECORATORS
def process_data(func):
    def wrapper(*args, **kwargs):
        mk_dir(r"C:\Users\Ilia\Documents\projects\programming_projects\task_tracker\data")
        mk_file(r"C:\Users\Ilia\Documents\projects\programming_projects\task_tracker\data\tasks.json")
        data = get_data()
        set_data(func(data, *args, **kwargs))
    return wrapper


# FILES
def mk_dir(path: str) -> None:
    """Makes folder if it doesn't exist.
    
    ---
    
    ### Arguments
    - `path` `(str)`: leads to a directory.
    """
    if not path.exists(path):
        mkdir(path)
        logger.debug(f"Created directory: {path=}")
    else:
        logger.debug(f"Path already exists: {path=}")
    
    
def mk_file(path: str) -> None:
    """Makes file if it doesn't exist.
    
    ---
    
    ### Arguments
    - `path` `(str)`: leads to a file.
    """
    if not path.exists(path):
        with open(path, "w"):
            mk_json_struct(path)
        logger.debug(f"Created file: {path=}")
    else:
        logger.debug(f"File already exists: {path=}")
        
        
def mk_json_struct(path: str) -> None:
    """Makes structure in JSON-file for storing data into.
    
    ---
    
    ### Arguments
    - `path` `(str)`: leads to a file.
    """
    with open(path, "w") as file:
        dump({"tasks": []}, file, indent=2)
    logger.debug(f"Added structure into a file: {path=}")


# SETTERS & GETTERS
def get_data() -> dict:
    with open("data/tasks.json", "r", encoding="utf-8") as file:
        data = load(file)
        logger.debug(f"Got data: {data}")
        return data
    
    
def set_data(data) -> None:
    with open("data/tasks.json", "w", encoding="utf-8") as file:
        dump(data, file, indent=2)
    logger.debug(f"Set data: {data}")
    
    
def get_sorted_tasks(tasks: list, key: str, reversed: bool = False) -> list:
    sortedTasks = sorted(tasks, key=lambda task: task[key], reverse=reversed)
    logger.info(f"Sorted tasks by {key} {"reversed" if reversed else ""}")
    return sortedTasks
        
        
def get_index(id: int, tasks: list) -> int:
    """Searches task index in a list of tasks using binary search algorithm.
    
    ---
    
    ### Arguments
    - `tasks` `(list)`: a list that contains items including data of each task.
    - `id` `(int)`: an integer leading to a task id.
    
    ---
    
    ### Raises
    - `TypeError`: raises if type of values of arguments are not valid.
    - `ValueError`: raises if lenght of list `tasks` equals to zero or value of `id` is less or equal to zero.
    
    ---
    
    ### Returns
    - `int`: an integer leading to item index in a list of tasks.
    
    ---
    
    ### Example
    ```python
    >>> index = get_index(id=3, tasks=data["tasks"])
    2
    ```
    """
    validate_id(id)
    validate_tasks(tasks)
    lenght = len(tasks)
    low = 0
    high = lenght - 1
    middle = lenght // 2
    while tasks[middle]["id"] != id and low <= high:
        if id < tasks[middle]["id"]:
            high = middle - 1
        elif id > tasks[middle]["id"]:
            low = middle + 1
        middle = (low + high) // 2
    if low > high:
        logger.info(f"Did not get task index")
        return None
    else:
        logger.info(f"Got task index: {middle}")
        return middle


# VALIDATION
def validate_id(value: int) -> None:
    if type(value) != int:
        errStr = f'Type of value "id" should be "int", not "{type(value).__name__}"'
        logger.critical(errStr)
        raise TypeError(errStr)
    if value <= 0:
        errStr =f'Value "id" should not be less or equal to zero'
        logger.critical(errStr)
        raise ValueError(errStr)
    logger.info('Value "id" is valid')
    

def validate_tasks(value: list) -> None:
    if type(value) != list:
        errStr = f'Type of value "tasks" should be "list", not {type(value).__name__}'
        logger.critical(errStr)
        raise TypeError(errStr)
    if len(value) == 0:
        errStr = f"List lenght should not be equal to zero"
        logger.critical(errStr)
        raise ValueError(errStr)
    logger.info('Value "tasks" is valid')


# COMMANDS
@process_data
def add_task(data, description: str, status: str, category: str, tags: list) -> dict:
    task = {
        "id": 0,
        "description": description,
        "created": strftime("%Y-%m-%d %H:%M:%S"),
        "updated": strftime("%Y-%m-%d %H:%M:%S"),
        "status": status,
        "category": category,
        "tags": tags
    }
    if len(data["tasks"]) != 0:
        task["id"] = data["tasks"][-1]["id"] + 1
    else:
        task["id"] = 1
    data["tasks"].append(task)
    infoStr = f"Task added successfully (ID: {task["id"]})"
    logger.info(infoStr)
    print(infoStr)
    return data
    

@process_data
def delete_task(data, id: int) -> dict:
    if len(data["tasks"]) == 0:
        infoStr = f"Task list is already empty"
        logger.info(infoStr)
        print(infoStr)
        return data
    index = get_index(id, data["tasks"])
    if index != None:
        del data["tasks"][index]
        infoStr = f"Task deleted successfully (ID: {id})"
    else:
        infoStr = "Task is not found"
    logger.info(infoStr)
    print(infoStr)
    return data
            

@process_data
def delete_all_tasks(data, key: str) -> dict:
    if data["tasks"] != []:
        data["tasks"] = []
        infoStr = "All tasks deleted successfully"
    else:
        infoStr = "Task list is already empty"
    logger.info(infoStr)
    print(infoStr)
    return data
    

@process_data
def update_task(data, id: int, key: str, value) -> dict:
    if key == "id" or key == "updated" or key == "created" or key == "status" or key == "tags":
        infoStr = f'Can not change value "{key}"'
        logger.info(infoStr)
        print(infoStr)
        return data
    index = get_index(id, data["tasks"])
    if data["tasks"][index][key] == value:
        infoStr = f'Task key "{key}" is already have value "{value}"'
    else:
        data["tasks"][index][key] = value
        data["tasks"][index]["updated"] = strftime("%Y-%m-%d %H:%M:%S")
        infoStr = f"Task is updated successfully (ID: {id})"
    logger.info(infoStr)
    print(infoStr)
    return data


@process_data
def mark_task(data, id: int, status: str) -> dict:
    index = get_index(id, data["tasks"])
    if data["tasks"][index]["status"] == status:
        infoStr = f'Task is already marked as {status}'
    else:
        data["tasks"][index]["status"] = status
        infoStr = f'Marked task as {status} (ID: {id})'
    logger.info(infoStr)
    print(infoStr)
    data["tasks"][index]["updated"] = strftime("%Y-%m-%d %H:%M:%S")
    return data


@process_data
def list_tasks(data, key: str, reversed: bool) -> dict:
    tasks = get_sorted_tasks(data["tasks"],
                             key,
                             reversed)
    tasksStr = ""
    for task in tasks:
        taskStr =  f"\nID: {task["id"]} | Created: {task["created"]} | Updated: {task["updated"]} |\n"
        taskStr += f"Status: {task["status"]} | Category: {task["category"]} | Tags: {[tag + "; " for tag in task["tags"]] if task["tags"] != [] else ""} |\n"
        taskStr += f"   {task["description"]}\n"
        tasksStr += taskStr
    print(tasksStr)
    return data
        
        
if __name__ != "__main__":
    # IMPORTING
    import logging
    from json import load, dump
    from os import mkdir, path
    from time import strftime
    
    # SETTING LOGGER
    logging.basicConfig(level=logging.DEBUG,
                format="%(name)s %(levelname)s %(asctime)s %(message)s",
                filename=r"logs\task-tracker.log",
                filemode="w")
    logger = logging.getLogger(__name__)