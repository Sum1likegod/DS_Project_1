# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 1. THE DATA (Simulating a messy CSV)
# raw_data = {
#     'Employee': [' Amit', 'Suresh  ', 'Amit', ' Priya '],
#     'Score': [8, 10, None, 7],
#     'Department': ['Tech', 'Tech', 'Billing', 'Tech'],
#     'Issue': ['LOGIN ERROR', 'payment failed', 'InVoIcE missing', 'Slow Website']
# }
#
# df = pd.DataFrame(raw_data)
#
# # 2. THE CLEANING PHASE
# # Task: Strip the 'Employee' names and Lowercase the 'Issue' column
# df['Employee'] = df['Employee'].str.strip()
# df['Issue'] = df['Issue'].str.lower()
#
# # Task: Fill the missing 'Score' with the average
# df['Score'] = df['Score'].fillna(df['Score'].mean())
#
# # 3. THE ANALYSIS PHASE
# # Task: Count how many tickets are in each Department
# report = df['Department'].value_counts()
#
# # 4. THE VISUALIZATION PHASE
# report.plot(kind='bar', color='skyblue')
# plt.title('Tickets by Department')
# plt.show()
#
# print("Cleaned Data:")
# print(df)
# print("\nDepartment Report:")
# print(report)

import pandas as pd
import matplotlib.pyplot as plt


def process_support_data(file_path):
    """
    A universal function to clean and visualize support ticket data.
    """
    # 1. Load Data
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        return "Error: File not found. Please check the path."

    # 2. Clean Data (Generalized logic)
    # This automatically finds all 'object' (text) columns and strips/lowers them
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip().str.lower()

    # This finds all numerical columns and fills NaNs with the mean
    for col in df.select_dtypes(include=['number']).columns:
        df[col] = df[col].fillna(df[col].mean())

    # 3. Analyze & Visualize
    if 'department' in df.columns:
        report = df['department'].value_counts()
        report.plot(kind='bar', color='green')
        plt.title('Tickets per Department')
        plt.ylabel('Count')
        plt.show()

    return df

# How to use it for your freelancing gig:
excel_file = 'C:\Different Folder\Code\python\Restart\Book1.xlsx'
cleaned_df = process_support_data(excel_file)
print(cleaned_df)