import pandas as pd
import matplotlib.pyplot as plt

marathon_2015_2017 = pd.read_csv('../data/marathon_2015to2017_final.csv')

record = pd.DataFrame(marathon_2015_2017, columns=['5K',  '10K',  '15K',  '20K', 'Half',  '25K',  '30K',  '35K',  '40K',  'Official Time']).sort_values(by=['Official Time'])

record.insert(0, 'Rank', range(1, 1 + len(record)))

top100 = record[0:101]


xData = top100.Rank
yData_full = top100['Official Time']
yData_10k = top100['10K']
yData_20k = top100['20K']
yData_30k = top100['30K']

plt.figure(figsize=(15, 10))
plt.plot(xData, yData_full)
plt.plot(xData, yData_10k)
plt.plot(xData, yData_20k)
plt.plot(xData, yData_30k)

plt.show()