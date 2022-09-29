import EmployeeClass as ec
import PayrollDeductionClass as pd

Jimmy_Smith = ec.Employee('Jimmy Smith','58475','Information Systems','Developer',6800)

deduction_1 = pd.Payroll('food court','8/14/2022',22.50,'39119')
deduction_2 = pd.Payroll('gift contribution','8/12/2022',25.00,'58475')
deduction_3 = pd.Payroll('food court','8/17/2022',15.25,'21547')
deduction_4 = pd.Payroll('vending machine','8/22/2022',3.00,'58475')
deduction_5 = pd.Payroll('vending machine','8/5/2022',2.75,'58475')



list1 = [deduction_1,deduction_2,deduction_3,deduction_4,deduction_5]

total_deduction = 0

for i in list1:
    if i.get_EmployeeID() == '58475':
        total_deduction += i.get_ChargeAmount()

net_pay = Jimmy_Smith.get_MonthlySalary() - total_deduction
name = Jimmy_Smith.get_name()
Id_number = Jimmy_Smith.get_IDnumber()
department = Jimmy_Smith.get_department()
gross_pay = Jimmy_Smith.get_MonthlySalary()





print('*** Employee Pay ***')
print('Name: ',name)
print('ID Number: ',Id_number)
print('Department: ',department)
print('Gross Pay: $',gross_pay)
print('Net Pay: $',net_pay)




