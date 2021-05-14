# 5.	The Office
# You Will Receive Two Lines of Input:
# a List of Employee's Happiness As String with Numbers Separated by a Single Space and a Happiness Improvement Factor (Single Number). ' \
#                   'Your Task is to Find Out If the Employees Are Generally Happy in Their Office. To Do That You Have to Increase Their Happiness by Multiplying the All the Employee's Happiness (the Numbers from the List) by the Factor, Filter the Employees Which Happiness is Greater Than or Equal to the Average in the New List and Print the Result
# There are two types of output:
# •	If the half or more of the employees have happiness >= than the average: "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise: "Score: {happy_count}/{total_count}. Employees are not happy!"

employee_happiness = map(int, input().split())
# employee_happiness = [int(el) for el in input().split()]
factor = int(input())

factored_employee_happiness = list(map(lambda el: factor * el, employee_happiness))
# factored_employee_happiness = [el * factor for el in employee_happiness]

average_happiness = sum(factored_employee_happiness) / len(factored_employee_happiness)
factored_employee_happiness_filtered = list(filter(lambda el: el >= average_happiness, factored_employee_happiness))
# factored_employee_happiness_filtered = [el for el in factored_employee_happiness if el >= average_happiness]

count_employees = len(factored_employee_happiness)
count_very_happy_employees = len(factored_employee_happiness_filtered)

if count_very_happy_employees >= count_employees / 2:
    print(f"Score: {count_very_happy_employees}/{count_employees}. Employees are happy!")
else:
    print(f"Score: {count_very_happy_employees}/{count_employees}. Employees are not happy!")
