import pandas as pd 
import matplotlib.pyplot as plt 
 
df = pd.read_csv('PS_20174392719_1491204439457_log.csv', nrows=500000) 
 
print(df.head()) 
print(df.columns) 
print(df.shape) 
 
# Transaction type breakdown 
print("Transaction counts by type:") 
print(df['type'].value_counts()) 
 
# Average amount per type 
print("Average amount by type:") 
print(df.groupby('type')['amount'].mean()) 
 
# Overall fraud rate 
fraud_rate = df['isFraud'].mean() * 100 
print(f"Overall fraud rate: {fraud_rate:.4f}%%") 
 
# Fraud rate by transaction type 
print("Fraud rate by type:") 
print(df.groupby('type')['isFraud'].mean() * 100) 
 
# Chart: transaction counts by type 
df['type'].value_counts().plot(kind='bar', title='Transaction Types') 
plt.savefig('transaction_types.png') 
plt.show() 
 
# Fraud rate by type chart 
(df.groupby('type')['isFraud'].mean() * 100).plot(kind='bar', title='Fraud Rate by Transaction Type (%%)', color='crimson') 
plt.ylabel('Fraud Rate (%%)') 
plt.savefig('fraud_rate_by_type.png') 
plt.show() 
