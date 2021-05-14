# 8.	Company Users
# Write a program that keeps information about companies and their employees.
# You will be receiving a company name and an employee's id, until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# When you finish reading the data, order the companies by the name in ascending order.
# Print the company name and each employee's id in the following format:
# {companyName}
# -- {id1}
# -- {id2}
# -- {idN}

data = input()

companies = {}

while not data == "End":
    company_name, employee = data.split(" -> ")

    if company_name not in companies:
        companies[company_name] = []
    if employee not in companies[company_name]:
        companies[company_name].append(employee)

    data = input()

sorted_companies = sorted(companies.items(), key=lambda kvp: kvp[0])

for company_name, employees in sorted_companies:
    print(company_name)

    for employee in employees:
        print(f"-- {employee}")