# COMMANDS
def add_task(args):
    task: Task = Task(headline=args.headline,
                      description=args.description,
                      status=args.status,
                      category=args.category,
                      tags=args.tags)
    storage.add(task)
    
    
def update_task(args):
    data = storage.load_data()
    tasks = data["tasks"]
    task = tasks(storage.search_index(args.id))
    

def delete_task(args):
    storage.delete(args.id)
    

def list_tasks(args):
    data = storage.load_data()
    tasks = storage.sorted_tasks(data["tasks"],
                                 args.key,
                                 args.reverse)
    tasksStr = ""
    for task in tasks:
        taskStr = ""
        taskStr += f"id: {task["id"]}\n"
        taskStr += f"- headline: {task["headline"]}\n"
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
    from .task import Task
    from . import storage
    import logging
    
    # SETTING LOGGER
    logging.basicConfig(level=logging.DEBUG,
                        format="%(name)s %(levelname)s %(asctime)s %(message)s",
                        filename=r"logs\task-tracker.log",
                        filemode="w")
    logger = logging.getLogger(__name__)