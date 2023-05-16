def age_calculator(age_list):
    total_age = 0
    for age in age_list:
        total_age += age
    average_age = total_age / len(age_list)
    return average_age
student_ages = [16, 16, 17, 18, 15, 17, 18]
average_age = age_calculator(student_ages)
print(average_age)