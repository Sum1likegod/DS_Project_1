import pandas as pd
import matplotlib.pyplot as plt

# 1. THE DATA (Simulating a messy CSV)
raw_data = {
    'Employee': [' Amit', 'Suresh  ', 'Amit', ' Priya '],
    'Score': [8, 10, None, 7],
    'Department': ['Tech', 'Tech', 'Billing', 'Tech'],
    'Issue': ['LOGIN ERROR', 'payment failed', 'InVoIcE missing', 'Slow Website']
}

df = pd.DataFrame(raw_data)

# 2. THE CLEANING PHASE
# Task: Strip the 'Employee' names and Lowercase the 'Issue' column
df['Employee'] = df['Employee'].str.strip()
df['Issue'] = df['Issue'].str.lower()

# Task: Fill the missing 'Score' with the average
df['Score'] = df['Score'].fillna(df['Score'].mean())

# 3. THE ANALYSIS PHASE
# Task: Count how many tickets are in each Department
report = df['Department'].value_counts()

# 4. THE VISUALIZATION PHASE
report.plot(kind='bar', color='skyblue')
plt.title('Tickets by Department')
plt.show()

print("Cleaned Data:")
print(df)
print("\nDepartment Report:")
print(report)