import pandas as pd
import matplotlib.pyplot as plt

marathon_2015_2017 = pd.read_csv('../data/marathon_2015to2017_final.csv')

MALE_runner = marathon_2015_2017[marathon_2015_2017['M/F'] == 'M']
FEMALE_runner = marathon_2015_2017[marathon_2015_2017['M/F'] == 'F']

plt.figure(figsize=(10, 10))
x_male = MALE_runner.Age
y_male = MALE_runner['Official Time']
x_female = FEMALE_runner.Age
y_female = FEMALE_runner['Official Time']

plt.plot(x_male, y_male, '.', color = 'b', alpha=0.1)
plt.plot(x_female, y_female, '.', color = 'r', alpha=0.1)

plt.xlabel("Age", fontsize=16)
plt.ylabel("Official Time(second)", fontsize=16)
plt.title("Distribution by Running Time and Age", fontsize=20)

plt.show()

