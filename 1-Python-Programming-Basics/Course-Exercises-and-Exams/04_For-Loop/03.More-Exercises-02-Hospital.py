# 2.	Болница
# За даден период от време, всеки ден в болницата пристигат пациенти за преглед. Тя разполага първоначално със 7 лекари.
# Всеки лекар може да преглежда само по един пациент на ден, но понякога има недостиг на лекари, затова останалите
# пациенти се изпращат в други болници. Всеки трети ден, болницата прави изчисления и ако броят на непрегледаните пациенти
# е по-голям от броя на прегледаните, се назначава още един лекар.
# Като назначаването става преди да започне приемът на пациенти за деня.
# Напишете програма, която изчислява за дадения период броя на прегледаните и непрегледаните пациенти.

doctors = 7
days = int(input())
current_day_treated_patients = 0
total_treated_patients = 0
current_day_untreated_patients = 0
total_untreated_patients = 0

for day in range(1, days + 1):
    current_day_coming_patients = int(input())
    if day % 3 == 0 and (total_untreated_patients > total_treated_patients):
            doctors += 1
    if current_day_coming_patients <= doctors:
        current_day_treated_patients = current_day_coming_patients
        total_treated_patients = total_treated_patients + current_day_treated_patients
    else:
        current_day_treated_patients = doctors
        total_treated_patients = total_treated_patients + current_day_treated_patients
        current_day_untreated_patients = current_day_coming_patients - doctors
        total_untreated_patients = total_untreated_patients + current_day_untreated_patients


print(f'Treated patients: {total_treated_patients}.')
print(f'Untreated patients: {total_untreated_patients}.')
