import pandas as pd

def calculate_average(file_path, column_name):
    """
    Calculate the average of a specific column in a CSV file.

    Parameters:
    - file_path (str): The path to the CSV file.
    - column_name (str): The name of the column to calculate the average for.

    Returns:
    - float: The average value of the column.
    - str: A message if there are errors.
    """
    print(column_name)
    df = pd.read_csv(file_path)
    print(df[column_name])
    # try:
    # #     # Load the dataset
    #     df = pd.read_csv(file_path)

    #     # Check if the column exists
    #     if column_name not in df.columns:
    #         print("Column '{column_name}' not found in the dataset.")

    #     # Calculate the average
    #     average = df[column_name].mean()
    #     print(f"The average value of '{column_name}' is {average:.2f}")

    # except Exception as e:
    #     print(f"Error processing file: {e}")
