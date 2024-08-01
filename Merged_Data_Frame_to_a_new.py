# import pandas as pd

# # Create an empty list to store DataFrames read from CSV files
# dfs = []

# # Loop to read and combine data from all CSV files
# for i in range(1, 257):  # Iterate from 1 to 256
#     file_name = f'D:\\SP_TrainData\\adnormal\\hot_w_sub\\rawData ({i}).csv'
    
#     try:
#         df = pd.read_csv(file_name)
#         dfs.append(df)
#     except FileNotFoundError:
#         print(f"File not found: {file_name}")
#     except Exception as e:
#         print(f"An error occurred while reading {file_name}: {e}")

# # Check if any DataFrames were successfully read
# if len(dfs) > 0:
#     # Combine DataFrames into one
#     combined_df = pd.concat(dfs, ignore_index=True)

#     # Save the combined DataFrame to a CSV file
#     output_file = 'D:\\SP_TrainData\\adnormal\\hot_w_sub\\hot_w_sub.csv'
#     combined_df.to_csv(output_file, index=False)
#     print(f"Combined data saved to {output_file}")
# else:
#     print("No data was successfully read from CSV files.")

import pandas as pd
import os

# Directory containing the CSV files
directory = "D:\\Prowu\\data\\adnormal\\all"

# Initialize an empty DataFrame to store the merged data
merged_df = pd.DataFrame()

# Loop through CSV files in the directory and concatenate them
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        # Read the CSV file into a DataFrame
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)
        print("**********")
        # Concatenate the DataFrame to the merged_df
        merged_df = pd.concat([merged_df, df], ignore_index=True)

# Save the merged DataFrame to a new CSV file
output_file_path = "D:\\Prowu\\data\\adnormal\\all1.csv"
merged_df.to_csv(output_file_path, index=False)