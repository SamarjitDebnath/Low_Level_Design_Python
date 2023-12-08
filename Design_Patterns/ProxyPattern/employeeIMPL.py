from employeeDAO import EmployeeDAO
from employeeDo import EmployeeDO


class EmployeeIMPL(EmployeeDAO):

    def create(self, client: str, employeeObject: EmployeeDAO) -> Exception | None:
        print(f"{client} - Created a row of {employeeObject} in the Employee table...")

    def get(self, client: str, employeeId: int) -> Exception | EmployeeDO:
        print(
            f"{client} - Fetching data from database with {employeeId} from database...")
        return EmployeeDO(employeeId)

    def delete(self, client: str, employeeId: int) -> Exception | None:
        print(f"{client} - Deleting data with {employeeId} from database...")
