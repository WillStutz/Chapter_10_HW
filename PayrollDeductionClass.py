class Payroll:

    def __init__(self,description,date,ChargeAmount,EmployeeID):

        self.__description = description
        self.__date = date
        self.__ChargeAmount = ChargeAmount
        self.__EmployeeID = EmployeeID

    def get_description(self):
        return self.__description
    def get_date(self):
        return self.__date
    def get_ChargeAmount(self):
        return self.__ChargeAmount
    def get_EmployeeID(self):
        return self.__EmployeeID

    