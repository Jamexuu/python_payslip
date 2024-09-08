import datetime
import SSS as sss
import PagIbig as pagibig
import PhilHealth as philhealth
import WithHoldingTax as wtax

print("La Consolacion College Tanauan Payslip")

#display date and time
time = datetime.datetime.now()
date_time = time.strftime("%x")

#employers input
employee_name = str(input("Enter Employee's name: "))
job_pos = str(input("Enter Employee's Job Position: "))
basic_salary = float(input("Enter basic income: "))
loan = 0
other_salary = 0
divider = "\n------------------------------------"

def condition_loan():
    for i in range(9):
        have_loan = str(input("do you have loans? "))
        global loan
        if have_loan == "yes" or have_loan == "Yes" or have_loan == "YES":
            loan = float(input("Enter loan:"))
            break
        elif have_loan == "no" or have_loan == "No" or have_loan == "NO":
            break
        else:
            print("Please enter a valid input...")

for i in range(9):
    have_other = str(input("do you have other salary? "))
    if have_other == "yes" or have_other == "Yes" or have_other == "YES":
        other_salary = float(input("Enter Other Salary: "))
        condition_loan()
        break
    elif have_other == "no" or have_other == "No" or have_other == "NO":
        condition_loan()
        break
    else:
        print("\nPlease enter a valid input...")

gross_income = basic_salary + other_salary

tax = wtax.display_with_holding_tax(
        sss.display_sss(gross_income), philhealth.get_philhealth(basic_salary),
        pagibig.get_pagibig(gross_income), gross_income)

def getTotalDeduction(sss, philh, pagibig, loan, tax):
    return sss + philh + pagibig + loan + tax

def Total(deduction):
    return gross_income - deduction

def toString(arg):
    return str(arg)


with open("payroll.txt", 'w') as slip:
    slip.write("\tLa Consolacion College Tanauan\n")
    slip.write("\t\t\tPAY SLIP")
    slip.write(divider+"\n")
    slip.write("Date\t\t\t: ")
    slip.write(date_time)
    slip.write("\n\nEmployee's Name\t: ")
    slip.write(employee_name)
    slip.write("\n")
    slip.write("Job Position\t: " + job_pos)
    slip.write(divider + "\n")
    slip.write("Earnings")
    slip.write("\n\tBasic Income: " + toString(basic_salary))
    slip.write("\n\tOther Income: " + toString(other_salary))
    slip.write("\n\tGross Income: " + toString(gross_income))
    slip.write(divider)
    slip.write("\nNet Income\n")
    slip.write("\tSSS\t\t\t: " + toString(sss.display_sss(gross_income)))
    slip.write("\n\tPhilHealth\t: " + toString(philhealth.get_philhealth(basic_salary)))
    slip.write("\n\tPag-Ibig\t: " + toString(pagibig.get_pagibig(gross_income)))
    slip.write("\n\tLoans\t\t: " + toString(loan))
    slip.write("\n\tTax\t\t\t: " + toString(round(tax,2)))
    slip.write(divider)
    slip.write("\nTotal deduction : ")
    slip.write(toString(getTotalDeduction(sss.display_sss(gross_income),
                                 philhealth.get_philhealth(basic_salary),
                                 pagibig.get_pagibig(gross_income), loan, tax)))
    slip.write("\nTake Home Pay\t: ")
    slip.write(toString(round(Total(getTotalDeduction(sss.display_sss(gross_income),
                                 philhealth.get_philhealth(basic_salary),
                                 pagibig.get_pagibig(gross_income), loan, tax)), 2)))





