def mk_dir(path: str) -> None:
    """Makes folder if it doesn't exist.
    
    ---
    
    ### Arguments
    - `path` `(str)`: leads to a directory.
    """
    if not os.path.exists(path):
        os.mkdir(path)
        logging.debug(f"Created directory: {path=}")
    else:
        logging.debug(f"Path already exists: {path=}")
    
    
def mk_file(path: str) -> None:
    """Makes file if it doesn't exist.
    
    ---
    
    ### Arguments
    - `path` `(str)`: leads to a file.
    """
    if not os.path.exists(path):
        with open(path, "w"):
            mk_json_struct(path)
        logging.debug(f"Created file: {path=}")
    else:
        logging.debug(f"File already exists: {path=}")
        
        
def mk_json_struct(path: str) -> None:
    """Makes structure in JSON-file for storing data into.
    
    ---
    
    ### Arguments
    - `path` `(str)`: leads to a file.
    """
    with open(path, "w") as file:
        json.dump({"tasks": []}, file, indent=2)
    logger.debug(f"Added structure into a file: {path=}")
        
        
def load_data() -> dict:
    """Returns all data from JSON-file in dict type."""
    with open("data/tasks.json", "r", encoding="utf-8") as file:
        return json.load(file)
    
    
def save_data(data) -> None:
    """Saves data into a JSON-file."""
    with open("data/tasks.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def add(task: object) -> None:
    """Saves a task into a file."""
    mk_dir(r"C:\Users\Ilia\Documents\projects\programming_projects\task_tracker\data")
    mk_file(r"C:\Users\Ilia\Documents\projects\programming_projects\task_tracker\data\tasks.json")
    data = load_data()
    tasks = data["tasks"]
    if len(tasks) != 0:
        task.set_id(tasks[-1]["id"] + 1)
    else:
        task.set_id(1)
    task = task.mk_dict()
    tasks.append(task)
    save_data(data)
    logger.info(f"Task added successfully: {task=}")
    print(f"Task added successfully (ID: {task["id"]})")
    
    
def delete(id: int) -> None:
    # VALIDATION
    if type(id) != int:
        errorStr = f"type of \"id\" value should be \"int\", not {type(id)}"
        logger.critical(errorStr)
        raise TypeError(errorStr)
    if id <= 0:
        errorStr =f"id value should not be less or equal to zero"
        logger.critical(errorStr)
        raise ValueError(errorStr)
    
    # DELETION
    data = load_data()
    index = search_index(id, data["tasks"])
    if index != None:
        tasks = data["tasks"]
        task = tasks[index]
        del tasks[index]
        save_data(data)
        logger.info(f"Task deleted successfully: {task=}")
        print(f"Task deleted successfully (ID: {id})")
    else:
        logger.warning(f"Task not found")
        print(f"Task not found")
        
        
def search_index(id: int, tasks: list) -> int:
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
    >>> index = search_index(3, tasks)
    2
    ```
    """
    logger.debug(f"Got arguments: {id=}; {tasks=}")
    # VALIDATION
    if type(tasks) != list:
        errorStr = f"type of \"tasks\" value should be \"list\", not {type(tasks)}"
        logger.critical(errorStr)
        raise TypeError(errorStr)
    if type(id) != int:
        errorStr = f"type of \"id\" value should be \"int\", not {type(id)}"
        logger.critical(errorStr)
        raise TypeError(errorStr)
    if len(tasks) == 0:
        errorStr = f"list lenght should not equal to zero"
        logger.critical(errorStr)
        raise ValueError(errorStr)
    if id <= 0:
        errorStr =f"id value should not be less or equal to zero"
        logger.critical(errorStr)
        raise ValueError(errorStr)
    # SEARCHING
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
        logger.warning(f"Task is not found: index={middle}")
        return None
    else:
        logger.info(f"Task index is found: index={middle}")
        return middle
    
    
def sorted_tasks(tasks: list, key: str, reverse: bool = False) -> list:
    sortedTasks = sorted(tasks, key=lambda task: task[key], reverse=reverse)
    logger.info(f"Sorted tasks by {key} {"reversed" if reverse else ""}")
    return sortedTasks
        
        
if __name__ != "__main__":
    # IMPORTING
    import logging
    import json
    import os
    
    # SETTING LOGGER
    logging.basicConfig(level=logging.DEBUG,
                        format="%(name)s %(levelname)s %(asctime)s %(message)s",
                        filename=r"logs\task-tracker.log",
                        filemode="w")
    logger = logging.getLogger(__name__)