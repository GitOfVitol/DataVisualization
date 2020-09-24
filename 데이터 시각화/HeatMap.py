import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

marathon_2015_2017 = pd.read_csv("../data/marathon_2015to2017_final.csv")

sns.set()

marathon_2015_2017_under60 = marathon_2015_2017[marathon_2015_2017.Age.isin(range(0,60))]

#나이에 따른 Male, Female count
marathon = marathon_2015_2017_under60.groupby('Age')['M/F'].value_counts().unstack().fillna(0)

f, ax = plt.subplots(figsize=(10, 20))
sns.heatmap(marathon, annot=True, fmt="d", linewidths=.5, ax=ax)

plt.show()