# 7.	Изготвяне на проекти
# Напишете програма, която изчислява колко часове ще са необходими на един архитект, за да изготви проектите на няколко строителни обекта. Изготвянето на един проект отнема три часа.
architect_name = input()
project_number = int(input())
project_hours = project_number * 3
print(f"The architect {architect_name} will need {project_hours} hours to complete {project_number} project/s.")