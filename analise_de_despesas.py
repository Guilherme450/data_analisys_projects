# Daily expense analysis over two weeks.

# Import useful libraries for data storage, modeling, and analysis.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-dark")

# Inserting the data obtained during two weeks.
data = {
    'total_expenses': [13.5, 6, 5, 50.5, 6, 2, 0, 6, 6, 7, 24.5, 22.4],
    'days_of_the_week': np.arange(1, 13),
    'daily_transport_expenses': [12.5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 5, 6.4],
    'daily_food_expenses': [1, 1, 0, 1, 1, 2, 0, 1, 1, 2, 19.5, 11],
    'daily_other_expenses': [0, 0, 0, 44.9, 0, 0, 0, 0, 0, 0, 0, 0]
}

# Creating a dataframe to identify each variable in data.
df = pd.DataFrame(data)

#print(df)

# Statistical summary of daily total expenses.
summary_total_expenses = df['total_expenses'].describe()

print(summary_total_expenses)

# Count the frequencies of transport and food data.
count_transport = (df['daily_transport_expenses'].sum() / df['total_expenses'].sum()) * 100
count_food = (df['daily_food_expenses'].sum() / df['total_expenses'].sum()) * 100
count_others = (df['daily_other_expenses'].sum() / df['total_expenses'].sum()) * 100 

values = [count_transport, count_food, count_others]
labels = ['Transport', 'Food', 'Others']

sum_total_expenses = df['total_expenses'].sum()

#print(f'Sum of Total Expenses: {sum_total_expenses}')

# Show a bar chart of days x total expenses.
fig, ax = plt.subplots(2, 2, figsize=(9, 6), num='Expense Analysis from: 01/04/24 to 12/04/24')

plt.subplots_adjust(
    left=0.055,
    bottom=0.069,
    top=0.952,
    right=0.97,
    wspace=0.189,
    hspace=0.324
)

ax[0, 0].plot(df['days_of_the_week'], df['total_expenses'], color='purple', marker='o')
ax[0, 0].set_title('Total daily expenses')
ax[0, 0].set_xlabel('Days')
ax[0, 0].set_ylabel('Total expenses ($)')
ax[0, 0].grid()

ax[0, 1].pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#9D00FF', '#DA70D6', '#800080'])
ax[0, 1].set_title('Expenses by area')

ax[1, 0].hist(df['daily_transport_expenses'], color= '#800080', edgecolor='white')
ax[1, 0].set_title('Frequency of transport expenses')
ax[1, 0].set_ylabel('Frequency')
ax[1, 0].set_xlabel('Expenses ($)')

ax[1, 1].hist(df['daily_food_expenses'], color= '#800080', edgecolor='white')
ax[1, 1].set_title('Frequency of food expenses')
ax[1, 1].set_ylabel('Frequency')
ax[1, 1].set_xlabel('Expenses ($)')

plt.show()