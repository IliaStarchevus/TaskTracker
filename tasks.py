class Tasks:
    def __init__(self):
        self.id: int = 0
        self.description: str = ""
        self.status: str = "todo"
        self.createdAt: str = ""
        self.updatedAt: str = ""

    def add(self, description: str) -> None:
        """Adds a new dict into a list of tasks in "data.json" file.

        Args:
            description (str): String for a description.
        """
        self.mk_file()
        task = {
            "id": 0,
            "status": "todo",
            "createdAt": strftime("%Y-%m-%d %H:%M:%S"),
            "updatedAt": None,
            "description": description,
        }
        data = self.get_data()
        tasks = self.get_tasks(data)
        if len(tasks) != 0:
            task["id"] = tasks[-1]["id"] + 1
        else:
            task["id"] = 1
        tasks.append(task)  # adds new element into a list
        data["count"] = len(tasks)
        self.set_data(data)
        print(f"Task added successfully (ID: {task["id"]})")

    def delete(self, id: int):
        data = self.get_data("data")
        
        # validate id
        try:
            id = int(id)
        except: ValueError("Parameter \"ID\" should contain an integer.")
        
        tasks = self.get_tasks(data)
        
        for index in range(len(tasks)):
            if tasks[index]["id"] == id:
                del tasks[index]; break
        
        data["count"] = len(data["tasks"])
        self.set_data(data)
        print(f"Task deleted successfully (id: {id})")

    def update(self, id, description):
        data = self.get_data("data")
        tasks = data["tasks"]
        
        # validate id
        try:
            id = int(id)
        except: ValueError("Parameter \"ID\" should contain an integer.")
        
        task = self.get_task(tasks, id)
            
        task["description"] = description
        task["updatedAt"] = strftime("%Y-%m-%d %H:%M:%S")
        self.set_data(data)
        print(f"Task updated successfully (ID: {id})")
        
    def mark(self, id: int, status: str):
        # validate status
        if status not in ("todo", "in progress", "done"):
            raise ValueError("Parameter \"status\" should contain one of the following potions: \"todo\", \"in progress\", \"done\"")
        
        # validate id
        try:
            id = int(id)
        except: ValueError("Parameter \"ID\" should contain an integer.")
        
        data = self.get_data("data")
        tasks = data["tasks"]
        task = self.get_task(tasks, id)
            
        task["status"] = status
        task["updatedAt"] = strftime("%Y-%m-%d %H:%M:%S")
        self.set_data(data)
        print(f"Task marked successfully (id: {id}, status: {status})")
        
    def list_tasks(self, filter=None):
        data = self.get_data("data")
        tasks = data["tasks"]
        for task in tasks:
            for key, value in task.items():
                print(f"{key}: {value}")
    
    @staticmethod
    def mk_file(fileName: str = "data") -> None:
        if not f"{fileName}.json" in os.listdir():
            structure = {"count": 0, "tasks": []}
            with open(file=f"{fileName}.json", mode="w") as file:
                json.dump(structure, file, indent=2)
    
    @staticmethod            
    def get_data(fileName: str = "data") -> dict:
        with open(f"{fileName}.json", "r", encoding="utf-8") as file:
            return json.load(file)
    
    @staticmethod
    def get_tasks(data: dict) -> list:
        return data["tasks"]

    @staticmethod
    def get_task(tasks: list, id: int) -> dict | None:
        """Returns dictionary found in list of tasks if it exists.

        Args:
            tasks (list): List of tasks that contains all the tasks dicts.
            id (int): ID of each task.

        Returns:
            dict | None: Dict with all data of a task or None if it doesn't exist.
        """
        for task in tasks:
            return task if task["id"] == id else None
    
    @staticmethod
    def set_data(data: dict, fileName: str = "data") -> None:
        with open(f"{fileName}.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)


if __name__ != "__main__":
    from time import strftime
    import json, os
