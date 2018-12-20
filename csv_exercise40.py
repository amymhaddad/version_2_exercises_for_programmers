import csv

FILENAME = 'data_exercise40.txt'

user_search = input("Enter your search: ")
normalized_user_search = user_search.title()

with open(FILENAME, newline='') as csvfile:
        linereader = csv.reader(csvfile, delimiter=',')
        list_of_employee_data = []
        for employee in linereader:
                list_of_employee_data.append(employee)

headers = "   ".join(list_of_employee_data[0])
row_of_dashes = '-' * len(headers)

employee_data = ''

for employee in list_of_employee_data[1:]:
        full_name = employee[0] + ' ' + employee[1]
        position = employee[2]
        separation_date = employee[3]

        if normalized_user_search in full_name:
                employee_data += full_name + '  |  ' + position + '  |  ' + separation_date

final_format = f"{headers}\n{row_of_dashes}\n{employee_data}"
print(final_format)
