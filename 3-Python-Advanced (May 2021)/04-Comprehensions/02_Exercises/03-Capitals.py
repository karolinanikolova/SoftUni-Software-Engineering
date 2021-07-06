# 3.	Capitals
# Using a dictionary comprehension, write a program which receives country names on the first line,
# separated by comma and space ", ", and their corresponding capital cities on the second line
# (again separated by comma and space ", "). Print each country with their capital on a separate
# line in the following format: "{country} -> {capital}"

countries = input().split(', ')
capitals = input().split(', ')

print('\n'.join([f"{key} -> {value}" for key, value in {countries[index]: capitals[index] for index in range(len(countries))}.items()]))

# # Option 2 - with zip
# countries = input().split(', ')
# capitals = input().split(', ')
#
# my_dict = {country: capital for country, capital in tuple(zip(countries, capitals))}
#
# [print(f"{country} -> {capital}") for country, capital in my_dict.items()]