from employeeDAOProxy import EmployeeDAOProxy


def main():
    empObject = EmployeeDAOProxy()
    try:
        empObject.delete("USER", 1)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
