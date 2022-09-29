


class Employee:


    def __init__(self,name,IDnumber,department,JobTitle,MonthlySalary):

        self.__name = name
        self.__IDnumber = IDnumber
        self.__department = department 
        self.__JobTitle = JobTitle
        self.__MonthlySalary = MonthlySalary


    def get_name(self):
        return self.__name
    def get_IDnumber(self):
        return self.__IDnumber
    def get_department(self):
        return self.__department
    def get_JobTitle(self):
        return self.__JobTitle
    def get_MonthlySalary(self):
        return self.__MonthlySalary

    

