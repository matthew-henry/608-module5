import pandas as pd

grades_dict = {'Wally': 87, 'Eva': 100, 'Sam': 94}
grades_list = [87, 100, 94]

#List based exercise
grades = pd.Series(grades_list)
print(f'The first value in the grades series is {grades[0]}.')
print(f'The mean of the grades are {grades.mean()}.')
print(f'The count of grades is {grades.count()}.')
print(f'The minimum grade is {grades.min()}')
print(f'The maximum grade is {grades.max()}')
print(f'The standard deviation is {grades.std()}')
print(f'{grades.describe()}')

#Dict based exercise
grades = pd.Series(grades_dict)
print(f"Eva's score is {grades['Eva']}")
print(f"Wally's score is {grades.Wally}")
print(f'The grades are: {grades.values}')

