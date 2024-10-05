import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")

data = sns.load_dataset("dowjones")

print(data.head())

#sns.displot(data, x='day', kind='hist')

#plt.show()