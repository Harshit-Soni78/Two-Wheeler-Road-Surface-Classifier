import pandas as pd
import os

def split_csv(file_path, output_dir, chunk_size=250, file_index=1):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Get the base filename without extension
    base_filename = os.path.splitext(os.path.basename(file_path))[0]
    
    # Create a numbered folder for the file inside the output directory
    file_output_dir = os.path.join(output_dir, f"{file_index:03d}_{base_filename}")
    os.makedirs(file_output_dir, exist_ok=True)
    
    # Calculate number of full chunks
    num_chunks = len(df) // chunk_size
    
    # Split and save each chunk
    for i in range(num_chunks):
        chunk = df[i * chunk_size : (i + 1) * chunk_size]
        output_file = os.path.join(file_output_dir, f"{file_index:03d}_{base_filename}_part_{i+1:03d}.csv")
        chunk.to_csv(output_file, index=False)
        print(f"Saved: {output_file}")
    
    print(f"Splitting complete for {file_path}. Any remaining rows (less than 250) have been discarded.")

# Usage example
input_folder = 'F:/Study/sem 6/Mini Project/TWRSC_2/Two-Wheeler-Road-Surface-Classifier-main/04 Preprocessed Data/FInal Data/Kanker'  # Replace with your folder containing large CSV files
output_folder = 'F:/Study/sem 6/Mini Project/Abhijeet_Preprocessed_Data/kanker_processed'  # Replace with your desired output folder
os.makedirs(output_folder, exist_ok=True)

for file_index, filename in enumerate(sorted(os.listdir(input_folder)), start=1):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_folder, filename)
        split_csv(file_path, output_folder, file_index=file_index)

