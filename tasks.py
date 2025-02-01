class Tasks:
    def __init__(self):
        self.id: int = 0
        self.description: str = ""
        self.status: str = "to do"
        self.createdAt: str = ""
        self.updatedAt: str = ""

    def add(self, description):
        self.mk_file("data")
        task = {
            "id": 0,
            "status": "to do",
            "createdAt": strftime("%Y-%m-%d %H:%M:%S"),
            "updatedAt": None,
            "description": description,
        }
        data = self.get_data("data")
        tasks = self.get_tasks(data)
        if len(tasks) != 0:
            task["id"] = tasks[-1]["id"] + 1
        else:
            task["id"] = 1
        tasks.append(task)  # добавляет элемент в список
        data["count"] = len(tasks)
        self.set_data("data", data)
        print(f"Task added successfully (id: {task["id"]})")

    def delete(self, id):
        data = self.get_data("data")
        for task in range(data["count"]):
            if data["tasks"][task]["id"] == int(id):
                del data["tasks"][task]
                break
        data["count"] = len(data["tasks"])
        self.set_data("data", data)
        print(f"Task deleted successfully (id: {id})")

    def update(self, id, description):
        self.updatedAt = strftime("%Y-%m-%d %H:%M:%S")
        print(f"Task updated successfully (id: {id}, description: {description}, updated at: {self.updatedAt})")
        
    def mark(self, id, status):
        self.updatedAt = strftime("%Y-%m-%d %H:%M:%S")
        print(f"Task marked successfully (id: {id}, status: {status})")
        
    def list(self):
        ...
    
    # json setup
    def set_structure(self, fileName):
        """Организует структуру внутри файла."""
        structure = {"count": 0, "tasks": []}
        with open(file=f"{fileName}.json", mode="w") as file:
            json.dump(structure, file, indent=2)
        
    def mk_file(self, fileName):
        """Создает файл, если такого не существует, и организует структуру внутри него"""
        if not f"{fileName}.json" in os.listdir():
            with open(file=f"{fileName}.json", mode="w"):
                self.set_structure(fileName)
                
    def get_data(self, fileName) -> dict:
        with open(file=f"{fileName}.json", mode="r", encoding="utf-8") as file: data = json.load(file)
        return data
    
    def get_tasks(self, data) -> list:
        return data["tasks"]

    def set_data(self, fileName, data) -> None:
        with open(file=f"{fileName}.json", mode="w", encoding="utf-8") as file: json.dump(data, file, indent=2)


if __name__ != "__main__":
    from time import strftime
    import json, os
