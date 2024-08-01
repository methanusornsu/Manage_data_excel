import pandas as pd
import os

# Directory containing the CSV files
directory = "D:\\Prowu\\data\\adnormal\\all"


# List of conditions and corresponding values
conditions = {
    "c-s": 1,
    "c-f": 2,
    "h-s": 3,
    "h-f": 4

}

# Loop through CSV files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        print("***************")
        # Read the CSV file into a DataFrame
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)

        # Extract the condition from the file name
        condition = None
        for key, value in conditions.items():
            if key in filename:
                condition = key
                break

        # Set the "intervene" column based on the condition
        if condition is not None:
            df['intervene'] = conditions[condition]
        else:
            df['intervene'] = 0

        # Save the updated DataFrame back to the same CSV file
        df.to_csv(file_path, index=False)  # Set index to False to avoid saving the index column

# import pandas as pd
# import os

# # Specify the file name you want to modify
# filename_to_modify = "D:\\SP_TrainData\\TrainData.csv"

# # Read the CSV file into a DataFrame
# file_path = os.path.join(filename_to_modify)
# if os.path.isfile(file_path):
#     df = pd.read_csv(file_path)

#     # Set the "intervene" column to 0 for all rows
#     df['intervene'] = 0

#     # Create a new file with the updated DataFrame
#     new_filename = "new_" + filename_to_modify
#     new_file_path = os.path.join(new_filename)
#     df.to_csv(new_file_path, index=False)  # Set index to False to avoid saving the index column

#     print(f"New file '{new_filename}' has been created with 'intervene' column set to 0.")
# else:
#     print(f"The specified file '{filename_to_modify}' does not exist.")


# import pandas as pd

# # Replace 'your_input_file.csv' with the path to your actual input CSV file
# input_file_path = "D:\\SP_TrainData\\TrainData.csv"

# # Read the CSV file into a DataFrame
# df = pd.read_csv(input_file_path)

# # Add a new column 'intervene' with all values set to 0
# df['intervene'] = 0

# # Replace 'your_output_file.csv' with the desired output file path
# output_file_path = "D:\\SP_TrainData\\new_TrainData.csv"

# # Save the updated DataFrame to a new CSV file
# df.to_csv(output_file_path, index=False)

# print(f"New column 'intervene' added to {output_file_path} with all values set to 0.")

# import pandas as pd

# def merge_two_csv_files(file1, file2, output_file):
#     # Read the two CSV files into DataFrames
#     df1 = pd.read_csv(file1)
#     df2 = pd.read_csv(file2)

#     # Merge the two DataFrames based on a common column (you can change 'common_column' to the actual common column name)
#     merged_data = pd.concat([df1, df2], axis=0, ignore_index=True)

#     # Write the merged data to a new CSV file
#     merged_data.to_csv(output_file, index=False)
#     print(f"Merged data saved to {output_file}")

# # Specify the paths to the two CSV files and the output file name
# file1_path = "D:\\SP_TrainData\\adnormal\\new_TrainData.csv"
# file2_path = "D:\\SP_TrainData\\adnormal\\data.csv"
# output_file = 'D:\\SP_TrainData\\adnormal\\merged_data555.csv'

# # Call the function to merge the two CSV files
# merge_two_csv_files(file1_path, file2_path, output_file)
