from abc import ABC, abstractmethod


class EmployeeDAO(ABC):

    @abstractmethod
    def create(self, client: str, employeeObject: 'EmployeeDAO') -> Exception | None:
        pass

    @abstractmethod
    def get(self, client: str, employeeID: int) -> Exception | None:
        pass

    @abstractmethod
    def delete(self, client: str, employeeID: int) -> Exception | None:
        pass
