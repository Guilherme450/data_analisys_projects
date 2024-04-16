import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as st

plt.style.use("seaborn-v0_8-dark")

# creating three fictional data that describes variables like name, gender and grade.
classmate_name = [
    'antonio', 'carla', 'fabiana',
    'murilo', 'paulo', 'wilma'
]

classmate_gender = [
    'male', 'female', 'female',
    'male', 'male', 'female'
]

classmate_grade = np.array([6.5, 9, 7.5, 5, 8.5, 7], dtype=float)

# a function to modify each string in a iterable to title style.
def adjust_list_elements_to_title(iterable):
    '''This function adds the built-in function title() to each string in a list.
    args:
        iterable(list): A set of strings.
    
    return(list): In the end of the process, the function will return a list of strings in a title form.
    
    '''
    index = 0

    if isinstance(iterable, str):

        for i in iterable:
            classmate_name[index] = i.title()

            index += 1
        return iterable

    return False

adjust_list_elements_to_title(classmate_name)
adjust_list_elements_to_title(classmate_gender)

# appending data to a dictionary for posterior use in a pandas datafame.
classmate_grade_data = {
    "classmate_name": classmate_name,
    "classmate_grade": classmate_grade,
    "classmate_gender": classmate_gender
}

classmate_dataframe = pd.DataFrame(classmate_grade_data)

# summary of statistics using pandas.
summary_classmate_grades = classmate_dataframe.describe() # we use the .describe() method to see statistics.

#print(f'The summary statistic of classmate grades is: {summary_classmate_grades}')

# mean of classmate's grades by gender, using the groupby() method.
mean_grade_by_gender = classmate_dataframe[['classmate_gender', 'classmate_grade']].groupby('classmate_gender').describe()
#print(mean_grade_by_gender)

filtering_male = classmate_dataframe[classmate_dataframe['classmate_gender'] == 'male']
filtering_female = classmate_dataframe[classmate_dataframe['classmate_gender'] == 'female']

print(classmate_dataframe)

using_loc = classmate_dataframe.loc[5]

print(using_loc)

# plot a graph that contains the name and grade of each classmate.
fig, ax = plt.subplots(2, 1, figsize=(6, 4))

plt.subplots_adjust(
    bottom=0.112,
    top=0.933,
    hspace=0.589
)

ax[0].plot(filtering_male['classmate_name'], filtering_male['classmate_grade'], marker='o', color='red')

ax[0].set_xlabel('Name')
ax[0].set_ylabel('Grade')
ax[0].set_title('Grades of male classmate')
ax[0].grid()

ax[1].plot(filtering_female['classmate_name'], filtering_female['classmate_grade'], marker='o', color='red')

ax[1].set_xlabel('Name')
ax[1].set_ylabel('Grade')
ax[1].set_title('Grades of female classmate')
ax[1].grid()

plt.show()