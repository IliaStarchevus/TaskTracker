# DECORATOR
def log_func(func):
    def wrapper(*args, **kwargs):
        # logger.debug(f"Running function: {func.__name__}")
        func(*args, **kwargs)
        logger.debug(f"Finished function: {func.__name__}")
    return wrapper   

# MAIN
@log_func
def main():
    # MAIN PARSER
    parser = ArgumentParser(prog="task-tracker",
                            description="CLI program for tracking tasks",
                            epilog="Inspired by roadmap.sh")
    
    # SUBPARSERS
    subparsers = parser.add_subparsers(dest="command",
                                       help="Allowed commands")
    
    ## SUBCOMMAND ADD
    parserAdd = subparsers.add_parser(name="add",
                                      help="Adds a new task")
    parserAdd.add_argument("headline", default="")
    parserAdd.add_argument("description", default="")
    parserAdd.add_argument("--status", default="todo", choices=("todo", "in-progress", "done"))
    parserAdd.add_argument("--category", default="all")
    parserAdd.add_argument("--tags", type=str, action="extend", nargs="+", default=[])
    parserAdd.set_defaults(func=commands.add_task)
    
    ## SUBCOMMAND UPDATE 
    parserUpdate = subparsers.add_parser(name="update",
                                         help="Updates data of a task")
    parserUpdate.add_argument("id", type=int)
    parserUpdate.add_argument("--headline")
    parserUpdate.add_argument("--description")
    parserUpdate.add_argument("--status", choices=("todo", "in-progress", "done"))
    parserUpdate.add_argument("--category")
    parserUpdate.add_argument("--tags", type=str, action="extend", nargs="+", default=[])
    parserUpdate.set_defaults(func=commands.update_task)
    
    ## SUBCOMMAND DELETE 
    parserDelete = subparsers.add_parser(name="delete",
                                         help="Deletes task")
    parserDelete.add_argument("id", type=int)
    parserDelete.set_defaults(func=commands.delete_task)
    
    ## SUBCOMMAND LIST
    parserList = subparsers.add_parser(name="list",
                                       help="Shows a list of tasks")
    parserList.add_argument("--key", default="id", choices=("id", "headline", "description", "created", "updated", "status", "category", "tags"))
    parserList.add_argument("--reverse", action="store_true")
    parserList.set_defaults(func=commands.list_tasks)
    
    # PARSING ARGUMENTS & RUNNING FUNCTIONS
    args = parser.parse_args()
    logger.info(f"Got args: {args._get_kwargs()}")
    args.func(args)


if __name__ != "__main__":
    # IMPORTING
    import logging
    from argparse import ArgumentParser
    from . import commands
    
    # SETTING LOGGER
    logging.basicConfig(level=logging.DEBUG,
                        format="%(name)s %(levelname)s %(asctime)s %(message)s",
                        filename=r"logs\task-tracker.log",
                        filemode="w")
    logger = logging.getLogger(__name__)