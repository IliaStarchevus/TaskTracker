# VALIDATION
def validate_id(value: int) -> int:
    if type(value) != int:
        errStr = f'Type of value "id" should be "int", not "{type(value).__name__}"'
        logger.critical(errStr)
        raise TypeError(errStr)
    if value <= 0:
        errStr =f'Value "id" should not be less or equal to zero'
        logger.critical(errStr)
        raise ValueError(errStr)
    logger.debug('Value "id" is valid')
    return value


def validate_description(value) -> str:
    return value


def validate_status(value) -> str:
    return value


def validate_category(value) -> str:
    return value


def validate_tags(value) -> list:
    return value


def validate_key(value) -> None:
    return value


def validate_value(value) -> str:
    return value

# COMMANDS
def add(args) -> None:
    description = validate_description(args.description)
    status = validate_status(args.status)
    category = validate_category(args.category)
    tags = validate_tags(args.tags)
    storage.add_task(description, status, category, tags)
    
    
# def update(args) -> None:
#     id = validate_id(args.id)
#     property = args.property
#     match property:
#         case "description":
#             value = args.description
#         case "status":
#             value = args.status
#         case "tags":
#             value = args.tags
#     storage.update_task(id, property, value)


def update_description(args) -> None:
    id = validate_id(args.id)
    description = args.description
    storage.update_task_description(id, description)
    
    
def update_status(args) -> None:
    id = validate_id(args.id)
    status = args.status
    storage.update_task_status(id, status)
    
    
def update_category(args) -> None:
    id = validate_id(args.id)
    category = args.category
    storage.update_task_category(id, category)
    
    
def update_tags(args) -> None:
    id = validate_id(args.id)
    tags = args.tags
    storage.update_task_tags(id, tags)
    

# def mark(args):
#     id = validate_id(args.id)
#     status = validate_status(args.status)
#     storage.mark_task(id, status)
    

def delete(args) -> None:
    id = validate_id(args.id)
    storage.delete_task(id)
    
    
def delete_all(args) -> None:
    key = validate_key(args.key)
    storage.delete_all_tasks(key)
    

def list(args) -> None:
    
    # storage.list_tasks(args.key, args.reverse)
    # return

    data = storage.get_data()
    tasks = storage.get_sorted_tasks(data["tasks"],
                                     args.key,
                                     args.reversed)
    tasksStr = ""
    for task in tasks:
        taskStr = ""
        taskStr += f"id: {task["id"]}\n"
        taskStr += f"- description: {task["description"]}\n"
        taskStr += f"- created: {task["created"]}\n"
        taskStr += f"- updated: {task["updated"]}\n"
        taskStr += f"- status: {task["status"]}\n"
        taskStr += f"- category: {task["category"]}\n"
        taskStr += f"- tags: {[tag + ", " for tag in task["tags"]] if task["tags"] != [] else ""}\n"
        tasksStr += taskStr
    print(tasksStr)


if __name__ != "__main__":
    # IMPORTING
    from . import storage
    
    import logging
    
    # SETTING LOGGER
    logging.basicConfig(level=logging.DEBUG,
                        format="%(name)s %(levelname)s %(asctime)s %(message)s",
                        filename=r"logs\task-tracker.log",
                        filemode="w")
    logger = logging.getLogger(__name__)