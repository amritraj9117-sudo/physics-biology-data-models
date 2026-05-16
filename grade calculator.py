
grade_intervals = {
    (100, 85): 'A+', (85, 75): 'A-', (75, 65): 'B+', (65, 55): 'B-',
    (55,45): 'C+', (45, 35): 'C-', (35, 25): 'D+', (25, 15): 'D-', (15, 0): 'F'
}

a = int(input('Please enter your marks: '))
b = int(input('What was the full marks: '))
percent = a * 100 / b

def get_grade(percent):
    for (upper, lower), grade in grade_intervals.items():
        
        if lower <= percent <= upper:
            return grade

print(f'Your grade is {get_grade(percent)}')
print(f'Your percentage is {percent:.2f}%')

table = {
    'a+': 4.0, 'a': 4.0, 'a-': 3.7, 'b+': 3.3, 'b': 3.0, 'b-': 2.7,
    'c+': 2.3, 'c': 2.0, 'c-': 1.7, 'd+': 1.3, 'd': 1.0, 'd-': 0.7, 'f': 0
}

flag = True
sum_frequencies = 0
total_points = 0

while flag:
    try:
        frequency = int(input('Please enter the frequency of the grade (or 0 to stop): '))
        if frequency == 0:
            flag = False
            break
        
        l = str(input('Please enter the grade: '))
        l = l.lower()
        
        no = table[l]
        calculated_points = no * frequency
        total_points += calculated_points
        sum_frequencies += frequency

    except KeyError:
        print('Please enter a valid grade from the table and try again.')
        continue

try:
    print(f"Your GPA is {total_points / sum_frequencies:.2f}")
except ZeroDivisionError:
    print("Your GPA is 0")