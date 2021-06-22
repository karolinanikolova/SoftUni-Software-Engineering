# Write a function that receives a grade between 2.00 and 6.00 and prints the corresponding grade in words
# •	2.00 – 2.99 - "Fail"
# •	3.00 – 3.49 - "Poor"
# •	3.50 – 4.49 - "Good"
# •	4.50 – 5.49 - "Very Good"
# •	5.50 – 6.00 - "Excellent"

def convert_grade_to_text_grade(grade_as_num):
    if 2 <= grade_as_num <= 2.99:
        return "Fail"
    elif 3 <= grade_as_num <= 3.49:
        return "Poor"
    elif 3.5 <= grade_as_num <= 4.49:
        return "Good"
    elif 4.5 <= grade_as_num <= 5.49:
        return "Very Good"
    elif 5.5 <= grade_as_num <= 6:
        return "Excellent"


grade = float(input())
result = convert_grade_to_text_grade(grade)

print(result)
