import pandas as pd

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100,87,90], 'Sam': [94,77,90], 'Katie': [100,81,82], 'Bob': [83,65,85]}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1', 'Test2', 'Test3']
print(f"Eva's grades are {grades['Eva']}")
print(f"Sam's grades are {grades.Sam}")
print(f"The results of Test1 are {grades.loc['Test1']}")
print(f"The results of the second test are {grades.iloc[1]}")
print(f"Eva's second test score is {grades.at['Test2', 'Eva']}")
print(f"The first student's (Wally's) third exam score was {grades.iat[2,0]}")
print(grades.describe())
for key, values in grades.iteritems():
    print(f"{key}'s average score is {values.mean()}")
grades = grades.sort_index(ascending=False, axis=0)
grades = grades.sort_index(ascending=True, axis=1)
print(grades)

