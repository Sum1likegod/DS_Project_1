import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def process_support_data(file_path):
    """
    A universal function to clean and visualize support ticket data.
    """
    # 1. Load Data
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        return "Error: File not found. Please check the path."
        return None

    # 2. Clean Data (Generalized logic)
    # This automatically finds all 'object' (text) columns and strips/lowers them
    for col in df.select_dtypes(include=['object', 'string']).columns:
        df[col] = df[col].str.strip().str.capitalize()

    # This finds all numerical columns and fills NaNs with the mean
    for col in df.select_dtypes(include=['number']).columns:
        df[col] = df[col].fillna(df[col].mean())


    # 3. Analyze & Visualize
    if 'Field' in df.columns:
        report = df['Field'].value_counts()
        report.plot(kind='bar', color='green')
        plt.title('Employee per Field')
        plt.xlabel('Field')
        plt.ylabel('Employee')
        plt.show()

    # 4. Save to the new folder
    output_folder = Path(__file__).parent / "processed_data"
    output_folder.mkdir(exist_ok=True)


    df.to_excel(output_folder / 'Book1_Cleaned.xlsx', index=False)
    print(f"Success! Cleaned file saved at: {output_folder}")

    return df


if __name__ == "__main__":
    base_path = Path(__file__).parent
    input_file = base_path / "raw_data" / "Book1.xlsx"

    ## For using it as the Jupyter notebook use this instead
    ## file_path = Path("your_example_file.xlsx")

    cleaned_df = process_support_data(input_file)
