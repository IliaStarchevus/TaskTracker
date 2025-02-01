class App:
    def __init__(self):
        self.tasks = Tasks()
        self.parser = ArgumentParser(prog="tasks",
                                     description="A program to track tasks.",
                                     epilog="E-mail: iliastarchevus@gmail.com")
        self.add_arguments()
        self.parse()

    def add_arguments(self):
        self.parser.add_argument("command", choices=["add", "update", "delete", "mark", "list"], metavar="command", help="available: %(choices)s")
        self.parser.add_argument("parameters", action="extend", nargs="*", metavar="parameters")
        
    def parse(self):
        self.args = self.parser.parse_args()
        
        command = self.args.command
        parameters = self.args.parameters
        
        # print(self.args)
            
        match command:
            case "add":
                self.tasks.add(parameters[0])
            case "update":
                self.tasks.update(parameters[0], parameters[1])
            case "delete":
                self.tasks.delete(parameters[0])
            case "mark":
                self.tasks.mark(parameters[0], parameters[1])
            case "list":
                self.tasks.list(parameters[0])
            

if __name__ != "__main__":
    from argparse import ArgumentParser

    from tasks import Tasks
