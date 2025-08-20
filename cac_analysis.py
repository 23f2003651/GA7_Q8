# 23f2003651@ds.study.iitm.ac.in
import pandas as pd
import matplotlib.pyplot as plt

# Quarterly CAC data
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'CAC': [224.74, 226.22, 232.29, 229.02]
}

df = pd.DataFrame(data)
df['Average_CAC'] = df['CAC'].mean()
industry_target = 150

plt.figure(figsize=(8,5))
plt.plot(df['Quarter'], df['CAC'], marker='o', label='Company CAC')
plt.axhline(industry_target, color='red', linestyle='--', label='Industry Target (150)')
plt.title('Quarterly Customer Acquisition Cost (CAC)')
plt.ylabel('CAC')
plt.xlabel('Quarter')
plt.ylim(140, max(df['CAC']) + 10)
plt.legend()
plt.grid(True)
plt.savefig('cac_trend.png')
plt.show()
