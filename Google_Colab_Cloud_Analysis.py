# CloudSphere - Google Colab Analysis
from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import matplotlib.pyplot as plt

base='/content/drive/MyDrive/CloudSphere/'
df=pd.read_csv(base+'cloud_usage_data.csv')
print(df.head())
print(df.info())
print(df.isnull().sum())

df=df.dropna().copy()
df['Date']=pd.to_datetime(df['Date'])
df.to_csv(base+'cleaned_cloud_data.csv',index=False)

print('Average CPU:',df.CPU_Usage.mean())
print('Average Memory:',df.Memory_Usage.mean())
print('Average Storage:',df.Storage_Usage.mean())

plt.figure(figsize=(9,5))
df.groupby('Service_Type')['CPU_Usage'].mean().plot(kind='bar')
plt.title('Average CPU Usage by Service Type');plt.ylabel('CPU Usage (%)')
plt.tight_layout();plt.savefig(base+'cpu_usage_chart.png');plt.show()

plt.figure(figsize=(9,5))
df['Memory_Usage'].plot(kind='hist',bins=12)
plt.title('Memory Usage Distribution');plt.xlabel('Memory Usage (%)')
plt.tight_layout();plt.savefig(base+'memory_distribution.png');plt.show()

plt.figure(figsize=(9,5))
df.groupby('Service_Name')['Storage_Usage'].mean().plot(kind='bar')
plt.title('Storage Usage by Service')
plt.tight_layout();plt.savefig(base+'storage_usage.png');plt.show()

plt.figure(figsize=(10,5))
df.groupby('Date')['CPU_Usage'].mean().plot()
plt.title('CPU Usage Over Time');plt.ylabel('CPU Usage (%)')
plt.tight_layout();plt.savefig(base+'cpu_over_time.png');plt.show()
