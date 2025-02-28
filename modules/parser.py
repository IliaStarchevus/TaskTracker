# MAIN
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
    parserAdd.add_argument("description", type=str)
    parserAdd.add_argument("--status", default="todo", choices=("todo", "in-progress", "done"))
    parserAdd.add_argument("--category", default="all")
    parserAdd.add_argument("--tags", type=str, action="extend", nargs="+", default=[])
    parserAdd.set_defaults(func=commands.add)
    
    ## SUBCOMMAND UPDATE 
    parserUpdate = subparsers.add_parser(name="update",
                                         help="Updates data of a task")
    parserUpdate.add_argument("id", type=int)
    
    ### SUBPARSERS UPDATE
    subparsersUpdate = parserUpdate.add_subparsers(dest="property",
                                                   help="Update property of a task")
    
    #### SUBCOMMAND DESCRIPTION
    parserDescription = subparsersUpdate.add_parser(name="description",
                                                    help="Update description")
    parserDescription.add_argument("description", type=str)
    parserDescription.set_defaults(func=commands.update_description)
    
    #### SUBCOMMAND STATUS
    parserStatus = subparsersUpdate.add_parser(name="status",
                                                    help="Update status")
    parserStatus.add_argument("status", type=str, choices=("todo", "in-progress", "done"))
    parserStatus.set_defaults(func=commands.update_status)
    
    #### SUBCOMMAND TAGS
    parserTags = subparsersUpdate.add_parser(name="tags",
                                                    help="Update tags")
    parserTags.add_argument("tags", type=str, nargs="+", action="extend", default=[])
    parserTags.set_defaults(func=commands.update_tags)
    
    
    ## SUBCOMMAND DELETE 
    parserDeleteOne = subparsers.add_parser(name="delete",
                                         help="Deletes task")
    parserDeleteOne.add_argument("id", type=int)
    parserDeleteOne.set_defaults(func=commands.delete)
    
    parserDeleteAll = subparsers.add_parser(name="delete-all",
                                         help="Deletes all tasks")
    parserDeleteAll.add_argument("--key", type=str)
    parserDeleteAll.set_defaults(func=commands.delete_all)
    
    ## SUBCOMMAND MARK
    # parserMark = subparsers.add_parser(name="mark",
    #                                    help="Marks task")
    # parserMark.add_argument("id", type=int)
    # parserMark.add_argument("status", choices=("todo", "in-progress", "done"))
    # parserMark.set_defaults(func=commands.mark)
    
    ## SUBCOMMAND LIST
    parserList = subparsers.add_parser(name="list",
                                       help="Shows a list of tasks")
    parserList.add_argument("--key", default="id", choices=("id", "description", "created", "updated", "status", "category", "tags"))
    parserList.add_argument("--reversed", action="store_true")
    parserList.set_defaults(func=commands.list)
    
    
    # PARSING ARGUMENTS & RUNNING FUNCTIONS
    args = parser.parse_args()
    logger.debug(f"Parsed args: {args}")
    # try: args.func(args)
    # except AttributeError:
    #     parser.print_help()
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