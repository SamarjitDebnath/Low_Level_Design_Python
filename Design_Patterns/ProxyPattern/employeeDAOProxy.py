from employeeDAO import EmployeeDAO
from employeeIMPL import EmployeeIMPL


class EmployeeDAOProxy(EmployeeDAO):
    def __init__(self):
        self.employDAO_Object: EmployeeDAO = EmployeeIMPL()

    def create(self, client: str, employeeObject: 'EmployeeDAO') -> Exception | None:
        if client == "ADMIN":
            self.employDAO_Object.create(client, employeeObject)
            return
        else:
            raise Exception("Access denied")

    def get(self, client: str, employeeID: int) -> Exception | None:
        if client == "ADMIN" or client == "USER":
            self.employDAO_Object.get(client, employeeID)
        else:
            raise Exception("Access denied")

    def delete(self, client: str, employeeID: int) -> Exception | None:
        if client == "ADMIN":
            self.employDAO_Object.delete(client, employeeID)
        else:
            raise Exception("Access denied")
